import pygame

from grid import Grid

# Initialize Pygame
pygame.init()

# Constants
bg_color = (246, 241, 241)
dot_color = (20, 108, 148)
# line_color = (200, 200, 200)
line_color = bg_color

# Set up the window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

# Set up graphics
font = pygame.font.SysFont(None, 48)
text = font.render("", True, (3, 0, 0))

# Initialize the Grid
grid = Grid()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the cells in the grid
    grid.update_cells()

    # Clear the screen
    screen.fill(bg_color)

    for x in range(grid.width):
        for y in range(grid.height):
            rect = pygame.Rect(x * grid.cell_size, y * grid.cell_size, grid.cell_size, grid.cell_size)
            if grid.cells[x][y] == 1:
                pygame.draw.rect(screen, dot_color, rect)
            else:
                pygame.draw.rect(screen, bg_color, rect)
            pygame.draw.rect(screen, line_color, rect, 1)

    # Draw graphics
    screen.blit(text, (400, 300))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
