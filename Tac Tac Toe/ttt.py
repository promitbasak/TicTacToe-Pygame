import random
import time

CELLS = 9
PLAYERS = 2
CORNERS = [1, 3, 7, 9]
NON_CORNERS = [2, 4, 6, 8]
board = {}
for i in range(9):
    board[i + 1] = 0
signs = {0: " ", 1: "X", 2: "O"}
winner = None


def rpermutation(a):
    array = a[:]
    for _ in range(len(array)):
        yield array.pop(random.randint(0, len(array)-1))


class player:
    def __init__(self, name, mark):
        self.name = name
        self.sign = "X" if mark == 1 else "O"
        self.mark = mark
        self.playings = []
        self.antimark = mark % 2 + 1

    def getturn(self):
        showboard()
        print(f"\n{self.name}'s Turn:")
        time.sleep(1)
        print(f"\n{self.name} is giving his turn", end="")
        for _ in range(6):
            print(".", end="")
            time.sleep(0.1)
        print()


class user(player):
    def getturn(self):
        showboard()
        print(f"\n{self.name}'s Turn:")
        while True:
            turnprompt = f"Enter where do you want to put {self.sign}\nEnter corresponding cell number [1-9]:  "
            turn = getintinput(turnprompt, 1, 9)
            if board[turn] == 0:
                break
            elif board[turn] == self.mark:
                print("You have already used that cell, please choose another!!!")
            else:
                print("Opponent has already used that cell, please choose another!!!")
        return turn


class easy(player):
    def getturn(self):
        super().getturn()
        while True:
            turn = random.choice(getemptycells())
            return turn


class medium(player):
    def getturn(self):
        super().getturn()
        for i in range(3):
            row = [board[i * 3 + 1], board[i * 3 + 2], board[i * 3 + 3]]
            if sum(row) == 2 * self.mark and (self.mark in row):
                try:
                    # print("1row")
                    return cellvalidator(i * 3 + row.index(0) + 1)
                except:
                    pass
            col = [board[i + 1], board[i + 4], board[i + 7]]
            if sum(col) == 2 * self.mark and (self.mark in col):
                try:
                    # print("1col")
                    return cellvalidator(i + col.index(0) * 3 + 1)
                except:
                    pass
        diag = [board[1], board[5], board[9]]
        if sum(diag) == 2 * self.mark and (self.mark in diag):
            try:
                # print("1diag")
                return cellvalidator(diag.index(0) * 4 + 1)
            except:
                pass
        antidiag = [board[3], board[5], board[7]]
        if sum(antidiag) == 2 * self.mark and (self.mark in antidiag):
            try:
                # print("1antidiag")
                return cellvalidator(3 + antidiag.index(0) * 2)
            except:
                pass

        for i in range(3):
            row = [board[i * 3 + 1], board[i * 3 + 2], board[i * 3 + 3]]
            if sum(row) == 2 * self.antimark and (self.antimark in row):
                try:
                    # print("row")
                    return cellvalidator(i * 3 + row.index(0) + 1)
                except:
                    pass
            col = [board[i + 1], board[i + 4], board[i + 7]]
            if sum(col) == 2 * self.antimark and (self.antimark in col):
                try:
                    # print("col")
                    return cellvalidator(i + col.index(0) * 3 + 1)
                except:
                    pass
        diag = [board[1], board[5], board[9]]
        if sum(diag) == 2 * self.antimark and (self.antimark in diag):
            try:
                # print("diag")
                return cellvalidator(diag.index(0) * 4 + 1)
            except:
                pass
        antidiag = [board[3], board[5], board[7]]
        if sum(antidiag) == 2 * self.antimark and (self.antimark in antidiag):
            try:
                # print("antidiag")
                return cellvalidator(3 + antidiag.index(0) * 2)
            except:
                pass
        while True:
            turn = random.choice(getemptycells())
            return turn


