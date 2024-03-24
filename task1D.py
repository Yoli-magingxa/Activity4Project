import pandas as pd

books = {
     'book_id': [2024001],
     'tittle' : ["Python Programming"],
     'author' : ["Jacob Zuma"],
     'status' :["Not available"]   
}
member = {
    'member_id':[1],
    'name' :["Anelisa Maleka"]
}

book_data = pd.DataFrame(books)
member_data = pd.DataFrame(member)

print("Books DataFrame: ", book_data)
print("Member DataFrame: ", member_data)