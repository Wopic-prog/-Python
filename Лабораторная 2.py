class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает следующий идентификатор для новой книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        """
        Возвращает индекс книги по её идентификатору.

        :param book_id: Идентификатор книги.
        :raises ValueError: Если книги с таким id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
