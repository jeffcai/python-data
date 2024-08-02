from fredapi import Fred

# Get a free API key from the FRED website
fred = Fred(api_key='xxx')

# Search for the required data using keywords
fred.search("Exchange monthly China")

# Extract the required data set using the series ID obtained from the search
ind_monthly = fred.get_series(series_id = 'EXCHUS')

import pandas as pd

# Convert the series to a data frame
ind_df = pd.DataFrame({'Exchange_rate': ind_monthly})

# Slice the dataset from 01st January 2014 to 31st October 2023
ind_df = ind_df.loc['2014-01-01':'2023-11-01']

# Set the date index to `datetime` format
ind_df.index = pd.to_datetime(ind_df.index)

# Set the period of the time-series data
ind_df = ind_df.asfreq('MS')

# import the seasonal decomposition function
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose into trend, seasonal, and residual components
ind_decomposition = seasonal_decompose(ind_df['Exchange_rate'], model='additive', period = 12)
ind_trend =ind_decomposition.trend
ind_seasonal = ind_decomposition.seasonal
ind_residual = ind_decomposition.resid

import matplotlib.pyplot as plt

# # Plot the deconposition
# plt.figure(figsize = (20,8))
# plt.subplot(411)
# plt.title("Indian Rupees - Seasonal Decomposition of Exchange Rates with US Dollars")
# plt.plot(ind_df, label = "Original")
# plt.legend(loc = "upper left")
# plt.subplot(412)
# plt.plot(ind_trend, label = "Trend")
# plt.legend(loc = "upper left")
# plt.subplot(413)
# plt.plot(ind_seasonal, label = "Seasonality")
# plt.legend(loc = "upper left")
# plt.subplot(414)
# plt.plot(ind_residual, label = "Residual")
# plt.legend(loc = "upper left")
# plt.tight_layout()
# plt.show()

# ADF test for stationarity
from statsmodels.tsa.stattools import adfuller

# Perform the Augmented Dickey-Fuller (ADF) test
result = adfuller(ind_df['Exchange_rate'])

# Extract and print the test statistic and p-value
adf_statistic = result[0]
p_value = result[1]
print("ADF Statistic:", adf_statistic)
print("p-value:", p_value)
print('Critical Values', result[4])

# Creating the differenced data from the existing column
ind_df['Differenced_Data'] = ind_df['Exchange_rate'].diff()
ind_df = ind_df.dropna() # dropping the first row

# # ACF plot
# plt.figure(figsize=(10, 6))
# plot_acf(ind_df['Differenced_Data'], label = "INR", lags=30)
# plt.xlabel('Lag')
# plt.ylabel('Autocorrelation')
# plt.legend()
# plt.show()

# # PACF plot
# plt.figure(figsize=(10, 6))
# plot_pacf(ind_df['Differenced_Data'], label = "INR", lags=30)
# plt.xlabel('Lag')
# plt.ylabel('Partial Autocorrelation')
# plt.legend()
# plt.show()

# Splitting the dataset into train and test sets
split_index = int(0.9 * len(ind_df))
ind_train = ind_df['Differenced_Data'].iloc[:split_index]
ind_test = ind_df['Differenced_Data'].iloc[split_index:]

print(split_index)
print(ind_train)
print(ind_test)

from statsmodels.tsa.arima.model import ARIMA

# # Fitting the ARMA model
# ind_model = ARIMA(ind_train, order=(9,0,9))
# ind_model_fit = ind_model.fit()

# # Predicting the test values
# start = len(ind_train)
# end = len(ind_train) + len(ind_test) - 1
# ind_pred = ind_model_fit.predict(start, end)

# Defining the forecast horizon and index
forecast_index = pd.date_range(start = '2023-12-01', periods =10, freq = 'MS')
print(forecast_index)

# Forecasting the differenced exchange rate
ind = ARIMA(ind_df['Differenced_Data'], order = (9,0,9))
print("start fitting")

ind_model = ind.fit()
print("finish fitting")

ind_forecast = ind_model.forecast(steps=10)
ind_forecast.index = forecast_index.astype(str)

# Converting the differenced data into actual exchange rate ratios
ind_forecast_rates = ind_df['Exchange_rate'].iloc[-1] + ind_forecast.cumsum()
ind_forecasts = pd.concat([ind_df['Exchange_rate'], ind_forecast_rates], axis = 0)
