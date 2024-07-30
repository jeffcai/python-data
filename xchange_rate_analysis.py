from fredapi import Fred

# Get a free API key from the FRED website
fred = Fred(api_key='xxxxx')

# Search for the required data using keywords
fred.search("Exchange monthly China")

# Extract the required data set using the series ID obtained from the search
ind_monthly = fred.get_series(series_id = 'EXCHUS')
