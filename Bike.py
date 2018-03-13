class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def display_info(self):
        print self
    
    def ride(self):
        #miles on bike
        self.miles = self.miles+10
        return self

    def reverse(self):
        self.miles = self.miles-5
        return self

    def __repr__(self):
        return "<Bike! price: {}, max_speed: {}, miles travelled: {}>".format(self.price, self.max_speed, self.miles)

if __name__ == "__main__":
    bike1 = Bike(price=250, max_speed="50")
    bike2 = Bike(price=130, max_speed="25")
    bike3 = Bike(price=50, max_speed="10")
    bike1.ride().reverse().ride().display_info()
    bike2.display_info()
    bike3.display_info()
    