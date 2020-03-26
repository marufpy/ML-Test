from car import Car
class Battery:
    '''A simple attempt to model a battery for an electric car.'''
    def __init__(self,battery_size = 75):
        '''Initilize the battery's attributes'''
        self.battery_size = battery_size
    def decribe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.battery_size}-kWh batery.')
    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size==75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f'This car can go about {range} miles on full charge.')
        

class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''
    def __init__(self,make,model,year):
        '''Initialize attributes fo he parent class.
        Then initialize attributes specific to an electric car.'''
        super().__init__(make,model,year)
        self.battery = Battery()
#        self.battery_size = 75

#    def decribe_battery(self):
#        '''Print a statement describing the battery size.'''
#        print(f'This car has a {self.battery_size}-kWh battery.')

    def fill_gas_tank(self):
        '''Electric cars don't have gas tanks'''
        print("This car doesn't need a gas tank!.")