class Figury():

    def __init__(self, x, y, color):
        self.a = x
        self.b = y
        self.color = color

    def prostokat(self):
        print("Prostokąt")
        print("Pole jest równe:", self.a*self.b)
        print("Kolor figury: ", self.color)

    def trojkat(self):
        print("Trójkąt")
        print("Pole jest równe:", 1/2*self.a*self.b)
        print("Kolor figury: ", self.color)

    def trapez(self):
        print("Trapez")
        print("Pole jest równe: ", ((self.a+self.b)/2)*10)
        print("Kolor figury: ", self.color)

prostakat = Figury(4,6,"żółty")
trojkat = Figury(3,6,"zielony")
trapez = Figury(10,6,"różowy")

prostakat.prostokat()
trojkat.trojkat()
trapez.trapez()

