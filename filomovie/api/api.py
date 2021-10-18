from urllib.request import urlopen
import json

apikey = 'api_key_here'
baseurl = 'https://api.themoviedb.org/3/movie/'
posterpath = 'https://image.tmdb.org/t/p/original'

info_dict = {}
stream = []
open("data2send.txt", "w").close()
#movie_id, movie_image, movie_title, movie_desc, stream
with open('file_test.txt') as f:
    for line in f:
        data = json.loads(line)
        movie_id = data['id']
        info_dict['movie_id'] = movie_id
        url = baseurl + str(movie_id) + '?api_key=' + apikey
        output = urlopen(url)
        info = json.loads(output.read())
        info_dict['movie_title'] = info['title']
        info_dict['movie_image'] = posterpath + info['poster_path']
        info_dict['movie_desc'] = info['overview']
        print(info)
        url = baseurl + str(movie_id) + '/watch/providers?api_key=' + apikey
        output = urlopen(url)
        info = json.loads(output.read())
        providers = info['results']['US']['flatrate']
        for p in providers:
            stream.append(p['provider_name'])
        info_dict['stream_providers'] = stream
        dump = json.dumps(info_dict)
        g = open("data2send.txt", "a")
        g.write(dump + '\n')
g.close()
