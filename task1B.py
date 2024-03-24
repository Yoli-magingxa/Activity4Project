books = []
members = []

def add_book():


     books.append({
          "book_id ": 2024001,
          "title  ": "Python Programming",
           "author ": "Jacob Zuma",
           "status ": "Not available"
     })

def add_member():
     members.append({
          "member_id ": 1,
          "name ": "Anelisa Maleka",
          "borrowed_books": []

     })

     print("Book List :" , books)
     print("Members List: ", members)

add_book()
add_member()
 