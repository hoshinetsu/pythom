def bibljotekav1(wys, pien):
    for x in range(0, wys):
        print((wys - x) * " " + ' *' * x)
    while pien > 0:
        print(int(wys / 1.3) * " ", "| | |")
        pien -= 1
    print("BiblJoteka życzy Wesołych!")


def bibljotekav2(wys, pien):
    for x in range(1, wys):
        print((wys - x) * " " + ' *' * x)
    while pien > 0:
        print((wys - 3) * " " + " | | |")
        pien -= 1
    print("BiblJoteka życzy Wesołych!")


intin = lambda txt: int(input(txt))
wys = intin("Podaj wysokość choinki: ")
pien = intin("Podaj wysokość pnia: ")
bibljotekav2(wys, pien)
# while True:
# try:
#     x = int(input("Wybierz wersję programu [1,2]: "))
#     if x == 1:
#         bibljotekav1(10, 3)
#         break
#     else:
#         bibljotekav2(25, 3)
#         break
# except Exception:
#     print("No chyba to nie liczba! Try again.")
