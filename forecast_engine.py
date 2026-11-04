import pandas as pd

def create_forecast(data,horizon):
 avg=float(pd.to_numeric(data['COST_USD'],errors='coerce').fillna(0).tail(12).mean())
 return pd.DataFrame({'Month':range(1,horizon+1),'Forecast':[avg]*horizon})