class hard(player):
    def getturn(self):
        super().getturn()
        for i in range(3):
            row = [board[i * 3 + 1], board[i * 3 + 2], board[i * 3 + 3]]
            if sum(row) == 2 * self.mark and (self.mark in row):
                try:
                    # print("1row")
                    return cellvalidator(i * 3 + row.index(0) + 1)
                except:
                    pass
            col = [board[i + 1], board[i + 4], board[i + 7]]
            if sum(col) == 2 * self.mark and (self.mark in col):
                try:
                    # print("1col")
                    return cellvalidator(i + col.index(0) * 3 + 1)
                except:
                    pass
        diag = [board[1], board[5], board[9]]
        if sum(diag) == 2 * self.mark and (self.mark in diag):
            try:
                # print("1diag")
                return cellvalidator(diag.index(0) * 4 + 1)
            except:
                pass
        antidiag = [board[3], board[5], board[7]]
        if sum(antidiag) == 2 * self.mark and (self.mark in antidiag):
            try:
                # print("1antidiag")
                return cellvalidator(3 + antidiag.index(0) * 2)
            except:
                pass

        for i in range(3):
            row = [board[i * 3 + 1], board[i * 3 + 2], board[i * 3 + 3]]
            if sum(row) == 2 * self.antimark and (self.antimark in row):
                try:
                    # print("row")
                    return cellvalidator(i * 3 + row.index(0) + 1)
                except:
                    pass
            col = [board[i + 1], board[i + 4], board[i + 7]]
            if sum(col) == 2 * self.antimark and (self.antimark in col):
                try:
                    # print("col")
                    return cellvalidator(i + col.index(0) * 3 + 1)
                except:
                    pass
        diag = [board[1], board[5], board[9]]
        if sum(diag) == 2 * self.antimark and (self.antimark in diag):
            try:
                # print("diag")
                return cellvalidator(diag.index(0) * 4 + 1)
            except:
                pass
        antidiag = [board[3], board[5], board[7]]
        if sum(antidiag) == 2 * self.antimark and (self.antimark in antidiag):
            try:
                # print("antidiag")
                return cellvalidator(3 + antidiag.index(0) * 2)
            except:
                pass

        for i in list(rpermutation(CORNERS)):
            if not board[i]:
                if sum([board[i] for i in getadjacentcorners(i)]):
                    try:
                        return cellvalidator(i)
                    except:
                        pass
        
        if not board[5]:
            return 5
                    
        if board[5] == self.mark:
            for i in list(rpermutation(NON_CORNERS)):
                if board[i] == self.mark:
                    # print("last but one")
                    try:
                        return cellvalidator(CELLS + 1 - i)
                    except:
                        pass
        # print("corner")
        try:
            return cellvalidator(random.choice([i for i in getemptycells() if i in CORNERS]))
        except:
            pass
        # print("last")
        return cellvalidator(random.choice(getemptycells()))


