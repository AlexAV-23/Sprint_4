from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def create_instance_books_collector(self):
        # создаем экземпляр (объект) класса BooksCollector перед каждым тестом
        self.collector = BooksCollector()

    @pytest.fixture
    def create_list_of_favorites_books(self, create_instance_books_collector):
        self.collector.favorites = ['Остров', 'Умка']

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # добавляем две книги
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две в
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(self.collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем, что у добавленной книги нет жанра
    def test_add_new_book_added_new_book_without_genre_positive_result(self):

        name_book = 'Гордость и предубеждение и зомби'
        self.collector.add_new_book(name_book)

        assert self.collector.books_genre[name_book] == ''

    # проверяем, что устанавливается жанр книги, 
    # если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_positive_result(self):

        book_name = 'Гордость и предубеждение и зомби'
        this_book_genre = self.collector.genre[0]
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name,this_book_genre)

        assert self.collector.books_genre.get(book_name) == this_book_genre

    # проверяем что get_book_genre выводит жанр книги по её имени.
    def test_get_book_genre_positive_result(self):

        book_name = 'Гордость и предубеждение и зомби'
        this_book_genre = self.collector.genre[0]
        self.collector.books_genre[book_name] = this_book_genre

        assert self.collector.get_book_genre(book_name) == this_book_genre

    # проверяем, что get_books_with_specific_genre выводит список книг с определённым жанром
    def test_get_books_with_specific_genre_positive_result(self):

        list_books_genre_1 = ['Инопланетянен', 'Чужой']
        genre_1 = self.collector.genre[0]
        list_books_genre_2 = ['Самогонщики', 'Операция Ы']
        genre_2 = self.collector.genre[-1]

        for book in list_books_genre_1:
            self.collector.books_genre[book] = genre_1
        
        for book in list_books_genre_2:
            self.collector.books_genre[book] = genre_2

        assert self.collector.get_books_with_specific_genre(genre_1) == list_books_genre_1
        assert self.collector.get_books_with_specific_genre(genre_2) == list_books_genre_2

    # проверяем, что get_books_genre выводит текущий словарь books_genre
    def test_get_books_genre_positive_result(self):

        test_books_genre = {}
        for i in range(len(self.collector.genre)):
            test_books_genre['book' + str(i)] = self.collector.genre[i]

        self.collector.books_genre = test_books_genre

        assert self.collector.get_books_genre() == test_books_genre

    # проверяяем, что get_books_for_children — возвращает книги, 
    # у которых жанр не имеет возрастного рейтинга
    def test_get_books_for_children_positive_result(self):

        self.collector.books_genre = {'Кот в сапогах': 'Мультфильмы', 'Афоня': 'Комедии', \
                                     'Оно': 'Ужасы', 'Двенадцать': 'Детективы', 'Книга без жанра': ''}
        expected = ['Кот в сапогах', 'Афоня']

        assert sorted(self.collector.get_books_for_children()) == sorted(expected)

    # проверяем, что add_book_in_favorites — добавляет книгу в избранное
    # Книга должна находиться в словаре books_genre
    @pytest.mark.parametrize('book', ['Остров', 'Арктика'])
    def test_add_book_in_favorites_positive_result(self, book):

        favorite_book = book
        self.collector.books_genre = {'Остров': '', 'Арктика':''}

        self.collector.add_book_in_favorites(favorite_book)

        assert favorite_book in self.collector.favorites

    # проверяем, что delete_book_from_favorites удаляет книгу из избранного, если она там есть
    def test_delete_book_from_favorites_positive_result(self, create_list_of_favorites_books):

        deleted_book = 'Остров'

        self.collector.delete_book_from_favorites(deleted_book)

        assert deleted_book not in self.collector.favorites

    # проверяем, что get_list_of_favorites_books — получает список избранных книг
    def test_get_list_of_favorites_books_positive_result(self, create_list_of_favorites_books):

        assert self.collector.get_list_of_favorites_books() == ['Остров', 'Умка']