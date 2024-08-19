import streamlit as st
from weather_backend import get_weather_data
from streamlit.components.v1 import html

# Set your OpenWeatherMap API Key
API_KEY = 'e7dd30ae458db307e4be21b79847e940'

# Load SVG file
with open('D:/Aravind/AI/generate_frontend_and_backedn_from_svg/attempt_with_chatgpt/weather_template.svg', 'r') as file:
    svg = file.read()


# Streamlit app
st.title("Weather App")

# Input for the city
city = st.text_input("Enter a city", "Bangalore")

# Fetch weather data
weather = get_weather_data(API_KEY, city)

if weather:
    # Display SVG with weather data
    svg_with_data = svg.replace("{{city}}", weather["city"])\
                       .replace("{{temperature}}", f"{weather['temperature']} °C")\
                       .replace("{{description}}", weather["description"])

    # Embed SVG into Streamlit app
    html(svg_with_data, height=600, width=1000)
else:
    st.error("City not found or API error.")