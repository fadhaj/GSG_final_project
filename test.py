

import datetime
from turtle import st


class Client:
    class_id = 0
    clients_list = []
    client_idnumbers = []
    def __init__(self,fname,age,id_no,phone_no) -> None:
        self.id = Client.class_id + 1 
        self.fname = fname
        self.age = age
        self.id_no= id_no
        self.phone_no = phone_no
        Client.clients_list.append([f"id :{self.id} - name : {self.fname} - age : {self.age} - id number :{self.id_no} - phone :{self.phone_no}  "])
        Client.class_id+=1
        Client.client_idnumbers.append(f'{self.id_no}')
        

class Librarian():
    lib_id = 0
    lib_list = []
    def __init__(self,fname,age,id_no,emp_type) -> None:
        self.id = Librarian.lib_id + 1
        self.fname = fname
        self.age = age
        self.id_no = id_no
        self.emp_type = emp_type
        Librarian.lib_list.append(f"id :{self.id} - name : {self.fname} - age : {self.age} - id number :{self.id_no} - Employment type :{self.emp_type}  ")
        Librarian.lib_id+=1



class Book:
    book_list = []
    book_id = 0
    Active_books = []
    def __init__(self,title,description,author,status) -> None:
        self.id = Book.book_id + 1
        self.title = title
        self.description= description
        self.author = author
        self.status = status
        Book.book_list.append([f"id:{self.id} - title :{self.title} "])
        Book.book_id += 1
        if self.status in ['active','a','A','Active'] :
            Book.Active_books.append(f'{self.title}')


    

            

class BorrowOrder:
    book_no = 1
    order_id = 0
    orders_ids_list = []
    orders_dict = {}
    BO_Active_books = Book.Active_books
    Borrowed_books = []
    
    def __init__(self) -> None:

        client_request = input('Do u want to borrow a book from librarian or return book to librarian Y for borrow R for return  :  ')
        if client_request in ['Yes','Y']:
            book_name = input('What book u want to borrow  :  ')
            if book_name in BorrowOrder.BO_Active_books:
                our_client_id = input('What is ur id_no  :  ')
                if our_client_id in Client.client_idnumbers :

			
                    
                    self.id = BorrowOrder.order_id + 1
                    self.date = datetime.datetime.now()
                    self.client_id= our_client_id
                    BorrowOrder.order_id += 1
                    BorrowOrder.orders_ids_list.append(f'{self.id}')
                    BorrowOrder.orders_dict[f"{self.id}" ]=  book_name
                    BorrowOrder.orders_dict[f"date time id {self.id}" ] =  self.date
                    BorrowOrder.BO_Active_books.remove(book_name)
                    BorrowOrder.Borrowed_books.append(book_name)
                else :
                    print('This ID is not in the Database')



        if client_request in ['R','return']:
            returned_book_id = input('what is borrowing id for your book ')
            if returned_book_id in BorrowOrder.orders_ids_list:
                BorrowOrder.orders_ids_list.remove(f'{returned_book_id}')
                returned_book_name = BorrowOrder.orders_dict[returned_book_id]
                BorrowOrder.BO_Active_books.append(returned_book_name)
                BorrowOrder.Borrowed_books.append(returned_book_name)




        



class Main:
    List_of_books = ['C','P', 'J']
    id  = 1
    def __init__(self) -> None:
        self.listofclients = Client.clients_list
        self.listoflibraries = Librarian.lib_list
        self.listofbooks = Book.book_list
        self.listofbo_orders = BorrowOrder.orders_dict
        self.listofbo_books = BorrowOrder.Borrowed_books
        self.listofav_books = BorrowOrder.BO_Active_books
        print('list of clients  :' )
        print(Client.clients_list)
        print('#' * 80)
        print('list of Libraries  :' )
        print(Librarian.lib_list)
        print('#' * 80)
        print('list of Books  :' )
        print(Book.Active_books)
        print('#' * 80)
        print('list of orders :' )
        print(BorrowOrder.orders_dict)
        print('#' * 80)
        print('list of borrowed books  :' )
        print(BorrowOrder.Borrowed_books)
        print('#' * 80)
        print('list of active books :' )
        print(BorrowOrder.BO_Active_books)
        print('#' * 80)
        if Main.id == 1 :
            print(f'THIS IS Main NO {Main.id}')
        print('#' * 80)
        if Main.id > 1 :
            print(f'THIS IS Main NO {Main.id} after your last update' )
        Main.id+=1



client1 = Client('Yazan A. H. AbuOun','24','403','25891212')
librarian1 = Librarian('Fadel','28','40856494','Librarian')
book1= Book('C','low level lang','Fadel hajjaj','A')
book2= Book('P','high level lang','moda','A')
book3= Book('J','Med level lang','Ahmed','A')

state = True
counter = 1
while state:
    mainbefore = Main()
    borrw1 = BorrowOrder()
    mainafter = Main()    
    state = False



