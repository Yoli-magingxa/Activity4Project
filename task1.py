books = []
members = []

def add_book(book_id, title, author, status):


     books.append({
          "book_id ": book_id,
          "title  ": title,
           "author ": author,
           "status ": status
     })

def add_member(member_id, name):
     members.append({
          "member_id ": member_id,
          "name ": name,
          "borrowed_books": []

     })

     print("Book List :" , books)
     print("Members List: ", members)


 