class deadly(player):
    def getturn(self):
        super().getturn()

        ################# Priority ##################
        # Aggressive
        for i in range(3):
            row = [board[i * 3 + 1], board[i * 3 + 2], board[i * 3 + 3]]
            if sum(row) == 2 * self.mark and (self.mark in row):
                try:
                    # print("1row")
                    return cellvalidator(i * 3 + row.index(0) + 1)
                except:
                    pass
            col = [board[i + 1], board[i + 4], board[i + 7]]
            if sum(col) == 2 * self.mark and (self.mark in col):
                try:
                    # print("1col")
                    return cellvalidator(i + col.index(0) * 3 + 1)
                except:
                    pass
        diag = [board[1], board[5], board[9]]
        if sum(diag) == 2 * self.mark and (self.mark in diag):
            try:
                # print("1diag")
                return cellvalidator(diag.index(0) * 4 + 1)
            except:
                pass
        antidiag = [board[3], board[5], board[7]]
        if sum(antidiag) == 2 * self.mark and (self.mark in antidiag):
            try:
                # print("1antidiag")
                return cellvalidator(3 + antidiag.index(0) * 2)
            except:
                pass

        # Defensive
        for i in range(3):
            row = [board[i * 3 + 1], board[i * 3 + 2], board[i * 3 + 3]]
            if sum(row) == 2 * self.antimark and (self.antimark in row):
                try:
                    # print("row")
                    return cellvalidator(i * 3 + row.index(0) + 1)
                except:
                    pass
            col = [board[i + 1], board[i + 4], board[i + 7]]
            if sum(col) == 2 * self.antimark and (self.antimark in col):
                try:
                    # print("col")
                    return cellvalidator(i + col.index(0) * 3 + 1)
                except:
                    pass
        diag = [board[1], board[5], board[9]]
        if sum(diag) == 2 * self.antimark and (self.antimark in diag):
            try:
                # print("diag")
                return cellvalidator(diag.index(0) * 4 + 1)
            except:
                pass
        antidiag = [board[3], board[5], board[7]]
        if sum(antidiag) == 2 * self.antimark and (self.antimark in antidiag):
            try:
                # print("antidiag")
                return cellvalidator(3 + antidiag.index(0) * 2)
            except:
                pass
        ########################################
        
        emptycells = getemptycells()
        mycells = self.getmycells()
        oppenentcells = self.getoppenentcells()
        
        # Only move Defensive
        if len(emptycells) == 8:
            if sum([board[i] for i in CORNERS]) != 0:
                return 5
            elif 5 in oppenentcells:
                return random.choice(CORNERS)
        
        # Only move 2 Defensive
        if len(emptycells) % 2 == 0 and 5 in mycells:
            for i in list(rpermutation(NON_CORNERS)):
                try:
                    return cellvalidator(i)
                except:
                    pass

        # Aggressive
        if len(emptycells) == 9:
            return random.choice(CORNERS + [5] + [5])

        if len(emptycells) == 7 and (5 in mycells) and sum([board[i] for i in CORNERS]) != 0:
            for i in CORNERS:
                if i in oppenentcells:
                    try:
                        return cellvalidator(CELLS + 1 - i)
                    except:
                        pass

        if len(emptycells) % 2 != 0:
            if sum([board[i] for i in CORNERS]) != 0:
                for i in list(rpermutation(CORNERS)):
                    if not board[i] and sum([board[i] for i in getadjacentcorners(i)]):
                        adjcells = getadjacentcells(i)
                        if not(adjcells[0] in oppenentcells or adjcells[1] in oppenentcells):
                            try:
                                return cellvalidator(i)
                            except:
                                pass
            else:
                try:
                    # print("corner")
                    return cellvalidator(random.choice(CORNERS))
                except:
                    pass
            for i in list(rpermutation(CORNERS)):
                if not board[i]:
                    if sum([board[i] for i in getadjacentcorners(i)]):
                        try:
                            return cellvalidator(i)
                        except:
                            pass

        if not board[5]:
            return 5
        
        # Adjacent corners
        for i in list(rpermutation(CORNERS)):
            if not board[i]:
                if sum([board[i] for i in getadjacentcorners(i)]):
                    try:
                        return cellvalidator(i)
                    except:
                        pass
        
        # Non Corners for mid
        if len(emptycells) % 2 == 0:
            if board[5] == self.mark:
                for i in list(rpermutation(NON_CORNERS)):
                    if board[i] == self.mark:
                        # print("last but one")
                        try:
                            return cellvalidator(CELLS + 1 - i)
                        except:
                            pass
        
        # Corners
        try:
            # print("corner")
            return cellvalidator(random.choice([i for i in getemptycells() if i in CORNERS]))
        except:
            pass

        if board[5] == self.mark:
            for i in list(rpermutation(NON_CORNERS)):
                if board[i] == self.mark:
                    # print("last but one")
                    try:
                        return cellvalidator(CELLS + 1 - i)
                    except:
                        pass

        # print("last")
        return cellvalidator(random.choice(getemptycells()))

    def getmycells(self):
        return [i for i in range(1, 10) if board[i] == self.mark]
    
    def getoppenentcells(self):
        return [i for i in range(1, 10) if board[i] == self.antimark]
        

def getintinput(prompt, lower, upper):
    while True:
        print()
        try:
            num = int(input(prompt))
        except:
            print("You must enter one number from the options shown above!!!")
        else:
            if num < lower or num > upper:
                print("You must choose a number between {} and {}!!!".format(lower, upper))
            else:
                break
    return num


