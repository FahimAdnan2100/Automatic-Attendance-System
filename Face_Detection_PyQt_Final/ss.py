import random

busSeats = [['A1', 'A2'], ['A3', 'A4'], ['B1', 'B2'], ['B3', 'B4'], ['C1', 'C2'], ['C3', 'C4'],
            ['D1', 'D2'], ['D3', 'D4'], ['E1', 'E2'], ['E3', 'E4'], ['F1', 'F2'], ['F3', 'F4']]

userInput = int(input("Please enter the numbers of input: "))

numOfPassenger = []
seatNumber = {}
itr = 0

while itr < userInput:
    in_one = input().split()
    if len(in_one) == 1:
        found = False
        for y in busSeats:
            if len(y) == 1:
                seatNumber[in_one[0]] = y[0]
                found = True
                y.remove(y[0])
                break

        if not found:
            update_value = random.choice(busSeats)[0]
            seatNumber[in_one[0]] = update_value
            for temp in busSeats:
                if update_value in temp:
                    temp.remove(update_value)

    else:
        seatAb = False
        for y in busSeats:
            if len(y) == 2:
                seatNumber[f"{in_one[0]}, {in_one[1]}"] = y
                seatAb = True
        if not seatAb:
            print("Seat is not available")
    itr += 1
print(seatNumber)

