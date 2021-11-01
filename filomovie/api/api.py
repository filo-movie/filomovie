import json
from filomovie.database.functions import insert_movie

def check_en(dict_list):
    for elem in dict_list:
        if elem['iso_639_1'] == 'en':
            return True
    return False

def api_parse():
    from urllib.request import urlopen
    import json
    apikey = 'df6bf47dab73bc03ab03b122a62753c9'
    baseurl = 'https://api.themoviedb.org/3/movie/'
    posterpath = 'https://image.tmdb.org/t/p/original'

    open("data2send.txt", "w").close()
    #movie_id, movie_image, movie_title, movie_desc, stream
    with open('movie_ids_10_18_2021.json', encoding='utf8') as f:
        for line in f:
            info_dict = {'movie_id':"", 'movie_image':"", 'movie_title':"", 'movie_desc':"", 'stream_providers':""}
            stream = []
            providers = []
            data = json.loads(line)
            movie_id = data['id']
            info_dict['movie_id'] = movie_id
            url = baseurl + str(movie_id) + '?api_key=' + apikey
            output = urlopen(url)
            info = json.loads(output.read())
            if info['original_language'] == 'en' and check_en(info['spoken_languages']):
                info_dict['movie_title'] = info['title']
                if info['poster_path'] != None:
                    info_dict['movie_image'] = posterpath + info['poster_path']
                info_dict['movie_desc'] = info['overview']
                url = baseurl + str(movie_id) + '/watch/providers?api_key=' + apikey
                output = urlopen(url)
                info = json.loads(output.read())
                if info['results'] and 'US' in info['results'].keys():
                    if 'flatrate' in info['results']['US']:
                        providers = info['results']['US']['flatrate']
                        for p in providers:
                            stream.append(p['provider_name'])
                    else:
                        stream = []
                info_dict['stream_providers'] = stream
                dump = json.dumps(info_dict)
                g = open("data2send.txt", "a", encoding='utf8')
                g.write(dump + '\n')
                g.close()

api_parse()
with open("data2send.txt") as f:
    for line in f:
        data = json.loads(line)
        insert_movie(data['movie_id'], data['movie_image'], data['movie_title'], data['movie_desc'], json.dumps(data['stream_providers']))