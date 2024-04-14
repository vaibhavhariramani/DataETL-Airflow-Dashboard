import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import sys

# Fetch weather data from API
def fetch_weather(api_key):
    print("Fetching weather data...")
    locations = ['Dublin', 'Delhi', 'Spain', 'Bali']
    weather_data = []
    for location in locations:
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}')
        data = response.json()
        print(f"Received weather data for {location}: {data['current']['temp_c']}")
        weather_data.append({
            'location': location,
            'temperature': data['current']['temp_c'],
            'weather_icon': data['current']['condition']['icon']
        })
    return weather_data

# Transform data using pandas
def transform_data(weather_data):
    print("Transforming data...")
    return pd.DataFrame(weather_data)

# Load data into database
def load_data(df, db_url):
    print("Loading data into database...")
    engine = create_engine(db_url)
    df.to_sql('weather_forecast', engine, if_exists='replace', index=False)
    print("Data loaded into database successfully.")

# Fetch stock data from API
def fetch_stock_data(api_key, symbols):
    print("Fetching stock data...")
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
    all_data = []
    day_today = datetime.today()
    if day_today.weekday() == 5:  # If today is Saturday (Saturday is 5)
        day_today -= timedelta(days=1)  # Get data for Friday
    elif day_today.weekday() == 6:  # If today is Sunday (Sunday is 6)
        day_today -= timedelta(days=2)  # Get data for Friday
    for symbol in symbols:
        url = base_url + '&symbol=' + symbol + '&apikey=' + api_key
        print(url)
        response = requests.get(url)
        data = response.json()
        if 'Time Series (Daily)' in data:
            # Convert JSON response to DataFrame
            df = pd.DataFrame(data['Time Series (Daily)']).T
            # Calculate moving average
            df.index = pd.to_datetime(df.index)
            df['Open'] = df['1. open'].astype(float)
            df['High'] = df['2. high'].astype(float)
            df['Low'] = df['3. low'].astype(float)
            df['Close'] = df['4. close'].astype(float)
            df['Volume'] = df['5. volume'].astype(int)
            print(day_today.date())
            df = df.head(5)
            df.drop(columns=['1. open', '2. high', '3. low', '4. close', '5. volume'], inplace=True)
            df['Symbol'] = symbol
            print(f"Received stock data for {symbol}: {df.head(3)}")
            all_data.append(df)
    return pd.concat(all_data)

# Load stock data into database
def load_stock_data(df, db_url):
    print("Loading stock data into database...")
    engine = create_engine(db_url)
    df.to_sql('stock_forecast', engine, if_exists='replace', index=False)
    print("Stock data loaded into database successfully.")

# Main function
def main(weather_api_key, stock_api_key, db_url):
    api_key = weather_api_key
    db_url = db_url
    weather_data = fetch_weather(api_key)
    stock_data = fetch_stock_data(api_key=stock_api_key, symbols=['AAPL', 'GOOGL', 'MSFT'])
    load_data(transform_data(weather_data), db_url)
    load_stock_data(stock_data, db_url)

if __name__ == '__main__':
    # Parse command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python etl.py <weather_api_key> <stock_api_key> <db_url>")
        sys.exit(1)
    
    weather_api_key = sys.argv[1]
    stock_api_key = sys.argv[2]
    db_url = sys.argv[3]

    print("Starting ETL process...")
    # Call main function with command-line arguments
    main(weather_api_key, stock_api_key, db_url)
    print("ETL process completed successfully.")
