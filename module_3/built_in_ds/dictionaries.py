empty_dict = {}  # Empty dictionary
print(empty_dict)


phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)

del phone_book["Batman"]
print(phone_book)


cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

lastAdded = phone_book.popitem()
print(lastAdded)

print(len(phone_book))

print("Batman" in phone_book)

second_phone_book = {"Batman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)



