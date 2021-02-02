
class Book:
    def __init__(self, author='', title=''):
        self.author = author
        self.title = title
    
    def display(self):
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    book_1 = Book('John Steinbeck', 'Of Mice and Men')
    book_2 = Book('Harper Lee', 'To Kill a Mockingbird')
    book_1.display()
    book_2.display()