def headline():
    print("""
            ==============================
                      TIC TAC TOE
            ==============================


            """)
    welcome = "Welcome to the game..."
    for i in welcome:
        print(i, end="")
        time.sleep(0.1)
    print("\n")
    while True:
        name = input("Enter your name: ")
        if len(name) != 0:
            break
        else:
            print("You must enter a name to play!!!")
    mark = getintinput("Choose your mark\n1. Cross (X)  2. Round (O): ", 1, 2)
    return name, mark


def init():
    diff = getintinput("Choose your difficulty\n1. Easy   2. Medium  3. Hard  4. Deadly:  ", 1, 4)
    return diff


def showboard():
    print()
    print("   |   |   ")
    print(f" {signs[board[1]]} | {signs[board[2]]} | {signs[board[3]]} ")
    print("   |   |   ")
    for _ in range(11):
        print("—", end="")
    print("\n   |   |   ")
    print(f" {signs[board[4]]} | {signs[board[5]]} | {signs[board[6]]} ")
    print("   |   |   ")
    for _ in range(11):
        print("—", end="")
    print("\n   |   |   ")
    print(f" {signs[board[7]]} | {signs[board[8]]} | {signs[board[9]]} ")
    print("   |   |   ")


def getemptycells():
    return [i for i in range(1, 10) if board[i] == 0]


def cellvalidator(cell):
    if board[cell] == 0:
        return cell
    else:
        # print(f"Cell {cell} is occupied!!!")
        raise Exception()


def getadjacentcorners(cell):
    adjacent = CORNERS[:]
    adjacent.remove(cell)
    adjacent.remove(CELLS + 1 - cell)
    return adjacent


def getadjacentcells(cell):
    if cell < 5:
        return [cell * 2, 5 - cell]
    else:
        return [15 - cell, cell - 1]


def solve():
    for i in range(3):
        if board[i * 3 + 1] == board[i * 3 + 2] == board[i * 3 + 3] and board[i * 3 + 1] != 0:
            return board[i * 3 + 1]
        elif board[i + 1] == board[i + 4] == board[i + 7] and board[i + 1] != 0:
            return board[i + 1]
    if board[1] == board[5] == board[9] and board[1] != 0:
        return board[1]
    elif board[3] == board[5] == board[7] and board[3] != 0:
        return board[3]
    try:
        list(board.values()).index(0)
    except:
        return -1


def marker(cell, mark):
    if (cell < 1 and cell > 10):
        print(f"Cell: {cell} not exist!!!")
        raise Exception()
    elif board[cell] != 0:
        print(f"Cell: {cell} is occupied!!!")
        raise Exception()
    else:
        board[cell] = mark


def getwinner(winner, human, comp):
    showboard()
    if winner == -1:
        print("\nMatch Drawn", end="")
        for _ in range(3):
            print(".", end="")
            time.sleep(0.2)
    elif winner:
        if human.mark == winner:
            print(f"\n{human.name} Wins!", end="")
        else:
            print(f"\n{comp.name} Wins!", end="")
        for _ in range(15):
            print("!", end="")
            time.sleep(0.05)
    key = getintinput("\nDO you want to play again?\n1. Yes   2. No:  ", 1, 2)
    board = {}
    for i in range(9):
        board[i + 1] = 0
    winner = None
    return key, board, winner


############### GAME ##################
name, mark = headline()
while True:
    diff = init()
    human = user(name, mark)
    if diff == 1:
        comp = easy("Computer", mark % 2 + 1)
    elif diff == 2:
        comp = medium("Computer", mark % 2 + 1)
    elif diff == 3:
        comp = hard("Computer", mark % 2 + 1)
    else:
        comp = deadly("Computer", mark % 2 + 1)
    if random.randint(0, 1):
        players = [human, comp]
    else:
        players = [comp, human]
    while True:
        for p in players:
            marker(p.getturn(), p.mark)
            winner = solve()
            if winner:
                break
        if winner:
            break
    key, board, winner = getwinner(winner, human, comp)
    if key == 2:
        print("")
        endstr = "Good Bye..."
        for i in endstr:
            print(i, end="")
            time.sleep(0.1)
        break
############### END ###################
