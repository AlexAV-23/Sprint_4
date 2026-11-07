# Sprint_4

## Реализованные тесты:

***test_add_new_book_add_two_books:***  
тестирует метод add_new_book - добавление двух книг  

***test_add_new_book_added_new_book_without_genre_positive_result***  
тестирует метод add_new_book - проверяет, что у добавленной книги нет жанра

***test_set_book_genre_positive_result***  
тестирует метод set_book_genre - проверяет, что устанавливается жанр книги

***test_get_book_genre_positive_result***  
тестирует метод get_book_genre - проверяет что get_book_genre выводит жанр книги по её имени

***test_get_books_with_specific_genre_positive_result***  
тестирует метод get_books_with_specific_genre - проверяет, что get_books_with_specific_genre выводит список книг с определённым жанром

***test_get_books_genre_positive_result***  
тестирует метод get_books_genre - проверяет, что get_books_genre выводит текущий словарь books_genre

***test_get_books_for_children_positive_result***  
тестирует метод get_books_for_children - проверяяет что get_books_for_children возвращает книги, у которых жанр не имеет возрастного рейтинга

***test_add_book_in_favorites_positive_result***  
тестирует метод add_book_in_favorites - проверяет, что add_book_in_favorites добавляет книгу в избранное

***test_delete_book_from_favorites_positive_result***  
тестирует метод_delete_book_from_favorites - проверяет, что delete_book_from_favorites удаляет книгу из списка избранного favorites, если она там есть

***test_get_list_of_favorites_books_positive_result***  
тестирует метод create_list_of_favorites_books - проверяет, что get_list_of_favorites_books получает список избранных книг

## Используемые fixture:  

    # создает экземпляр (объект) класса BooksCollector 
    # перед каждым тестом
    @pytest.fixture
    def collector():
        return BooksCollector()

    # создает список избранного в экземпляре класса BooksCollector 
    @pytest.fixture
    def collector_with_favorites(collector):
        collector.favorites = ['Остров', 'Умка']
        return collector

    # создает словарь books_genre в экземпляре класса BooksCollector 
    @pytest.fixture
    def collector_with_books_genre(collector):
        collector.books_genre = {'Кот в сапогах': 'Мультфильмы', 'Афоня': 'Комедии', \
                                        'Оно': 'Ужасы', 'Двенадцать': 'Детективы', 'Книга без жанра': ''}
        return collector
