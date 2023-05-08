import numpy as np

class GameOfLife3D:
    def __init__(self, size):
        self.size = size
        self.grid = np.random.choice([0, 1], size=(size, size, size), p=[0.8, 0.2])

    def count_neighbors(self, x, y, z):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if i == 0 and j == 0 and k == 0:
                        continue
                    xi, yj, zk = (x + i) % self.size, (y + j) % self.size, (z + k) % self.size
                    neighbors += self.grid[xi, yj, zk]
        return neighbors

    def step(self):
        new_grid = self.grid.copy()
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    live_neighbors = self.count_neighbors(x, y, z)
                    if self.grid[x, y, z] == 1:
                        if live_neighbors < 2 or live_neighbors > 3:
                            new_grid[x, y, z] = 0
                    elif live_neighbors == 3:
                        new_grid[x, y, z] = 1
        self.grid = new_grid

    def run_simulation(self, steps):
        for _ in range(steps):
            self.step()
            self.print_slice()
            print("\n")

    def print_slice(self, z=0):
        for x in range(self.size):
            for y in range(self.size):
                print("#" if self.grid[x, y, z] == 1 else ".", end="")
            print()

def draw_cube(x, y, z):
    vertices = [
        [x-0.5, y-0.5, z-0.5], [x+0.5, y-0.5, z-0.5],
        [x+0.5, y+0.5, z-0.5], [x-0.5, y+0.5, z-0.5],
        [x-0.5, y-0.5, z+0.5], [x+0.5, y-0.5, z+0.5],
        [x+0.5, y+0.5, z+0.5], [x-0.5, y+0.5, z+0.5]
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
