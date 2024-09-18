from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_added_one_book_with_genre_get_one_book_with_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер','Ужасы')
        assert collector.get_book_genre('Гарри Поттер') == 'Ужасы'

    def test_get_book_genre_zero_books_empty_list(self, collector):
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    def test_get_book_genre_one_book_with_genre_get_genre_of_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер','Ужасы')
        assert collector.get_book_genre('Гарри Поттер') is 'Ужасы'

    def test_get_books_with_specific_genre_zero_books_empty_list(self, collector):
        assert collector.get_books_with_specific_genre('Гордость и предубеждение и зомби') == []

    def test_get_books_genre_added_one_book_book_received(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert collector.get_books_genre() == {'Гарри Поттер':''}

    def test_get_books_for_children_added_one_book_with_genre_get_one_book_with_genre_for_children(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер','Ужасы')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_added_one_book_with_genre_get_one_book_in_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_one_book_get_empty_list(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_empty_list_get_empty_list(self, collector):
        assert collector.get_list_of_favorites_books() == []
