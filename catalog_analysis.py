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
    total = sum(f["rating"] for f in movies)
    return round(total / len(movies), 1)

# Функция описания возраста фильма
def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - f["year"] for f in movies]
    return (min(ages), max(ages), math.ceil(sum(ages) / len(ages)))

# Функция времени фильма
def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"

#print(f"Средний рейтинг каталога: {average_rating(movies)}")
#print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]}")

# Этап №2. Условия и match
# Функция описания рейтинга фильма
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating < 5:
        return "слабо"
    else:
        return "хорошо" if rating >= 7  else "средне"

# Функция описания года фильма
def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >=2015:
            return "недавние"
        case _:
            return "старые"

# Этап №3. Циклы
# Функция вывода не комедий
def is_comedy(movies):
    for f in movies:
        if "comedy"  in f["genres"]:
            continue  
        print(f'Не комедии {f["title"]}')

is_comedy(movies)

# Функция поиска шедевра
shedevr_count = 0
while shedevr_count < len(movies):
    if movies[shedevr_count]["rating"] > 9.0:
        print(f'Найден шедевр:  {movies[shedevr_count]["title"]}')
        break
    shedevr_count = shedevr_count +1
else:
    print("Шедевров не найдено")

# Функция количества фильмов длиннее 120 минут
def count_long_movies(movies, threshold = 120):
    movie_count = 0
    for f in movies:
        if f["duration_min"] > threshold:
            movie_count = movie_count + 1
    return movie_count