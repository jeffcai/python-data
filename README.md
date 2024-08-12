# Data processing coded with Python

To code something with Python for analysing data, and code machine learning algorithms.

## To Run

To initialize environment, run the commands below:

> python -m venv .env
>
> source .env/bin/activate

To install dependencies, run "pip install -r requirements.txt" script at the root of the project.

### shiny application

Run "shiny run" script in terminal to run shiny app (coded in the app.py).

### time series analysis and forcasting of exchange rate

Request API key accessing the URL https://fredaccount.stlouisfed.org/apikey, need registration first if not yet

Can search to find series id, such as Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate: https://fred.stlouisfed.org/series/DEXCHUS, which id is DEXCHUS and frequency is Daily, the EXCHUS https://fred.stlouisfed.org/series/EXCHUS frequency is monthly

Edit the xchange_rate_analysis.py to replace API key and series id with yours.

No complete yet - TODO

### more code relevant to Machine Learning/Data Science

TODO

### more code relevant to Modern Applied Statistics

TODO

## Tips

The pyrightconfig file is used to enable Python virtual environment (so that code navigation works).

## References
- [Python 数据分析工具箱](https://xiangyun.rbind.io/2024/03/python-data-analysis-toolbox/)
- [用 Python 语言开发 Shiny 应用](https://xiangyun.rbind.io/2024/04/shiny-for-python/)
- [Time-Series Analysis and Forecasting of Foreign Exchange Rate with ARIMA Model](https://medium.com/womenintechnology/foreign-exchange-rate-time-series-analysis-and-forecasting-with-arima-model-c22f7972fd36)
- [Time-Series Analysis and Forecasting of Foreign Exchange Rate with SARIMAX Model](https://medium.com/womenintechnology/time-series-analysis-and-forecasting-of-foreign-exchange-rate-with-sarimax-model-efbc39babd33)
- [动手实战人工智能 AI By Doing](https://aibydoing.com/)
- [现代应用统计](https://bookdown.org/xiangyun/masr/)
