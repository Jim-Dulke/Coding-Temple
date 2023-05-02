#parking garage class
class Garage():
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
#taketicket Method - decreases amount of tickets and parkingSpaces available by 1
    def takeTicket(self):
        for x in tickets, parkingSpaces:
            tickets.remove(x)
            parkingSpaces.remove(x)

#payforParking Method - display an input that waits for an amount from user and store in a variable
    def payForParking(self):
        fee = 10
        while fee > 0:
            message = int(input(f'Please insert ${fee}!'))
            fee -= message

        if fee <= 0:
            return 'Your ticket has been paid.  You have 15 minutes to leave.'
            currentTicket['paid']

#leaveGarage method - if paid, display Thank you, have a nice day! if not, display prompt for payment
#part 2: increase parkingSpaces by 1 and tickets list by 1
    def leaveGarage():
        if currentTicket['paid']:
            return 'Thank you, have a nice day!'
            for x in tickets, parkingSpaces:
                tickets.append(x)
                parkingSpaces.append(x)

        elif currentTicket['paid']: False
        while fee > 0:
            message = int(input(f'Please insert ${fee}!'))
            fee -= message

    
    '''
    tickets = [1,2,3,...500]
    parkingSpaces = [1,2,3...500]
    currentTicket = {'paid': False}



    '''