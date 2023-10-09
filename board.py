# Battleship is a 2 player game with the goal of
# trying to sink the opponent's 5 ships while trying/hoping
# for our own ship to not get hit

# Both players are blind to the opponent's board
# all X tiles of the ship S will have to be hit to be considered
# sinked

# Carrier length 5
# Battleship length 4
# Cruiser length 3
# Submarine length 3
# Destroyer length 2

# Each players have 2 grids
# 1 for their own
# 1 for marking which enemy's grid is already shot at

# We will create instances of board (one for each)
# Each class have 2 10x10 arrays
# one for player, one for marking

# Shot == X
# Ship occupied = AAAAA (5 consecutive blocks of A)
# Empty == numbers

class board:

    def __init__(self):
        # Our area
        self.play_area = [[i for i in range(10)] for j in range(10)]
        self.isShot = [[False for i in range(10)] for j in range(10)]
        
        #Enemy area
        self.enemy_area = [[i for i in range(10)] for j in range(10)]
        self.enemy_isShot = [[False for i in range(10)] for j in range(10)]
        
        # Shippings
        # Must be consecutives number of cells vertically or horizontally (eg. Cruiser 5 in a rows) no diagonally
        self.carrier = ['A', 'A', 'A', 'A', 'A']
        self.carrierHit = [False for i in range(5)]
        
        self.battleShip = ['B', 'B', 'B', 'B']
        self.battleShipHit = [False for i in range(4)]
        
        self.cruiser = ['C', 'C', 'C']
        self.cruiserHit = [False for i in range(3)]
        
        self.submarine = ['D', 'D', 'D']
        self.submarineHit = [False for i in range(3)]
        
        self.destroyer = ['E', 'E']
        self.destroyerHit = [False, False]
        
        # Enemy placing random ships
        
        
        
    # 10x10 playable area
    
    def display_board(self):
        
        # Enemy board
        print('--------------------------------------')
        print('Displaying where player shot opponent')
        # Same as player board but without ship displaying logic
        for i in range(10):
            print(i, end='   ')

        for i in range(10):
            print()
            for j in range(10):
                if not self.isShot[i][j]:
                    print('-', end='   ')
                else:
                    # Ship
                    print('X', end='   ')
                
                # Always print row number at the end of each row
                if j == 9:
                    print(i, end='')
        
        print()
        print('--------------------------------------')
        # Player board
        print("Displaying players board")
        for i in range(10):
            print(i, end='   ')

        for i in range(10):
            print()
            for j in range(10):
                if not self.isShot[i][j]:
                    print('-', end='   ')
                else:
                    # Ship or shot
                    print('X', end='   ')
                
                # Always print row number at the end of each row
                if j == 9:
                    print(i, end='')