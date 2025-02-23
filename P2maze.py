import random

# Define the maze dimensions
MAZE_WIDTH = 21
MAZE_HEIGHT = 11

# Define the maze characters
WALL = '#'
PATH = ' '

# Function to generate the maze
def generate_maze(width, height):
    maze = [[WALL for x in range(width)] for y in range(height)]
    stack = [(0, 0)]
    while stack:
        x, y = stack[-1]
        maze[y][x] = PATH
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2*dx, y + 2*dy
            if (0 <= nx < width) and (0 <= ny < height) and maze[ny][nx] == WALL:
                maze[ny-dy][nx-dx] = PATH
                stack.append((nx, ny))
                break
        else:
            stack.pop()
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Function to solve the maze using DFS
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    while stack:
        x, y = stack.pop()
        if (x, y) == end:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze[0])) and (0 <= ny < len(maze)) and maze[ny][nx] == PATH:
                stack.append((nx, ny))
    return False

# Generate and print the maze
maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
print("Maze:")
print_maze(maze)

# Solve the maze
start = (1, 1)
end = (MAZE_WIDTH-2, MAZE_HEIGHT-2)
if solve_maze(maze, start, end):
    print("Maze solved!")
else:
    print("No solution found.")
