# 문제
# 아래 코드는 영화의 장르id를 장르 이름으로 바꿔서 영화 정보를 출력하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output:
# {'genre_names': ['Drama', 'Crime'],
#  'id': 278,
#  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는  
# 누명을 쓴다. 주변의 증언과 살해 현장의 '
#              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥 
# 같은 교도소 쇼생크로 향한다. 인간 말종 '
#              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한
#  취급을 당한다. 그러던 어느 날, 간수의 '
#              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하
# 게 된다. 그 와중에 교도소 소장은 죄수들을 '
#              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려
# 주면서 그의 돈을 관리하는데...',
#  'title': '쇼생크 탈출',
# 'vote_average': 8.7}

# 오류 코드
# from pprint import pprint


# def movie_info(movie, genres):
#     genres_names = []
#     genre_ids = movie["genre_ids"]
#     for genre_id in genre_ids:
#         for genre in genres:
#             if genre_id == genre["id"]:
#                 genre_name = genre["name"]
#                 genres_names.append(genre_name)

#     new_movie_info = {
#         "genre_names": genres_names,
#         "id": movie["id"],
#         "overview": movie["overview"],
#         "title": movie["title"],
#         "vote_average": movie["vote_average"],
#     }



# if __name__ == "__main__":
#     movie = {
#         "adult": False,
#         "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
#         "genre_ids": [18, 80],
#         "id": 278,
#         "original_language": "en",
#         "original_title": "The Shawshank Redemption",
#         "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
#         "popularity": 67.931,
#         "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
#         "release_date": "1995-01-28",
#         "title": "쇼생크 탈출",
#         "video": False,
#         "vote_average": 8.7,
#         "vote_count": 18040,
#     }

#     genres_list = [
#         {"id": 28, "name": "Action"},
#         {"id": 12, "name": "Adventure"},
#         {"id": 16, "name": "Animation"},
#         {"id": 35, "name": "Comedy"},
#         {"id": 80, "name": "Crime"},
#         {"id": 99, "name": "Documentary"},
#         {"id": 18, "name": "Drama"},
#         {"id": 10751, "name": "Family"},
#         {"id": 14, "name": "Fantasy"},
#         {"id": 36, "name": "History"},
#         {"id": 27, "name": "Horror"},
#         {"id": 10402, "name": "Music"},
#         {"id": 9648, "name": "Mystery"},
#         {"id": 10749, "name": "Romance"},
#         {"id": 878, "name": "Science Fiction"},
#         {"id": 10770, "name": "TV Movie"},
#         {"id": 53, "name": "Thriller"},
#         {"id": 10752, "name": "War"},
#         {"id": 37, "name": "Western"},
#     ]

#     pprint(movie_info(movie, genres_list))

# 오류 원인
# SyntaxError: Non-UTF-8 code starting with '\xeb' in file C:\Users\chu02\Desktop\TIL\practice\220718\ex_11.py 
# on line 51, but no encoding declared; see https://python.org/dev/peps/pep-0263/ for details
# 51번째줄 코드에 나온 한글로 인해 인코딩 문제가 발생
# 소스 문서를 utf-8로 변환해서 저장

# 수정 코드

# -- coding: utf-8 --
from pprint import pprint


def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }


if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))




