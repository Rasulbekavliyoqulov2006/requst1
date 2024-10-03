ism=input("ismingizni kiriting: ")
familiya=input("familiya kiriting: ")
yosh=input("yoshingizni kiriting: ")
with open("misol1.txt", "w") as f :
    f.write(f"ism: {ism}\nfamiliya:{familiya}\nyosh: {yosh}\n")