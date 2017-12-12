while True:
  x = input("Imię: ")
  y = input("Hasło: ")
  z = 2130
  if x == "Arnold" and y == "icra2013":
      print ("Saldo: ", z)
      break
  else:
      print("Błędne dane")
  break


print("Jaką czynność chcesz wykonać?\nA - wpłata\nB - wypłata")
czynnosc = input("Czynność: ")
if czynnosc == "A":
    wplata = int(input("Podaj kwotę: "))
    print("Twoje saldo wynosi teraz: ", z)
elif czynnosc == "B":
    wyplata = int(input("Podaj kwotę: "))
    if wyplata < z :
     z -= wyplata
     print("Twoje saldo wynosi teraz: ", z)
    else:
     print("Idź do pracy!")
else:
    print("Błędne dane")





















