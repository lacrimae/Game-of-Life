import time


class Grid:
    GLIDER_OFFSETS = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    BEACON_OFFSETS = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)]
    BEEHIVE_OFFSETS = [(0, 1), (1, 0), (1, 2), (3, 1), (2, 0), (2, 2)]
    BLINKER_OFFSETS = [(0, 0), (0, 1), (0, 2)]
    BLOCK_OFFSETS = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self):
        self.width = 80
        self.height = 60
        self.cell_size = 10
        self.cells = [[0 for y in range(self.height)] for x in range(self.width)]
        self.delay = 0.1
        self.pattern = self.GLIDER_OFFSETS
        # todo: use random function
        self.cells[20][20] = 1
        self.cells[21][20] = 1
        self.cells[22][20] = 1

    # Main logic:
    # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # 2. Any live cell with two or three live neighbours lives on to the next generation.
    # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
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

    def add_cells_pattern_rhombus(self, cell_x, cell_y):
        self.cells[cell_x][cell_y] = 1
        # Handles edge cases
        if cell_x < self.width - 1:
            self.cells[cell_x + 1][cell_y] = 1
        if cell_x > 0:
            self.cells[cell_x - 1][cell_y] = 1
        if cell_y < self.height - 1:
            self.cells[cell_x][cell_y + 1] = 1
        if cell_y > 0:
            self.cells[cell_x][cell_y - 1] = 1

    def add_cells(self, cell_x, cell_y, pattern):
        for dx, dy in pattern:
            x, y = cell_x + dx, cell_y + dy
            if (0 <= x < self.width) and (0 <= y < self.height):
                self.cells[x][y] = 1

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
