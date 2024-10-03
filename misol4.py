with open("misol4.txt", "w") as fayl:
    fayl.write(input("matn kiriting: "))

with open("misol4.txt", "r") as fayl:
    sozlar = fayl.read().split()
    if sozlar:
        print(f"eng uzun: {max(sozlar, key=len)}")
        print()
        print(f"eng qisqa : {min(sozlar, key=len)}")
