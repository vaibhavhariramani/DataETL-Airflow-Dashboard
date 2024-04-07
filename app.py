import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Custom CSS
st.markdown(
    """
    <style>
    .fullScreenFrame > div[data-baseweb="modal"] > div > div > div {
        max-width: 100% !important;
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Connect to PostgreSQL database
engine = create_engine('postgresql://yqyyzzpf:lNbslDvgYQpEz01H3QL8hD28aQn0H4PL@cornelius.db.elephantsql.com/yqyyzzpf')

# Fetch data from PostgreSQL
def fetch_data_from_db():
    # Fetch stock data
    query_stock = 'SELECT * FROM stock_forecast'
    df_stock = pd.read_sql(query_stock, engine)

    # Fetch weather data
    query_weather = 'SELECT * FROM weather_forecast'
    df_weather = pd.read_sql(query_weather, engine)

    return df_stock, df_weather

# Streamlit UI
def main():
    st.title('Dashboard')
    st.write('Stock and Weather Data')
    
    # Fetch data
    df_stock, df_weather = fetch_data_from_db()

    # Display weather data
    # st.subheader('Weather Data')
    # st.write(df_weather)

    # Display weather data
    st.subheader('Weather Data')
    # for index, row in df_weather.iterrows():
        
    #     image = row['weather_icon']
    #     # print(image)
    #     st.markdown("![Alt Text](%s)" % image)
    #     st.write(f"City: {row['location']}")
    #     st.write(f"Temperature: {row['temperature']} °C")

    weather_rows = []
    for index, row in df_weather.iterrows():
        image = row['weather_icon']
        weather_rows.append(
            f"![Weather Icon]({image})  **City:** {row['location']}  **Temperature:** {row['temperature']} °C \n"
        )
    
    st.write("\n".join(weather_rows), unsafe_allow_html=True)
    
    # Display stock data
    st.subheader('Stock Data')
    st.write(df_stock)

    # Visualizations
    st.subheader('Stock Price Visualization')
    
    # Line Chart
    fig = px.line(df_stock, x=df_stock.index, y='Close', color='Symbol', title='Closing Price')
    st.plotly_chart(fig)
    
    # Candlestick Chart
    fig_candlestick = px.line(df_stock, x=df_stock.index, y=['Open', 'High', 'Low', 'Close'], title='Candlestick Chart')
    st.plotly_chart(fig_candlestick)
    
    # Bar Chart
    fig_volume = px.bar(df_stock, x=df_stock.index, y='Volume', color='Symbol', title='Volume')
    st.plotly_chart(fig_volume)

if __name__ == "__main__":
    main()
