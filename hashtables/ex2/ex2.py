#  Hint:  You may not need all of these.  Remove the unused functions.
# fail 

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []

    maps = []

    for ticket in tickets:
        routes = {'source': ticket.source, 'destination': ticket.destination}
        maps.append(routes)

    print(maps)

    # route.append(maps["None"])

    # tic_length = len(tickets)

    # for i in range(0, tic_length):
    #     route.append(maps[route[i-1]])

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)

