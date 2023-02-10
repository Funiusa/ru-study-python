from typing import Union, Any, Dict


def movie_rating_filter(movie: Dict[Any, Any]) -> Union[Any, float]:
    return movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"])


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        country_filter = filter(lambda movie: movie["country"].count(","), list_of_movies)

        rating = list(
            map(
                lambda movie: float(movie["rating_kinopoisk"]),
                filter(movie_rating_filter, country_filter),
            )
        )

        average_rating = sum(rating) / len(rating)

        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        rating_filter = filter(movie_rating_filter, list_of_movies)
        greater_or_equal_rating = filter(
            lambda movie: float(movie["rating_kinopoisk"]) >= rating, rating_filter
        )
        letters_count = list(map(lambda movie: movie["name"].count("и"), greater_or_equal_rating))

        return sum(letters_count)
