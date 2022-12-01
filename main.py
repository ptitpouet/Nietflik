import requests

# api-url
API_URL = "http://localhost:8000/api/v1"

# api-uri
TITLE_URI = "/titles/"
GENRES_URI = "/genres/"
MAX_PAGE_SIZE_PARAM = "?page_size=50"
SEVEN_ITEM_PARAM = "?page_size=7"
SEVEN_PLUS_ITEM_PARAM = "?page_size=8"
GENRE_PARAM = "&genre="
SORT_IMDB_PARAM = "&sort_by=-imdb_score"


# sending get request and saving the response as response object
top_response = requests.get(url = API_URL + TITLE_URI + SEVEN_PLUS_ITEM_PARAM + SORT_IMDB_PARAM)

# extracting data in json format
top_response_data_dict = top_response.json()
top_response_status_code = top_response.status_code


for title in top_response_data_dict['results']:
    if title is top_response_data_dict['results'][0] :
        print("   > HIGHLIGHT")
        best_movie_id = title["id"]
        # sending get request and saving the response as response object
        best_response = requests.get(url=API_URL + TITLE_URI + str(best_movie_id))
        # extracting data in json format
        best_response_data_dict = best_response.json()
        best_response_status_code = best_response.status_code
        print(best_response_data_dict["title"] + " [" + best_response_data_dict["url"] + "]")
        print(best_response_data_dict["description"])
    elif title is top_response_data_dict['results'][1] :
        print("   > TOP 7")
        print(title["title"] + " [" + title["image_url"] + "]")
    else:
        print(title["title"] + " [" + title["image_url"] + "]")

# sending get request and saving the response as response object
genres_response = requests.get(url = API_URL + GENRES_URI + MAX_PAGE_SIZE_PARAM)

# extracting data in json format
genres_data_dict = genres_response.json()
genres_status_code = genres_response.status_code


for genre in genres_data_dict['results']:
    print("   >" + genre['name'])
    response = requests.get(url=API_URL + TITLE_URI + SEVEN_ITEM_PARAM + GENRE_PARAM + genre['name'])
    current_genre_data_dict = response.json()
    #print(current_genre_data_dict)
    for title in current_genre_data_dict['results']:
        print(title["title"]+ " [" + title["image_url"] + "]")
