from librarypkgclass import book as book
from librarypkgclass import graphicNovel as graphicNovel    
from librarypkgclass import comicBook as comicBook
from librarypkgclass import magazine as magazine
if __name__ == "__main__":
    booklist = {"graphicNovels" : {}, "comicBooks" : {}, "magazines" : {}}


    while True:
        choice = int(input("""
        Welcome to the CRUD management system for the library of Alexandria!.
        What would you like to do today? 
        
        1. Add book
        2. search book
        3. view all book
        4. Delete book
        
        Enter your choice: 
        """))

        if choice == 1:
            while True:
                bookAdd = int(input("""what is the book type? 
                    1. Graphic Novel
                    2. Comic book
                    3. Magazine
                    4. Continue
                    """))
                if bookAdd == 1:
                    placementGraphicNovel = graphicNovel()
                    placementGraphicNovel.createBook()
                    print(f"adding {placementGraphicNovel.title}, by {placementGraphicNovel.author}, with pages {placementGraphicNovel.pages}, where it is {placementGraphicNovel.colorQ} colored")
                    booklist["graphicNovels"][placementGraphicNovel.title] = {"obj" : placementGraphicNovel}    
                elif bookAdd == 2:
                    placementComicBook = comicBook()
                    print(f"adding {placementComicBook.title}, by {placementComicBook.author}, with pages {placementComicBook.pages}, where it is read from {placementComicBook.readingstyle}")
                    booklist["comicBooks"][placementComicBook.title] = {"obj" : placementComicBook}    
                elif bookAdd == 3:
                    placementMagazine = magazine()
                    placementMagazine.createBook()
                    print(f"adding {placementMagazine.title}, by {placementMagazine.author}, with pages {placementMagazine.pages}, it is about {placementMagazine.Topic}")
                    booklist["magazines"][placementMagazine.title] = {"obj" : placementMagazine}    
                elif bookAdd == 4:
                    backTrace = input("would you like to go back to menu? (Y/N) ")
                    if backTrace == "N":
                        continue
                    elif backTrace == "Y":
                        break
                    else:
                        print("Err")    
                else:
                    print("not an option, please retry")
                    continue
        elif choice == 2:
            # def searchAlgo()
            while True:
                    choice = int(input(""" 
                                    1. Search By title
                                    =======================
                                    2. Search by author
                                    
                                    what would you like to search by?
                                    """))
                    if choice == 1: 
                        categorySearch = int(input("""
                                        1. Graphic Novel
                                        2. comic Book
                                        3.  Magazine
                                                """))
                        if categorySearch == 1:
                            pass
                        elif categorySearch == 2:
                            pass
                        elif categorySearch == 3:
                            pass

                        titleSearch = input("what is the title? ")

                    elif choice == 2: 
                        authorSearch = input("what is the author's name? ")
        elif choice ==3 :
            print (booklist)
            for novels in booklist["graphicNovels"]:
                tempObj =booklist["graphicNovels"][novels]['obj'].author 
                print(tempObj)
            # print(f"Graphic novels:")
            # for i in range(len(booklist[0])-1) :
            #     print(f"{i+1}., {booklist[0][i].title}, {booklist[0][i].name}")
            # for l in range(len(booklist[1])-1):
            #     print("Comic Books:")
            #     print(f"{l+1}., {booklist[1][l].title}, {booklist[1][l].name}")
            # for n in range(len(booklist[2])-1):
            #     print("Magazine Books:")
            #     print(f"{n+1}., {booklist[2][n].title}, {booklist[2][n].name}")


                
                
                
                
                
                
                
                
    # workerDave = Baker('Dave', 8, "Bread").description()
    # class officeWorker

    # class 


