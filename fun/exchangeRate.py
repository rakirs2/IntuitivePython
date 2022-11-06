import requests

# Where USD is the base currency you want to use

APIKEY = '2d60bd82198b7498a20af176'
url = 'https://v6.exchangerate-api.com/v6/2d60bd82198b7498a20af176/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data)
			