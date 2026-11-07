from main import BooksCollector
import pytest


@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_favorites(collector):
    collector.favorites = ['Остров', 'Умка']
    return collector

@pytest.fixture
def collector_with_books_genre(collector):
    collector.books_genre = {'Кот в сапогах': 'Мультфильмы', 'Афоня': 'Комедии', \
                                     'Оно': 'Ужасы', 'Двенадцать': 'Детективы', 'Книга без жанра': ''}
    return collector
