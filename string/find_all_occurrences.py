# ? This programme let's you find all the occurrences of a sub-string in a string utilizing string methods, conditional statements and conrol flow statements
s = "Hello! How are you?"
count = s.count("o")
prevelence = []
index = 0
if count > 0:
    for x in range(count):
        index = s.find("o", index, len(s))
        prevelence.append(index)
        index += 1
    print(f"Total {count} Occurrences in the indexes {prevelence}")
else:
    print("not found")
