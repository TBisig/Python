class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12      
    
    def display_all(self):
        print self

    
    def __repr__(self):
        return "<Car price: {}, speed: {}, fuel: {}, mileage: {}, tax: {}>".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

if __name__ == "__main__":
    car1 = Car(price=2000, speed="35mph", fuel="full", mileage="15mpg", tax=())
    car2 = Car(price=5000, speed="40mph", fuel="empty", mileage="20mpg", tax=())
    car3 = Car(price=7000, speed="44mph", fuel="full", mileage="37mpg", tax=())
    car4 = Car(price=8000, speed="92mph", fuel="half full", mileage="42mpg", tax=())
    car5 = Car(price=10000, speed="100mph", fuel="drops of fuel", mileage="10mpg", tax=())
    car6 = Car(price=12000, speed="55mph", fuel="full", mileage="22mpg", tax=())

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()