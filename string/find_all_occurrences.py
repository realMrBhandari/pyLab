s = "Hello! How are you?"
count = s.count("o")
print(f"in the string occurrence is {s.count("o")} no of times")
prevelence = []
index = 0
for x in range(count):
    index = s.find("o", index, len(s))
    prevelence.append(index)
    print(index)
    index += 1
    print(prevelence)

print(prevelence.sort())
