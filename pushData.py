import requests

URL = 'http://127.0.0.1:8000/'

data = {
    'name' : 'daddaddd',
    'description' : 'descr',
    'image_link' : 'img_link',
    'anime_link' : 'anime_lik'
}

def pushData(all_anime_data):

    for data_key in all_anime_data: 
        data = all_anime_data[data_key]
        try : 
            anime_data = {
                'name' : data['title'],
                'description' : data['description'],
                'image_link' : data['image'],
                'anime_link' : data['link']
            }

            res = requests.post(URL+'pushAnime/', data=anime_data)
            print(f'Push data -- > {res.status_code}')
            
            for genre in data['genre']:

                res = requests.post(URL+'pushGenre/', data={'name' : genre, 'description' : '#TODO'})
                print(f'Push data pushGenre-- > {res.status_code}')
                
                anime_genre_data = {
                    'anime' : data['title'],
                    'genre' : genre
                }
                res = requests.post(URL+'pushAnimeGenre/', data=anime_genre_data)
                print(f'Push data Anime/Genre -- > {res.status_code}')
            
            
        except Exception as e:
            print(e)