import pybitflyer

api = pybitflyer.API()

for k, v in api.ticker(product_code = "BTC_JPY").items():
    print(k, v)