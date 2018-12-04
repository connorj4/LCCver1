class vehicles:
    vehicles_list = ['Acura', 'Ford', 'Mercury', 'Bentley', 'Saab', 'Aston Martin', 'Jaguar', 'Kia', 'Geo', 'Mazda', 'Porsche', 'Maybach', 'Jeep', 'Toyota', 'Lotus', 'Maserati', 'Suzuki', 'Isuzu', 'Audi', 'Cadillac', 'Chevrolet', 'GMC', 'Saturn', 'Honda', 'Dodge', 'Lexus', 'BMW', 'Mitsubishi', 'Buick', 'Land Rover', 'Lamborghini', 'Volvo', 'Hyundai', 'Lincoln', 'Infiniti', 'Oldsmobile', 'Mercedes-Benz', 'Hummer', 'Volkswagen', 'Pontiac', 'Nissan', 'Chrysler', 'Subaru']

    def __init__(self):
        self = self
    def add_vehicle(self, name):
        if name in self.vehicles_list:
            print("This vehicles type already exist")
        else:
            self.vehicles_list.append(name)

    def remove_vehicle(self, name):
        if name in self.vehicles_list:
            self.vehicles_list.remove(name)

    def check_vehicle(self,items):
        print(items)
        id, name, description, price, plate, year = items
        if name in self.vehicles_list:
            if 1885 <= year <= 2019:
                if price >= 0.01:
                    if str(plate).isalnum() & str(plate).isupper():
                        print("Input Accepted")
                        return True
                    else:
                        raise SyntaxError("Vehicle plate number error")
                else:
                    raise SyntaxError("Vehicle price error")
            else:
                raise SyntaxError("Vehicle year error")
        else:
            raise SyntaxError("Vehicle name error")
