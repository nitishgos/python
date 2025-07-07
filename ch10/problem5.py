class Train:
    def __init__(self,name,seat,fare):
        self.name=name
        self.seat=seat
        self.fare=fare
    def book_ticket(self):
        if (self.seat>0):
            print(f"Ticket booked successfully in {self.name}")
            self.seat-=1
        else:
            print(f"No seats available in {self.name}")
    def get_status(self):
        print(f"Number of seat available is {self.seat}")
    def get_fare_info(self):
        print(f"The fare of the train '{self.name}' is: Rs. {self.fare}")
train1=Train("Rajdhani Express",255,4000)
train1.get_status()
train1.get_fare_info()
train1.book_ticket()
train1.book_ticket()
train1.get_status()