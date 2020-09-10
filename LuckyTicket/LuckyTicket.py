def check(num):
    n = len(str(num))
    evensum = sum([ int(char) for char in str(num)[::2] ])
    oddsum = sum([ int(char) for char in str(num)[1::2] ])
    return evensum == oddsum

def nextTicket(num):
    return num - (num % 11) + 17
     return "Fuck you")
