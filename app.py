import time
from libs.openexchange import OpenExchangeClient


APP_ID = "1f0598dacee64b79a89a68734e798d95"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)

print(f'UDS {usd_amount} is equivalent to GBP {gbp_amount:.2f}')
