import time
from SearchAlgorithms import AEstrela
from TaxiDriverProblem import TaxiDriver
import numpy as np
import gym

env = gym.make("Taxi-v3").env
M = np.zeros((env.desc.shape[0],env.desc.shape[1]))
M = M.astype(str)
points = ["R", "G", "B", "Y"]
letters = []
for i in range(env.desc.shape[0]):
    for j in range(env.desc.shape[1]):
        M[i,j] = env.desc[i,j].decode('UTF-8')
        if M[i,j] in points:
            letters.append([i,j])
start = [1,6]
M[start[0],start[1]] = '0'
map = env.desc

def test1():
    passenger = [1,0]
    goal = [2,0]
    blocks = []
    shape = [4,4]
    position = [0,0]
    on_board = False 
    print('Busca A *')
    state = TaxiDriver("", position, passenger, on_board, goal, shape, blocks)
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print("")
    print("=======================================")
    print("Teste 1")
    print(f"Tempo de resolucao: {tf - ts}")
    assert result.show_path() == " ; down ; pick passenger ; down"

def test2():
    passenger = [4,5]
    goal = [0,0]
    blocks = [[0,4],[1,4],[2,4],[3,4],[4,4],[5,4]]
    shape = [7,7]
    position = [0,0]
    on_board = False 
    print('Busca A *')
    state = TaxiDriver("", position, passenger, on_board, goal, shape, blocks)
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print("")
    print("=======================================")
    print("Teste 2")
    print(f"Tempo de resolucao: {tf - ts}")
    assert result.show_path() == " ; right ; right ; right ; right ; right ; down ; down ; down ; down ; pick passenger ; left ; left ; left ; left ; left ; up ; up ; up ; up"

def test3():
    passenger = [8,5]
    goal = [9,0]
    blocks = [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5]]
    shape = [10,10]
    position = [0,0]
    on_board = False 
    print('Busca A *')
    state = TaxiDriver("", position, passenger, on_board, goal, shape, blocks)
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print("")
    print("=======================================")
    print("Teste 3")
    print(f"Tempo de resolucao: {tf - ts}")
    assert result.show_path() == " ; right ; right ; right ; right ; right ; down ; down ; down ; down ; down ; down ; down ; down ; pick passenger ; left ; left ; left ; left ; left ; down"

def test4():
    passenger = [8,5]
    goal = [9,0]
    blocks = [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[6,4],[7,4],[8,4],[9,4]] 
    shape = [10,10]
    position = [0,0]
    on_board = False 
    print('Busca A *')
    state = TaxiDriver("", position, passenger, on_board, goal, shape, blocks)
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print("")
    print("=======================================")
    print("Teste 4")
    print(f"Tempo de resolucao: {tf - ts}")
    assert result.show_path() == " ; right ; right ; right ; right ; right ; down ; down ; down ; down ; down ; down ; down ; down ; pick passenger ; left ; left ; left ; left ; left ; down"
