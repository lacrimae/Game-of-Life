import time


class Grid:

    def __init__(self):
        self.width = 80
        self.height = 60
        self.cell_size = 10
        self.cells = [[0 for y in range(self.height)] for x in range(self.width)]
        self.delay = 0.1
        # todo: use random function
        self.cells[20][20] = 1
        self.cells[21][20] = 1
        self.cells[22][20] = 1

    # Main logic
    def update_cells(self):
        new_cells = [[0 for y in range(self.height)] for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                neighbors = self.count_neighbors(x, y)
                if self.cells[x][y] == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_cells[x][y] = 1
                else:
                    if neighbors == 3:
                        new_cells[x][y] = 1
        time.sleep(self.delay)
        self.cells = new_cells

    def count_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if i + x < 0 or i + x >= self.width:
                    continue
                if j + y < 0 or j + y >= self.height:
                    continue
                if self.cells[i + x][j + y] == 1:
                    count += 1
        return count
