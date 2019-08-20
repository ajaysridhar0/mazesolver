import time

class Maze:
    def __init__(self):
        self.xdim = 0
        self.ydim = 0
        self.maze = []
    def read_file(self, filename):
        with open(filename) as f_obj:
            for line in f_obj:
                self.maze.append(list(line.rstrip()))
        self.xdim = len(self.maze)
        self.ydim = len(self.maze[0])

class MazeSolver:
    def solve_maze(self, maze, x, y):
        print("bug: ", maze[18][17])
        # print(maze[y][x])
        if y > -1 and y < len(maze) and x > -1 and x < len(maze[y]) and maze[y][x] == ' ':
            maze[y][x] = '#'
            # check if right tile is open
            if x + 1 < len(maze[y]) and (maze[y][x + 1] != "+" and maze[y][x + 1] != "|"):
                animate(maze)
                self.solve_maze(maze, x + 1, y)
            # check if down tile is open
            if y + 1 < len(maze):
                animate(maze)
                self.solve_maze(maze, x, y + 1)
            # check if left tile is open
            if x - 1 > -1 and (maze[y][x - 1] != "+" and maze[y][x - 1] != "|"):
                animate(maze)
                self.solve_maze(maze, x - 1, y)
            # check if up tile is open
            if y - 1 > -1 and (maze[y - 1][x] != "+" and maze[y - 1][x] != "-"):
                animate(maze)
                self.solve_maze(maze, x, y - 1)
            # check if maze is solved
            if x == len(maze[y]) - 1 and y == len(maze) - 2:
                animate(maze)
                return 0
        print("Done")
        return -1

def print_maze(maze):
    for i in range(0, len(maze)):
        row = ""
        for j in range(0, len(maze[i])):
            row += maze[i][j]
        print(row)

def animate(maze):
    print_maze(maze)
    for i in range(0, 5):
        print("")
    time.sleep(0.05)

def main():
    maze_obj = Maze()
    maze_obj.read_file("maze1.txt")
    maze_solver_obj = MazeSolver()
    print_maze(maze_obj.maze)
    maze_solver_obj.solve_maze(maze_obj.maze, 0, 1)
main()
