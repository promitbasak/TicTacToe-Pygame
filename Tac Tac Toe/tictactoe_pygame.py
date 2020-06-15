import pygame
import random
import sys

CELLS = 9
PLAYERS = 2
CORNERS = [1, 3, 7, 9]
NON_CORNERS = [2, 4, 6, 8]
board = {}
for i in range(9):
    board[i + 1] = 0
signs = {0: " ", 1: "X", 2: "O"}
winner = None
boardX = 175
boardY = 130
icon = pygame.image.load("ttticon2.png")
pygame.display.set_icon(icon)
fpsClock = pygame.time.Clock()
boardimg = pygame.image.load("board3d.png")
crossimg = pygame.image.load("cross3d.png")
roundimg = pygame.image.load("cube.png")
bannerimg = pygame.image.load("tttbanner.png")
winimg = pygame.image.load("winsmall.png")
loseimg = pygame.image.load("losesmall.png")
drawimg = pygame.image.load("drawsmall.png")
markerimg = pygame.image.load("marker.png")
diffimg = pygame.image.load("difficulty.png")
backimg = pygame.image.load("back.png")
clickimg = pygame.image.load("click.png")


def rpermutation(a):
    array = a[:]
    for _ in range(len(array)):
        yield array.pop(random.randint(0, len(array) - 1))


class player:
    def __init__(self, name, mark):
        self.name = name
        self.sign = "X" if mark == 1 else "O"
        self.mark = mark
        self.playings = []
        self.antimark = mark % 2 + 1

    def getturn(self):
        print(f"\n{self.name}'s Turn:")
        print(f"\n{self.name} is giving his turn")
        print()


class user(player):
    def getturn(self):
        while True:
            turn = getinput()
            if board[turn] == 0:
                print("Good turn")
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
                        if not (adjcells[0] in oppenentcells or adjcells[1] in oppenentcells):
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
    return None


def marker(cell, mark):
    if 1 > cell > 10:
        print(f"Cell: {cell} not exist!!!")
        raise Exception()
    elif board[cell] != 0:
        print(f"Cell: {cell} is occupied!!!")
        raise Exception()
    else:
        board[cell] = mark


def getinput():
    begin = True
    key = None
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                key = keytonum(pygame.mouse.get_pos())
                if key:
                    begin = False
            if event.type == pygame.KEYDOWN:
                key = keytonum(event.key)
                if key:
                    begin = False
        pygame.display.update()
        showboard()

    return key


def getwinner(winner):
    begin = True
    showboard()
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                begin = False
            if event.type == pygame.KEYDOWN:
                begin = False
        if winner == -1:
            screen.blit(drawimg, (108.5, 5))
        elif winner == human.mark:
            screen.blit(winimg, (108.5, 5))
        else:
            screen.blit(loseimg, (108.5, 5))
        screen.blit(clickimg, (219, 560))
        pygame.display.update()
        fpsClock.tick(30)
    board = {}
    for i in range(9):
        board[i + 1] = 0
    winner = None
    return board, winner


def headline():
    begin1 = True
    begin2 = True
    mark = None
    while begin1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                begin1 = False
            if event.type == pygame.KEYDOWN:
                begin1 = False
        screen.blit(bannerimg, (0, 0))
        pygame.display.update()
        fpsClock.tick(30)
    while begin2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 158 <= x <= 400 and 290 <= y <= 430:
                    mark = 1
                    begin2 = False
                if 434 <= x <= 675 and 290 <= y <= 430:
                    mark = 2
                    begin2 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mark = 1
                    begin2 = False
                if event.key == pygame.K_2:
                    mark = 2
                    begin2 = False
        screen.blit(markerimg, (0, 0))
        pygame.display.update()
        fpsClock.tick(30)
    return mark


def init():
    begin = True
    diff = None
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 110 <= x <= 400 and 317 <= y <= 398:
                    diff = 1
                    begin = False
                if 438 <= x <= 730 and 317 <= y <= 398:
                    diff = 2
                    begin = False
                if 110 <= x <= 400 and 432 <= y <= 512:
                    diff = 3
                    begin = False
                if 438 <= x <= 730 and 432 <= y <= 512:
                    diff = 4
                    begin = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    diff = 1
                    begin = False
                if event.key == pygame.K_2:
                    diff = 2
                    begin = False
                if event.key == pygame.K_3:
                    diff = 3
                    begin = False
                if event.key == pygame.K_4:
                    diff = 4
                    begin = False
        screen.blit(diffimg, (0, 0))
        pygame.display.update()
        fpsClock.tick(30)
    return diff


def showboard():
    screen.blit(backimg, (0, 0))
    screen.blit(boardimg, (boardX, boardY))
    for i in range(1, 10):
        if board[i]:
            putmark(i, board[i])
    pygame.display.update()


def putmark(num, sign):
    markX = boardX + 20 + (num - 1) % 3 * 155
    markY = boardY + 20 + (num - 1) // 3 * 155
    if sign == 1:
        screen.blit(crossimg, (markX, markY))
    elif sign == 2:
        screen.blit(roundimg, (markX, markY))
    else:
        print("Invalid Sign!")


def keytonum(key):
    if isinstance(key, tuple):
        x, y = key
        if 140 <= y <= 265:
            if 180 <= x <= 310:
                if not board[1]:
                    return 1
            if 341 <= x <= 459:
                if not board[2]:
                    return 2
            if 490 <= x <= 613:
                if not board[3]:
                    return 3
        if 297 <= y <= 414:
            if 180 <= x <= 310:
                if not board[4]:
                    return 4
            if 341 <= x <= 459:
                if not board[5]:
                    return 5
            if 490 <= x <= 613:
                if not board[6]:
                    return 6
        if 446 <= y <= 572:
            if 180 <= x <= 310:
                if not board[7]:
                    return 7
            if 341 <= x <= 459:
                if not board[8]:
                    return 8
            if 490 <= x <= 613:
                if not board[9]:
                    return 9
    else:
        if key == pygame.K_1:
            if not board[1]:
                return 1
        elif key == pygame.K_2:
            if not board[2]:
                return 2
        elif key == pygame.K_3:
            if not board[3]:
                return 3
        elif key == pygame.K_4:
            if not board[4]:
                return 4
        elif key == pygame.K_5:
            if not board[5]:
                return 5
        elif key == pygame.K_6:
            if not board[6]:
                return 6
        elif key == pygame.K_7:
            if not board[7]:
                return 7
        elif key == pygame.K_8:
            if not board[8]:
                return 8
        elif key == pygame.K_9:
            if not board[9]:
                return 9


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TicTacToe", "tic-tac-toe.png")
screen.fill((20, 50, 80))

key = None
running = True
mark = headline()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            running2 = False
            sys.exit()
    diff = init()
    for i in range(100):
        showboard()
    running2 = True

    human = user("You", mark)
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
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running2 = False
                sys.exit()
        showboard()
        for p in players:
            pygame.display.update()
            showboard()
            marker(p.getturn(), p.mark)
            winner = solve()
            if winner:
                break
        if winner:
            running2 = False
            board, winner = getwinner(winner)
            pygame.display.update()

        showboard()
        pygame.display.update()
        fpsClock.tick(30)
