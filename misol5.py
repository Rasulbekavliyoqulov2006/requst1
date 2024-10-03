with open("misol5.txt", "w") as fayl:
    matn = input("matn kiriting: ")
    fayl.write(''.join(reversed(matn)))

with open("misol5.txt", "r") as fayl:
    matn = fayl.read()
print(matn)