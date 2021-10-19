import json
from filomovie.database.functions import insert_movie

def api_parse():
    from urllib.request import urlopen
    import json
    apikey = 'df6bf47dab73bc03ab03b122a62753c9'
    baseurl = 'https://api.themoviedb.org/3/movie/'
    posterpath = 'https://image.tmdb.org/t/p/original'

    open("data2send.txt", "w").close()
    #movie_id, movie_image, movie_title, movie_desc, stream
    with open('file_test.txt') as f:
        for line in f:
            info_dict = {}
            stream = []
            providers = []
            data = json.loads(line)
            movie_id = data['id']
            info_dict['movie_id'] = movie_id
            url = baseurl + str(movie_id) + '?api_key=' + apikey
            output = urlopen(url)
            info = json.loads(output.read())
            info_dict['movie_title'] = info['title']
            info_dict['movie_image'] = posterpath + info['poster_path']
            info_dict['movie_desc'] = info['overview']
            url = baseurl + str(movie_id) + '/watch/providers?api_key=' + apikey
            output = urlopen(url)
            info = json.loads(output.read())
            if 'flatrate' in info['results']['US']:
                providers = info['results']['US']['flatrate']
                for p in providers:
                    stream.append(p['provider_name'])
            else:
                stream = []
            info_dict['stream_providers'] = stream
            dump = json.dumps(info_dict)
            g = open("data2send.txt", "a")
            g.write(dump + '\n')
            g.close()

api_parse()
with open("data2send.txt") as f:
    for line in f:
        data = json.loads(line)
        insert_movie(data['movie_id'], data['movie_image'], data['movie_title'], data['movie_desc'], data['stream_providers'])