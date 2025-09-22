
macska = {
    "név": "Ede",
    "kor": 3
}

print("macska neve és kora:")
print(macska)

valasztas = input("Melyik adatot szeretnéd atirni?(név vagy kor): ")

if valasztas == "név":
    ujnev = input("Add meg az új nevet: ")
    macska["név"] = ujnev

elif valasztas == "kor":
        ujkor = int(input("Add meg az új kort: "))
        macska["kor"] = ujkor

else:
    print(" nincs módosítás.")

print(macska)

