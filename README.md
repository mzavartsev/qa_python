# qa_python

test_set_book_genre_added_one_book_with_genre_get_one_book_with_genre
Добавляю одну книгу с жанром, проверяю,что получаю одну книгу с жанром

test_get_book_genre_zero_books_empty_list
Ничего не добавляю, проверяю, что список пустой

test_get_book_genre_one_book_with_genre_get_genre_of_book
Добавляю одну книгу с жанром, проверяю жанр книги

test_get_books_with_specific_genre_zero_books_empty_list
Ничего не добавляю, проверяю, что список пустой

test_get_books_genre_added_one_book_book_received
Добавляю одну книгу, проверяю словарь

test_get_books_for_children_added_one_book_with_genre_get_empty_list
Добавляю одну книгу с жанром, проверяю, что книга не попала в список, тк не подошла по жанру

test_get_books_for_children_added_one_book_with_genre_get_one_book_with_genre_for_children
Добавляю одну книгу с жанром, проверяю, что книга попала в список для детей

test_delete_book_from_favorites_one_book_get_empty_list
Добавляю одну книгу с жанром,удаляю, проверяю, что список пустой

test_get_list_of_favorites_books_empty_list_get_empty_list
Ничего не добавляю, проверяю,что возвращается пустой список

test_add_new_book_add_4_books_check_that_2_are_on_the_dictionary
Параметризированный тест. Добавляю 4 книги, проверяю, что 2 из них попали в словарь

test_add_new_book_add_3_books_get_dictionary_with_3_books
Параметризированный тест. Добавляю 3 книги, проверяю, что 3 из них попали в словарь