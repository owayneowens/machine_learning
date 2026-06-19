# Weekly Arrest Forecasting (Charleston, SC)

A machine learning project that forecasts weekly arrest counts across Charleston zip codes using historical arrest records and local weather.

## What it does
- Pulls arrest data from 2015 to 2024 across 37 Charleston zip codes
- Joins it with weather (temperature, precipitation, wind) from the Open-Meteo API
- Aggregates everything to weekly counts per zip code, then engineers features: lagged counts (1 to 4 weeks), rolling averages (4, 8, and 12 weeks), seasonal flags, and weather interactions
- Trains and tunes two models to predict the next week's arrests

## Models and results
| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| XGBoost (best) | 5.91 | 3.34 | 0.83 |
| Random Forest | 6.29 | 3.40 | 0.81 |

Both models were tuned with GridSearchCV using TimeSeriesSplit, so the cross-validation respects time order and never trains on the future. Features were normalized with RobustScaler.

## Stack
Python, pandas, scikit-learn, XGBoost, matplotlib.

## Files
- `crime_count.ipynb` is the main analysis and modeling notebook
- `script.ipynb` covers data prep and exploration
- The CSV files are the raw and combined arrest and weather data
