# Weather/Stock data to a Streamlit dashboard

# 1. Project Overview
![Process overview](images/design.png)

This project focuses on gathering weather data for [`Dublin`, `Delhi`, `Spain`, `Bali`] using the Open Meteo API and utilizing Apache Airflow, ElephantSQL, and Streamlit to create a simple dashboard from the data.

By leveraging the Open Meteo API, the project retrieves up-to-date weather information for [`Dublin`, `Delhi`, `Spain`, `Bali`]. Apache Airflow is employed to automate the extraction and transformation of this data, ensuring a continuous and reliable pipeline.

The weather data is then stored and managed in DB on elephantSQL, a powerful cloud-based Postgres database. And lastly Streamlit is used to visualize the data.

The outcome was a simple dashboard containing the daily average temperature of these cities and stock valuation.

![Streamlit dashboard](images/dashboard.png.jpg)

# 2. Retrieving the data from the API

The data source for this project is an API that provides weather forecasts. The API offers the following features:

* End point ***'[https://api.weatherapi.com/v1/](https://api.weatherapi.com/v1/)'***
* Parameters 
    * ***'location'***:  Name of the location (optional).
    * ***'latitude'*** & ***'longitude'***:  Geographical coordinates of the location (optional).
    * ***'elevation'***: Elevation used for statistical downscaling (optional).
    * ***'hourly'***: List of weather variables to be returned (optional).
    * ***'daily'***: List of daily weather variable aggregations to be returned (optional).
    * ***'current_weather'***: Flag to include current weather conditions in the output (optional).
    * Other parameters such as temperature unit, windspeed unit, time format, timezone, etc. (optional).

## 2.1 Integration
\
The integration with the API involves making HTTP requests to the ***'/v1'*** endpoint, passing the necessary parameters, and retrieving the JSON response containing the weather forecast data.

The API documentation [https://www.weatherapi.com/docs/](https://www.weatherapi.com/docs/) provides detailed information about the available parameters, valid values, and the structure of the JSON response. By leveraging the API's capabilities, we can retrieve accurate and up-to-date weather forecasts for a given location.

# 3. [ElephantSQL](https://www.elephantsql.com/) integration

The Integration to ElephantSQL begins from creating the necessary database for the project in [ElephantSQl portal](https://www.elephantsql.com/):

![Creating a Elephant database](images/6.jpg)

After creating the database save username and password

# 4. Streamlit

# Conclusion 

In conclusion, the main focus of the project was to learn how to integrate Apache Airflow with various service providers. This involved understanding the concepts of Apache Airflow, exploring different service providers' APIs, and implementing the necessary connections to enable seamless integration.

Future improvement ideas could include retrieving data for more than one city and modifying the dashboard in a way that the user could select the city for which they would want to display the weather information.