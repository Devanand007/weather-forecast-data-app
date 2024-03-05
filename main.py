import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} in {place}")

if place:
    try:
        filtered_data = get_data(place, days)


        if option == 'Temperature':
            temp = [dicts['main']['temp'] / 10 for dicts in filtered_data]
            dates = [dicts["dt_txt"] for dicts in filtered_data]
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [dicts["weather"][0]["main"] for dicts in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            print(sky_condition)
            st.image(image_path, width=115)
    except KeyError:
        st.write("Place doesnt Exist")


