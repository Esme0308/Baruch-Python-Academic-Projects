#Cars
class Car:
    def __init__ (self,year_model,make):
        self.__year_model= year_model
        self.__make = make
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 5 
    def brake(self):
        self.__speed -= 5 
    def get_speed(self):
        return self.__speed 
 #Looking up a specific car        
def main():
    car=Car("2019","Nissan")
    car.accelerate()
    print("Speed=",car.get_speed())
    car.accelerate()
    print("Speed=",car.get_speed())
    car.accelerate()
    print("Speed=",car.get_speed())
    car.accelerate()
    print("Speed=",car.get_speed())
    car.accelerate()
    print("Speed=",car.get_speed())
    
    car.brake()
    print("Speed=",car.get_speed())
    car.brake()
    print("Speed=",car.get_speed())
    car.brake()
    print("Speed=",car.get_speed())
    car.brake()
    print("Speed=",car.get_speed())
    car.brake()
    print("Speed=",car.get_speed())
     
main()
