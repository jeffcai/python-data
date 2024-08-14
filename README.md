# Data processing coded with Python

To code something with Python for analysing data, and code machine learning algorithms.

## To Run

To initialize environment, run the commands below:

> python -m venv .env
>
> source .env/bin/activate

To install dependencies, run "pip install -r requirements.txt" script at the root of the project, to speed up in China, use mirror like to append the script "-i https://pypi.tuna.tsinghua.edu.cn/simple/";


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

### more code relevant to Data Lake or Lake House

TODO

docker compose to start containers for MinIO/Dremio/Nessie by referring to the code repo: https://github.com/miniohq/datalake_ref_arch (note that the code repo is to create data source in Dremio with Nessie for catalog)

Run execute: brew install apache-spark; once done, to run spark-shell for quick running script in terminal but which is optional

``` unclear about it yet, what causes error below when running python script (the line of dropping table, but comment it and run it again the table can be created, but another failure when insert data)
24/08/14 21:30:46 WARN FileSystem: Failed to initialize fileystem hdfs://master:8020/user/hive/warehouse: java.lang.IllegalArgumentException: java.net.UnknownHostException: master
24/08/14 21:30:46 WARN SharedState: Cannot qualify the warehouse path, leaving it unqualified.
java.lang.IllegalArgumentException: java.net.UnknownHostException: master
```



Run "python3 pyspark-iceberg-test.py", at first it will download dependencies (maven) from maven repo, note that it's to download maven jars during executing the python script, which may a bit slow like in China

After execution, you can access to view what table created and data inserted via Spark SQL implemented in the python script mentioned above:
- MinIO: http://localhost:9051/login, with account minioadmin/minioadmin;
- Dremio: http://localhost:9053/login, with account admin/bad4admins;
- Nessie: http://localhost:19120/tree/main.

## Tips

The pyrightconfig file is used to enable Python virtual environment (so that code navigation works).

## References
- [Python 数据分析工具箱](https://xiangyun.rbind.io/2024/03/python-data-analysis-toolbox/)
- [用 Python 语言开发 Shiny 应用](https://xiangyun.rbind.io/2024/04/shiny-for-python/)
- [Time-Series Analysis and Forecasting of Foreign Exchange Rate with ARIMA Model](https://medium.com/womenintechnology/foreign-exchange-rate-time-series-analysis-and-forecasting-with-arima-model-c22f7972fd36)
- [Time-Series Analysis and Forecasting of Foreign Exchange Rate with SARIMAX Model](https://medium.com/womenintechnology/time-series-analysis-and-forecasting-of-foreign-exchange-rate-with-sarimax-model-efbc39babd33)
- [动手实战人工智能 AI By Doing](https://aibydoing.com/)
- [现代应用统计](https://bookdown.org/xiangyun/masr/)
- [Modern Datalake Reference Tech Stack, docker compose for MinIO/Dremio/Nessie ...](https://github.com/miniohq/datalake_ref_arch)
