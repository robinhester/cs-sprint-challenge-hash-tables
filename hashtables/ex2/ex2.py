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
    print(len(maps))
    print(maps[1]['source'])

    maps_length = len(maps) - 1

    for i in range(0, maps_length):

        if maps[i]['source'] == 'NONE':
            route.insert(0, maps[i]['destination'])
        if len(route) == 1:
            if maps[i]['source'] == route[0]:
                route.append(maps[i]['destination'])
        if len(route) == 2:
            if maps[i]['source'] == route[1]:
                route.append(maps[i]['destination'])
        if len(route) >2:
            if maps[i]['source'] == route[i-1]:
                route.append(maps[i]['destination'])
        
        # if maps[i]['source'] == 'None':
        #     route.append(maps[i]['destination'])
        # if maps[i[['source'] == maps[i+1]['destination']:
        #     route.append(maps[i]['destination'])
        # if maps[i]['destination'] == 'None':
        #     route.append(maps[i]['source'])


    
    route.append('NONE')
    print(route)
    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

reconstruct_trip(tickets, 10)

