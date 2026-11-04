import streamlit as st
import pandas as pd
from data_preparation import prepare_data
from model_training import train_model
from forecast_engine import create_forecast
st.set_page_config(layout="wide")
st.title("Manufacturing Finance Forecast")
file=st.file_uploader("Oracle Excel",type=['xlsx'])
if file:
 df=prepare_data(file)
 model,metrics,data=train_model(df)
 st.write(metrics)
 horizon=st.slider('Months',3,12,6)
 fc=create_forecast(data,horizon)
 st.dataframe(fc)
