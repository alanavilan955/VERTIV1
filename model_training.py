from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd

def train_model(df):
 d=df.copy()
 if 'COST_USD' not in d.columns: raise ValueError('COST_USD not found')
 d['COST_USD']=pd.to_numeric(d['COST_USD'],errors='coerce').fillna(0)
 d=d.head(min(len(d),50000))
 X=pd.DataFrame({'idx':range(len(d))})
 y=d['COST_USD']
 m=RandomForestRegressor(n_estimators=100,random_state=42)
 m.fit(X,y)
 pred=m.predict(X)
 return m,{'MAE':float(mean_absolute_error(y,pred))},d
