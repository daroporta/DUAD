class Bus:
    def __innit__(self, max_passengers, bus_list):
        self.max_passengers=max_passengers
        self.bus_list=[]


    def add_passengers(self, person):
        amount=0
        while True:
            if amount <= (self.max_passengers-1):
                person=input(f"Name of passenger number {amount+1}: ") 
                self.bus_list.append(person)
                amount += 1
            else:
                print("The bus has reached the maximum capacity.")
                break
        print(f"The passengers inside the bus are: {self.bus_list}")


    def remove_passengers(self):
        self.bus_list.pop(-1)
        print(self.bus_list)


my_bus= Bus()

my_bus.max_passengers

my_bus.add_passengers("Passengers")

my_bus.remove_passengers()



