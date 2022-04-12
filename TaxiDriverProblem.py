import time
from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    def __init__(self, operator, position, passenger, on_board, goal, shape, blocks):
        self.operator = operator
        self.position = position
        self.passenger = passenger
        self.on_board = on_board
        self.goal = goal
        self.shape = shape
        self.blocks = blocks

    def env(self):
        #print(" ; "+str(self.operator)+str(self.position)+str(self.on_board))
        return str(self.operator)+str(self.position)+str(self.on_board)

    def is_movable(self, position):
        for b in self.blocks:
            if (b == position):
                return False
        return True

    def is_goal(self):
        return (self.position == self.goal) and self.on_board
    
    def cost(self):
        return 1

    def sucessors(self):
        sucessors = []

        # Up
        if (self.position[0]-1 >= 0 and self.is_movable((self.position[0]-1, self.position[1]))):
            sucessors.append(TaxiDriver("up", [self.position[0]-1, self.position[1]], self.passenger, self.on_board, self.goal, self.shape, self.blocks))
        
        # Down
        if (self.position[0]+1 < self.shape[0] and self.is_movable((self.position[0]+1, self.position[1]))):
            sucessors.append(TaxiDriver("down", [self.position[0]+1, self.position[1]], self.passenger, self.on_board, self.goal, self.shape, self.blocks))

        # Left
        if (self.position[1]-1 >= 0 and self.is_movable((self.position[0], self.position[1]-1))):
            sucessors.append(TaxiDriver("left", [self.position[0], self.position[1]-1], self.passenger, self.on_board, self.goal, self.shape, self.blocks))

        # Right
        if (self.position[1]+1 < self.shape[1] and self.is_movable((self.position[0], self.position[1]+1))):
            sucessors.append(TaxiDriver("right", [self.position[0], self.position[1]+1], self.passenger, self.on_board, self.goal, self.shape, self.blocks))

        # Get Passenger
        if ((not self.on_board) and (self.position == self.passenger)):
            sucessors.append(TaxiDriver("pick passenger", self.position, self.passenger, True, self.goal, self.shape, self.blocks))

        return sucessors

    def description(self):
        return "Taxi Driver Problem"

    def print(self):
        return str(self.operator)

    def h(self):

        if (self.on_board):
            i_goal = abs(self.position[0] - self.goal[0])
            j_goal = abs(self.position[1] - self.goal[1])

        else:
            i_goal  = abs(self.position[0] - self.passenger[0])
            j_goal = abs(self.position[1] - self.passenger[1])

        return i_goal + j_goal

    
def main():

    passenger = [8,5]
    goal = [9,0]
    blocks = [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[6,4],[7,4],[8,4],[9,4]] 
    shape = [10,10]
    position = [0,0]
    on_board = False 
    print('Busca A *')
    state = TaxiDriver("", position, passenger, on_board, goal, shape, blocks)
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()