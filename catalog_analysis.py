"""
Проект: Аналитика каталога стримингового сервиса.
Выполнил: Кузнецов Кирилл
"""

import math

# Приведём к стандарту PEP 8
movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"]
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"]
    }
]

# Этап №1. Разминка: переменные, числа, math
# Функция описания среднего рейтинга
def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


# Функция описания возраста фильма
def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


# Функция времени фильма
def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


# Этап №2. Условия и match
# Функция описания рейтинга фильма
def rating_tier(rating):
    if rating >= 9.0:
        return "шедевр"
    elif rating < 5.0:
        return "слабо"
    else:
        return "хорошо" if rating >= 7.0  else "средне"


# Функция описания года фильма
def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап №3. Циклы
# Функция вывода не комедий
def is_comedy(movies):
    print("Не относится к жанру комедия:")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(f"  - {movie['title']}")
is_comedy(movies)


# Функция поиска шедевра
def shedevr(movies):
    shedevr_count = 0
    while shedevr_count < len(movies):
        if movies[shedevr_count]["rating"] > 9.0:
            print(f'Найден шедевр:  {movies[shedevr_count]["title"]}')
            break
        shedevr_count = shedevr_count + 1
    else:
        print("Шедевров не найдено")


# Функция количества фильмов длиннее 120 минут
def count_long_movies(movies, threshold = 120):
    movie_count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            movie_count = movie_count + 1
    return movie_count


# Этап №4. Строки
# Функция строки к формату Title Case
def normalize_title(title):
    words = title.split()
    result =[]
    for word in words:
        if word:
            new_word = word[0].upper() + word[1:]
            result.append(new_word)
    return " ".join(result)


# Функция нормализованного названия в «слаг» виде
def make_slug(title):
    return title.lower().replace(" ", "-")


# Функция возвращающая единую строку с описанием фильма
def format_report_line(movie):
    title = normalize_title(movie["title"])
    time = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return(
        f'"{title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {time}, жанры: {genres}'
    )


# Этап №5. Списки
# Функция возвращающую список названий фильмов, по убыванию рейтинга
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies, key=lambda movie: movie["rating"], reverse=True
    )
    return [movie["title"] for movie in sorted_movies]


# Функция возвращающую список  из кортежей по рейтингу
def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies, key=lambda movie: movie["rating"], reverse=True
    )
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# Этап №6. Словари
# Функция возвращающая словарь количества жанров
def count_by_genre(movies):
    genre_count = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count


# Функция возвращающая словарь актёров
def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


# Функция фильмов с рейтингом выше среднего 
def high_rating(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


# Этап №7. Множества
# Функция, возвращающую множество всех уникальных жанров
def all_genres(movies):
    genres_set = set()
    for movie in movies:
        genres_set.update(movie["genres"])
    return genres_set


# Функция , возвращающую множество актёров, снимавшихся в обоих фильмах
def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


# Функцию которая возвращает жанры
def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


# Этап №8. Итераторы и генераторы
# Функция генератор
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie
total_duration = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7.0)


# Этап №9. Итоговый отчёт
def build_report(movies):
    print()
    print("Отчёт по каталогу")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет\n")    
    print("Топ-3 фильма:")
    top3 = top_n_by_rating(movies, n=3)
    for title, rating in top3:
        movie = next(movie for movie in movies if movie["title"] == title)
        print(f"  {format_report_line(movie)}")
    print()
    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre in sorted(genre_counts, key=genre_counts.get, reverse=True):
        print(f"  {genre} — {genre_counts[genre]}")
    print()  
    genres_str = ", ".join(sorted(all_genres(movies)))
    print(f"Все жанры каталога: {genres_str}")
if __name__ == "__main__":
    build_report(movies)