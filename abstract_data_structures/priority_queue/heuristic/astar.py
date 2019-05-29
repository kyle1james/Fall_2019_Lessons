import heapq
import time,random


def path_finder(matrix):

    length = len(matrix)
    start = (0,0,0,0)
    goal = (length-1, length-1)

    parent = {}
    visited = {(0,0): 0}
    unseenNodes = [start]
    heapq.heapify(unseenNodes)

    while unseenNodes:
        minNode = heapq.heappop(unseenNodes)
        #unseenNodes = sorted(unseenNodes, key = lambda x: x[3])
        #minNode = unseenNodes.pop(0)

        current_weight, distance, x, y = minNode
        px, py = x,y

        neighbors = ((x-1,y),(x,y-1),(x+1,y),(x,y+1))
        real_neighbors = ((x,y) for (x,y) in neighbors if 0 <= x < length and 0<= y < len(matrix[0]))

        for cx,cy in real_neighbors:
            cost = current_weight + matrix[cx][cy]
            dist = abs(goal[0] - cx) + abs(goal[1]-cy)
            if (cx,cy) not in parent or cost < visited[(cx,cy)]:
                visited[(cx,cy)] = cost
                unseenNodes.append((cost,dist,cx,cy))
                parent[(cx,cy)] = (px,py)

                if (cx,cy) == goal:
                    print('hey')
                    return (visited[goal])


import random, pprint
matrix = [[x + 1 for x in range(5)] for y in range(5)]
pprint.pprint(matrix)
start_time = time.time()
print(path_finder(matrix))
print("--- %s seconds ---" % (time.time() - start_time))
