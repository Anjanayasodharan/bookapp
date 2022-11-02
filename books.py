import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'librarydb')
mycursor = mydb.cursor()
while True:

    print("select an option from the menu")

    print("1 add book")

    print("2 view all book")  
    print("3 search a book")
    print("4 update the book")    
    print("5 delete a book")
    print("6 exit")
    choice = int(input('enter an option:'))
    if(choice==1):
        print('book enter selected') 
        author=input('enter the book author')
        title=input('enter the book title')
        category=input('enter the category of book')
        charge=input('enter the charge per day')
        sql='INSERT INTO `books`( `author`, `title`, `category`, `charge`) VALUES (%s,%s,%s,%s)'
        data=(author,title,category,charge)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        sql = 'SELECT * FROM `books`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search book')
        title = input('enter the title')
        sql = "SELECT * FROM `books` WHERE `title` = '"+title+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update all book')
    elif(choice==5):
        print('delete book')
        title = input('enter the title')
        sql = "DELETE FROM `books` WHERE `title` = '"+title+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted succesfully")
    elif(choice==6):
        break