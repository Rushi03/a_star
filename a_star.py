def a_star(grid, initial, cost, goal, heuristic):

    delta = [[0, -1],  # Up
             [1, 0],   # Right
             [0, 1],   # Down
             [-1, 0]]  # Left

    # Showed the squares that have been checked
    checked = [[0 for row in range(len(grid))] for col in range(len(grid[0]))]
    checked[initial[0]][initial[1]] = 1

    # Initialization
    x = initial[0]
    y = initial[1]
    h = heuristic[x][y]
    g = 0
    f = g + h

    # The unchecked squares
    unchecked = [[f, g, h, x, y]]

    # Boolean statements
    quit = False        # Quit if square in unchecked cannot expand further
    complete = False    # Stop when the maze has been completed
    counter = 0         # Count the moves

    while not complete and not quit:
        # Check expansion of the squares in list unchecked
        if len(unchecked) == 0:
            quit = True
            print "Cannot expand further."
        else:
            unchecked.sort()
            unchecked.reverse()
            next = unchecked.pop()
            g = next[1]
            x = next[3]
            y = next[4]

            # Check if reached goal
            if x == goal[0] and y == goal[1]:
                complete = True
                print "Completed."
            # Pathfinding
            else:
                for i in range(len(delta)):
                    x_prime = x + delta[i][0]
                    y_prime = y + delta[i][1]
                    if x_prime >= 0 and x_prime < len(grid) and y_prime >= 0 \
                       and y_prime < len(grid[0]):
                        if checked[x_prime][y_prime] == 0 and grid[x_prime][y_prime] == 0:
                            g_prime = g + cost
                            heuristic_prime = heuristic[x_prime][y_prime]
                            f_prime = g_prime + heuristic_prime
                            unchecked.append([f_prime, g_prime, heuristic_prime, x_prime, y_prime])
                            checked[x_prime][y_prime] = 1
            counter += 1

    return checked


'''
Test 1:
- Personal grid
- Manual heuristic
- Even cost for movement
- Start top left corner
- Goal bottom right corner
'''

grid = [[0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 0, 0]]

heuristic = [[8, 7, 6, 5, 4],
             [7, 6, 5, 4, 3],
             [6, 5, 4, 3, 2],
             [5, 4, 3, 2, 1],
             [4, 3, 2, 1, 0]]

initial = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

print a_star(grid, initial, cost, goal, heuristic)
