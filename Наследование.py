class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def decription(self):
        return f"{self.make} {self.model} {self.year}"


    def update_odometer(self,km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("НЕТ")

    def increment_odometer(self,km):
        self.odometer_reading += km

    def odometer_response(self):
        return f'Пробег нашего автомобиля: {self.odometer_reading}'


class Battery:

    def __init__(self,battery=100):
        self.battery = battery


    def battery_description(self):
        print(f"У вашего автомобиля {self.battery} заряда аккумулятора")


class ElectronicCar(Car):


    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    def decription(self):
        print(f"{self.model} {self.year}")

    def power(self,km):
        result = km // 10
        self.battery.battery -= result
        return self.battery.battery_description()

tesla = ElectronicCar("Tesla","X","2019")
tesla.battery.battery = 50
tesla.power(240)

