from car import Car
from electric_car import Car, ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())