import random
import time


class VacuumCleaner:
    def __init__(self, grid_size=(5, 5)):
        self.grid_size = grid_size
        self.position = (random.randint(0, grid_size[0]-1), random.randint(0, grid_size[1]-1))
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    
    def display_grid(self):
        for i in range(self.grid_size[0]):
            row = ""
            for j in range(self.grid_size[1]):
                if (i, j) == self.position:
                    row += "V "  # Vacuum position
                elif self.grid[i][j] == 1:
                    row += "D "  # Dirt
                else:
                    row += ". "  # Clean
            print(row)
        print("\n")


    def move(self):
        # Moves randomly in up, down, left, or right directions
        x, y = self.position
        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_moves = [m for m in moves if 0 <= m[0] < self.grid_size[0] and 0 <= m[1] < self.grid_size[1]]
        self.position = random.choice(valid_moves)


    def clean(self):
        x, y = self.position
        if self.grid[x][y] == 1:
            print(f"Cleaning dirt at {self.position}")
            self.grid[x][y] = 0


    def run(self, steps=20):
        print("Initial Grid:")
        self.display_grid()
        for _ in range(steps):
            self.clean()
            self.move()
            self.display_grid()
            time.sleep(0.5)


# Run the simulation
vacuum = VacuumCleaner(grid_size=(5, 5))
vacuum.run()