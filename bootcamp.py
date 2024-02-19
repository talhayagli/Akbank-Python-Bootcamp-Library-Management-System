
class Library:

    def addLib():
        
        while True:

            bookName=input("\nName of the Book:")
            author=input("\nAuthor:")
            relDate=input("\nRelease Date:")
            nPage=input("\nNumber of Pages:")

                
            with open("books.txt","a+",encoding="utf-8") as file:
                file.write(bookName.upper()+ "," +author.upper()+ "," +relDate.upper()+ "," +nPage.upper()+"\n")
                print("\n"+bookName.upper()+" Added\n")  
           
            break

    def listLib():
        
        try:
            with open('books.txt','r',encoding="utf-8") as file:
                numLine=0
                for line in file:
                    numLine+=1
                    columns = line.strip().split(',')
        
                    bookNAMES = columns[0]
                    authorNAMES= columns[1]
                    relDATES= columns[2]
                    nPAGES= columns[3]

                    print(bookNAMES+" , "+authorNAMES)

                print("\nThere are "+str(numLine)+" books in the library.\n")   
        
        except:
            print("\nTHE TXT FILE YOU WANT TO READ IS NOT EXISTS\nPLEASE START WITH ADDING BOOKS FIRST!!\n")



    def removeLib():


                

        while True:

            delType=input("\n1-Delete by book name\n2-Delete all the library\n3-Quit to MENU:")

            if delType =="1":
                deletedName=input("\nName of the book:").upper()
                
                
                with open('books.txt','r',encoding="utf-8") as file:
                    bookList=[]
                    lines=file.readlines()
                    print(lines)
                    for line in lines:
        
                        parts = line.strip().split(",")  
                        
                        book_name = parts[0].strip()
                        
                        bookList.append(book_name)
                
                try:
                    index=bookList.index(deletedName)
                    with open("books.txt", 'w',encoding="utf-8") as file:
                        filtered_lines = [line for line in lines if lines[index] not in line]
                        file.writelines(filtered_lines)
                        print("\nTHE BOOK "+deletedName+" HAS BEEN DELETED.\n")

                            
                except ValueError:
                    print("\nBook does not  in the library.\n")

                               
    
            elif delType=="2":
                with open("books.txt", 'w') as file:
                    file.write("")
                    print("\nALL THE LIBRARY HAS BEEN DELETED\n.")
                break
            

            elif delType=="3" or delType=="q" or delType=="Q":


                break
            


while True:
    process=input("\n*** MENU***\n1-List Books\n2-Add Books\n3-Remove Books\n4-Quit: ")
    
    if process =="2":
        Library.addLib()
    elif process=="1":
        Library.listLib()
    elif process=="3":
        Library.removeLib()
        
    elif process =="q" or process =="Q":
        break
    else:
        print("\nWRONG INPUT, TRY AGAIN !!!\n")
        


