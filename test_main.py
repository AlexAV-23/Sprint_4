from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # проверяем, что добавилось именно две книги словарь books_genre
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем, что у добавленной книги нет жанра
    def test_add_new_book_added_new_book_without_genre_positive_result(self, collector):

        name_book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name_book)

        assert collector.books_genre[name_book] == ''

    # проверяем, что устанавливается жанр книги, 
    # если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_positive_result(self, collector):

        book_name = 'Гордость и предубеждение и зомби'
        this_book_genre = collector.genre[0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,this_book_genre)

        assert collector.books_genre.get(book_name) == this_book_genre

    # проверяем что get_book_genre выводит жанр книги по её имени.
    def test_get_book_genre_positive_result(self, collector):

        book_name = 'Гордость и предубеждение и зомби'
        this_book_genre = collector.genre[0]
        collector.books_genre[book_name] = this_book_genre

        assert collector.get_book_genre(book_name) == this_book_genre

    # проверяем, что get_books_with_specific_genre выводит список книг с определённым жанром
    def test_get_books_with_specific_genre_positive_result(self, collector):

        list_books_genre_1 = ['Инопланетянен', 'Чужой']
        genre_1 = collector.genre[0]
        list_books_genre_2 = ['Самогонщики', 'Операция Ы']
        genre_2 = collector.genre[-1]

        for book in list_books_genre_1:
            collector.books_genre[book] = genre_1
        
        for book in list_books_genre_2:
            collector.books_genre[book] = genre_2

        assert collector.get_books_with_specific_genre(genre_1) == list_books_genre_1
        assert collector.get_books_with_specific_genre(genre_2) == list_books_genre_2

    # проверяем, что get_books_genre выводит текущий словарь books_genre
    def test_get_books_genre_positive_result(self, collector_with_books_genre):

        expected_books_genre = {'Кот в сапогах': 'Мультфильмы', 'Афоня': 'Комедии', \
                                     'Оно': 'Ужасы', 'Двенадцать': 'Детективы', 'Книга без жанра': ''}
    
        assert collector_with_books_genre.get_books_genre() == expected_books_genre

    # проверяяем, что get_books_for_children — возвращает книги, 
    # у которых жанр не имеет возрастного рейтинга
    def test_get_books_for_children_positive_result(self, collector_with_books_genre):

        expected = ['Кот в сапогах', 'Афоня']

        assert sorted(collector_with_books_genre.get_books_for_children()) == sorted(expected)

    # проверяем, что add_book_in_favorites добавляет книгу в избранное
    # Книга должна находиться в словаре books_genre
    @pytest.mark.parametrize('book', ['Афоня', 'Двенадцать'])
    def test_add_book_in_favorites_positive_result(self, book, collector_with_books_genre):

        favorite_book = book

        collector_with_books_genre.add_book_in_favorites(favorite_book)

        assert favorite_book in collector_with_books_genre.favorites

    # проверяем, что delete_book_from_favorites удаляет книгу из избранного, если она там есть
    def test_delete_book_from_favorites_positive_result(self, collector_with_favorites):

        deleted_book = 'Остров'

        collector_with_favorites.delete_book_from_favorites(deleted_book)

        assert deleted_book not in collector_with_favorites.favorites

    # проверяем, что get_list_of_favorites_books — получает список избранных книг
    def test_get_list_of_favorites_books_positive_result(self, collector_with_favorites):

        assert collector_with_favorites.get_list_of_favorites_books() == ['Остров', 'Умка']