'''
Создайте класс «Книга», который имеет атрибуты название, автор и количество
страниц. Добавьте методы для чтения и записи книги
'''
'''
Создайте класс «Книга», который имеет атрибуты название, автор и количество
страниц. Добавьте методы для чтения и записи книги
'''
class Book:
    name = None
    author = None
    pages = None

    def initial(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        self.current_page = 0
    
    def read(self, pages_to_read = 1):
        if self.pages is None or self.pages <= 0:
            return "Количество страниц не указано или недействительно."

        new_page = self.current_page + pages_to_read

        if new_page > self.pages:
            self.current_page = self.pages
        else:
            self.current_page = new_page

        if self.current_page >= self.pages:
            return f"Вы закончили читать '{self.name}' от {self.author}."
        else:
            return f"Вы читаете '{self.name}' от {self.author}. Текущая страница: {self.current_page} из {self.pages}."
        
    def write(self, name, author, pages):
        if name is not None:
            self.name = name
        if author is not None:
            self.author = author
        if pages is not None:
            self.pages = pages
        self.current_page = 0

    def get_info(self):
         return f"Название книги {self.name}, автор {self.author}, количество страниц {self.pages}, прочитанных страниц {self.current_page}"


book1 = Book()
book1.initial("1984", "Джордж Оруэлл", 328)

print(book1.read(50))  
print(book1.read(300)) 

book1.write("Преступление и наказание", "Фёдор Достоевский", 671)
print(book1.get_info())
print(book1.read(100)) 