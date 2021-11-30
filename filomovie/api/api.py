import json
from filomovie.database.functions import insert_movie, delete_movie

def check_en(dict_list):
    for elem in dict_list:
        if elem['iso_639_1'] == 'en':
            return True
    return False

def filter_movies():
    with open("filtered_data.txt", 'w') as outFile:
        with open('movie_ids_10_18_2021.json', encoding='utf8') as inFile:
            for line in inFile:
                data = json.loads(line)
                if data['popularity'] >= 10:
                    outFile.write(json.dumps(data) + '\n')

def api_parse():
    from urllib.request import urlopen
    import json
    apikey = 'df6bf47dab73bc03ab03b122a62753c9'
    baseurl = 'https://api.themoviedb.org/3/movie/'
    posterpath = 'https://image.tmdb.org/t/p/original'

    open("data2send.txt", "w").close()
    #movie_id, movie_image, movie_title, movie_desc, stream
    with open('filtered_data.txt', 'r', encoding='utf8') as f:
        for line in f:
            info_dict = {'movie_id':"", 'movie_image':"", 'movie_title':"", 'movie_desc':"", 'stream_providers':""}
            stream = []
            data = json.loads(line)
            movie_id = data['id']
            if data['popularity'] < 10:
                continue
            info_dict['movie_id'] = movie_id
            url = baseurl + str(movie_id) + '?api_key=' + apikey
            try:
                output = urlopen(url)
            except:
                print(f"Movie id: {str(movie_id)} not a URL")
                continue
            info = json.loads(output.read())
            if info['original_language'] == 'en' and check_en(info['spoken_languages']):
                info_dict['movie_title'] = info['title']
                if info['poster_path'] != None:
                    info_dict['movie_image'] = posterpath + info['poster_path']
                info_dict['movie_desc'] = info['overview']
                info_dict['runtime'] = info['runtime']
                info_dict['rating'] = info['vote_average']
                info_dict['release_date'] = info['release_date']
                genres = []
                for i in info['genres']:
                    genres.append(i['name'])
                info_dict['genres'] = genres
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
                insert_movie(info_dict['movie_id'], info_dict['movie_image'], info_dict['movie_title'],
                             info_dict['movie_desc'], json.dumps(info_dict['stream_providers']), info_dict['runtime'],
                             info_dict['rating'], info_dict['release_date'], json.dumps(info_dict['genres']))

filter_movies()
api_parse()