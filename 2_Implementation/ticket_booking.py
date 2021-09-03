"""" Ticket Booking System Source Code """
import random
import re


class Travel:
    """ Travel class contains init and travel_fare methods"""
    def __init__(self, source, destination, distance, time, privilege):
        self.source = source
        self.destination = destination
        self.distance = distance
        self.time = time
        self.privilege = privilege
        self.cost = 0


    def travel_fare(self):
        """ Travel fares method """
        if self.privilege == "FIRST CLASS":
            self.cost = self.distance * 150
        elif self.privilege == "ECONOMY":
            self.cost = self.distance * 20
        return self.cost


#t1 = travel("New York", "Beijing", 8000, 10, "ECONOMY")
#t2 = travel("London", "New York", 6000, 6, "FIRST CLASS")
#t3 = travel("Bengaluru", "Abu Dhabi", 3000, 3, "BUSINESS CLASS")
class PNR:
    """ PNR class is used to check the PNR status of a passenger """
    def __init__(self, pnr_no, ticket):
        self.pnr_no = pnr_no
        self.ticket = ticket
    def __str__(self):
        return f"PNR NO --> [{self.pnr_no}] Travelling From {self.ticket.source} To {self.ticket.destination} {(self.ticket.time,self.ticket.distance)}"

#p1 = PNR("24613", t1)
#print(p1)


destinations = {"New York":1, "London":2, "Beijing":3, "Tokyo":4, "Bengaluru":5, "Abu Dhabi":6}
distance_time = {12:(5600, 5), 13:(11000,14), 14:(10900, 14), 15:(13360, 17), 16:(11040, 14),
                 21:(5600, 5), 23:(8200,10), 24:(8200,11), 25:(9570,9), 26:(5500,7),
                 31:(10980, 13), 32:(8200,10), 34:(2100, 3), 35:(5575, 10), 36:(6000, 9),
                 41:(10850, 13), 42:(6000,13), 43:(6700,11), 45:(8500,11), 46:(8200,13),
                 51:(13400,12), 52:(8000,11), 53:(7650,10), 54:(8500,11), 56:(2750,4),
                 61:(11040,15), 62:(5520, 8), 63:(6000, 7), 64:(8100, 9), 65:(2750,4)}

#Please update the distance and time data for calculations purposes.

all_pnr = []

def booking():
    """To book Ticket"""


    src = input("FROM: ")
    dest = input("TO: ")
    try:
        dist = distance_time[int(str(destinations[src]) + str(destinations[dest]))][0]
        t_i = distance_time[int(str(destinations[src]) + str(destinations[dest]))][1]
        pri = input("FIRST CLASS OR ECONOMY: ")
        t_1 = Travel(src, dest, dist, t_i, pri)
        p_1 = PNR(random.randrange(1, 1000000), t_1)
        print(f"Booking Confirmed with Total Amount {p_1.ticket.travel_fare()}")
        print("Press YES OR NO To Confirm")
        if input("") == "YES":
            print(f"TICKET CONFIRMED for {p_1}")
            #all_details.append(p1)   #Ticket will be saved in a global list.
            with open('bookingdetails.txt', 'a') as b_1:
                b_1.write(f"{p_1}")
                b_1.write("\n")
        else:
            print(f"BOOKING CANCELLED")
    except:
        print("Incorrect details entered")

def check_pnr(val):  # Only this function to be done.
    """To check the details of the booked Ticket"""
    all_details = []

    with open('bookingdetails.txt', 'r') as f_1:
        all_tickets = f_1.readlines()
        all_details = all_tickets
        for ticket in all_tickets:
            pnr = re.findall(r'[0-9]+', ticket)
            for num in pnr:
                all_pnr.append(num)
    if val in all_pnr:

        for p_1 in all_details:
            print("TICKET FOUND")
            for source in re.findall(r'm [a-zA-Z ]+ T', p_1):
                src = source[2:-2]
            for destination in re.findall(r'To [a-zA-Z]+', p_1):
                dest = destination[3:]
            for time in re.findall(r'([0-9]+,)', p_1):
                t_i = time[:-1]
            for distance in re.findall(r'(,[0-9]+)', p_1):
                dist = distance[1:]
            print(f"{src} >>>>>>> {dest}  |\n\n| DISTANCE {dist} KMS|\n\n| TIME: {t_i} HRS")
            break

    else:
        print("INCORRECT PNR NO OR TICKET NOT CONFIRMED")


if __name__ == "__main__":
    while True:
        print("1.TICKET BOOKING")
        print("2.CHECK PNR STATUS AND ANY KEY TO EXIT")
        n = int(input("ENTER OPTION: "))
        if n == 1:
            booking()
        elif n == 2:
            check_pnr(input("ENTER PNR NO "))
        else:
            break
