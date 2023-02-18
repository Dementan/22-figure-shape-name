#write a function that determines the shape of the figure by the number of sides passed as an argument [3,10].

n = int(input("Enter by the number of sides of the figure: "))


def FigureType(n):
    if n == 3:
        print("Triangle")
    elif n == 4:
        print("Quadrilateral")
    elif n == 5:
        print("Pentagonal")
    elif n == 6:
        print("Hexagon")
    elif n == 7:
        print("Heptagon")
    elif n == 8:
        print("Octagon")
    elif n == 9:
        print("Nonagon")
    elif n == 10:
        print("Decagon")
    else:
        print("Error. Need number [3, 10]")


print(FigureType(n))    #example

