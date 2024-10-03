ism = input("ismingizni kiriting: ")

with open(f"{ism}.txt", "w") as fayl:
    fayl.write(input("matn kiriting: "))

with open(f"{ism}.txt", "r") as fayl:
    matn = fayl.read()
    s = len(matn.split())  
    print(f"{ism}.txt da {s} ta soz bor ")
