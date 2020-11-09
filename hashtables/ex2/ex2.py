#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = [None] * length
    cache = {}
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    result[0] = cache["NONE"]
    for index in range(1, length):
        result[index] = cache[result[index-1]]

    return result

   
