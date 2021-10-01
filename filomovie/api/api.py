from urllib.request import urlopen
import json

apikey = 'api_key_here'
baseurl = 'https://api.themoviedb.org/3/'
url1 = baseurl + 'search/movie?api_key=' + apikey + '&query=Shrek'

response1 = urlopen(url1)
data1 = json.loads(response1.read())

movieid = data1['results'][0]['id']
url2 = 'https://api.themoviedb.org/3/movie/' + str(movieid) + '/watch/providers?api_key=' + apikey
response2 = urlopen(url2)
data2 = json.loads(response2.read())

providers = data2['results']['US']['flatrate']

print(providers)
