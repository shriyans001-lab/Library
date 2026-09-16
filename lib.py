import json
try:
    with open('books.json','r') as f:
        books=json.load(f)
except FileNotFoundError:
    books={}
except json.JSONDecodeError:
    books={}
def add_books():
    book_id=input("Enter the book id: ")
    title=input("Enter the title: ")
    author=input('Enter the author name: ')
    year=int(input("Enter the year: "))
    if book_id in books:
        print("Book already exists")
    else:
        books[book_id]={
            'title':title,
            'author':author,
            'year':year
        }
        print("Book added successfully")
    with open('books.json','w') as f:
        json.dump(books,f)
def view_books():
    if books:
        for name,data in books.items():
            t=data['title']
            a=data['author']
            y=data['year']
            print(f'{name} | {t} | {a} | {y}')
    else:
        print("Library is empty")
def search_books():
    n=input("Enter the title to search: ")
    found=False
    for name,data in books.items():
        t=data['title']
        a=data['author']
        y=data['year']
        if t==n:
            print(f'{name} | {t} | {a} | {y}')
            found=True
    if not found:
        print("No books are found with this title")
def remove_book():
    m=input('Enter the book id to be removed: ')
    if m in books:
        del books[m]
        print("Book removed successfully")
    else:
        print("Books does not exist")
    with open('books.json','w') as f:
        json.dump(books,f)
while True:
    print('''===== Book Library =====

1. Add Book
2. View Books
3. Search Book
4. Remove Book
5. Exit''')
    n=int(input('Enter your choice: '))
    if n==1:
        add_books()
    elif n==2:
        view_books()
    elif n==3:
        search_books()
    elif n==4:
        remove_book()
    elif n==5:
        print("Good Bye!")
        break
    else:
        print("Invalid Menu Choice")