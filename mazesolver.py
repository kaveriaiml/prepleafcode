import random
import os
from collections import deque

# ANSI color codes
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# Constants
WALL = RED + '▓' + ENDC
OPEN_SPACE = BLUE + '◌' + ENDC
START = GREEN + 'S' + ENDC
END = GREEN + 'E' + ENDC
PATH = GREEN + '◍' + ENDC

# Maze class
class Maze:
    def __init__(self, size, wall_percentage):
        self.size = size
        self.wall_percentage = wall_percentage
        self.maze = self.generate_maze()

    def generate_maze(self):
        maze = [[WALL if random.random() < self.wall_percentage else OPEN_SPACE for _ in range(self.size)] for _ in range(self.size)]
        maze[0][0] = START
        maze[self.size - 1][self.size - 1] = END
        return maze

    def print_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.maze:
            print(' '.join(row))

# BFS pathfinding algorithm
def find_path(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    queue = deque([start])
    parent = {start: None}

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == OPEN_SPACE and (nx, ny) not in parent:
                queue.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    if end in parent:
        x, y = end
        while (x, y) != start:
            maze[x][y] = PATH
            x, y = parent[(x, y)]
        maze[start[0]][start[1]] = START
        maze[end[0]][end[1]] = END
        return True
    else:
        return False

# Main function
def main():
    print("Welcome to the Terminal-Based Maze Solver!")

    while True:
        size = int(input("Enter the size of the maze (n x n): "))
        wall_percentage = 0.25  # Adjust this to change the percentage of walls

        maze = Maze(size, wall_percentage)
        maze.print_maze()

        choice = input("Options:\n1. Print Path\n2. Generate Another Maze\n3. Exit\nEnter your choice: ")

        if choice == '1':
            maze_copy = [row[:] for row in maze.maze]  # Create a copy of the maze
            if find_path(maze_copy):
                maze.print_maze()
            else:
                print("No path found.")
        elif choice == '2':
            continue
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
