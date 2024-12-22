from files import CSV_FILE_PATH
from files import JSON_FILE_PATH

from itertools import islice
from csv import DictReader
import json


books_list = []
users_list = []

with open(CSV_FILE_PATH, newline="") as f:
    reader = DictReader(f)
    for row in reader:
        books_list.append(
            {
                "title": row.get("Title"),
                "author": row.get("Author"),
                "pages": row.get("Pages"),
                "genre": row.get("Genre"),
            }
        )


with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

k = len(books_list) // len(users)
for i_user in users:
    users_list.append(
        {
            "name": i_user.get("name"),
            "gender": i_user.get("gender"),
            "address": i_user.get("address"),
            "age": i_user.get("age"),
            "books": list(islice(books_list, k)),
        }
    )
    del books_list[0:k]


for i in range(len(books_list)):
    users_list[i]["books"].append(books_list[i])

with open("result.json", "w") as f:
    json.dump(users_list, f, indent=4)
