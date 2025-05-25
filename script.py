from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["moja_baza"]
kolekcja = db["uzytkownicy"]

#kolekcja.insert_one({"imie": "Adam", "wiek": 30})
#print(list(kolekcja.find()))
#print(kolekcja.find_one({"imie": "Adam"}))

#for doc in kolekcja.find({"imie": "Adam"}):
for doc in kolekcja.find({}):
    print(doc)
    print(100*'-')

print(kolekcja.count_documents({}))
print(kolekcja.count_documents({"imie": "Adam"}))
