class book():
    def __init__(self, title, author, pages):
        self.author = author
        self.pages = pages
        self.title = title
    def createBook(self):
        while True:
            try:
                name = input("what is the name of the author? ")
                pages = int(input("how many pages constitute this book? "))
                title = input("what is the title of this book? ")
                self.author = name
                self.pages = pages
                self.title = title
                break
            except ValueError:
                print("wrong data type, try again")
                continue
class graphicNovel(book):
    def __init__(self, author = "NA", title = "NA", pages = "NA", colorQ = "NA"):
        super().__init__(title, author, pages)
        self.colorQ = colorQ
    def createBook(self):
        super().createBook()
        while True:
            try:
                self.colorQ = input("is this graphic novel colored? ")
                break
            except ValueError:
                print("wrong data type, try again")
                continue
class comicBook(book):
    def __init__(self, author = "NA", title = "NA",pages = "NA", readingstyle = "NA"):
        super().__init__(title, author, pages)
        self.readingstyle = readingstyle
    def createBook(self):
        super().createBook(self)
        while True:
            try:
                style = int(input("(1) is it left to right ,or, (2) right to left"))
                if style == 1: self.readingstyle = "left to right"
                elif style == 2: self.readingstyle= "right to left"
                else: print("error, not an option")
                break
            except ValueError:
                print("error, maybe wrong datatype")
                continue
class magazine(book):
    def __init__(self, title = "NA", author = "NA", pages = "NA", Topic = "NA"):
        super().__init__(title, author, pages)
        self.Topic = Topic
    def createBook(self):
        super().createBook(self)
        while True:
            try:
                self.Topic = input("what is the category of this magazine")
                break
            except ValueError:
                print("error, input type is not a match")
                continue