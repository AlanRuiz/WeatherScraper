import functions
import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv("data.txt")
dates = data["date"]
weathers = data["temp"]

st.title("Weather Scraper")
weather_timeline = px.line(x=dates, y=weathers, labels={"x":"Date","y":"Temperature(Celcius)"})
st.plotly_chart(weather_timeline)
