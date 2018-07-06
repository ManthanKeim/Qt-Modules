class library:
    def __init__(self):
        self.books = list()

    def __repr__(self):

        return str([self.books])


class book():
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price

    def __repr__(self):
        return str([self.name , self.author, self.price])

if __name__ == '__main__':
    lib = library()

b1 = book("a" , "b" , 1 )
b2 = book("ac" , "sb" , 132 )
b3 = book("afdg" , "bxcv" , 13124 )
b4 = book("aasdas" , "dsadxb" , 132546 )

lib.books = [b1, b2 , b3 , b4]

print(lib.books)
print(b1)

books = list(filter(lambda item : item.author=="sb" and item.price<133 , lib.books))
print(books)