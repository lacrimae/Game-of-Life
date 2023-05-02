import pygame

from button import Button
from grid import Grid

# Initialize Pygame
pygame.init()

# Constants
bg_color = (246, 241, 241)
dot_color = (20, 108, 148)
line_color = bg_color
screen_width = 800
screen_height = 600

# Set up the window
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

# Set up graphics
font = pygame.font.SysFont('Arial', 48)
text = font.render("", True, (3, 0, 0))

# Initialize the Grid
grid = Grid()

# Create a new button instance
button_count = 5
button_total_width = (Button.BUTTON_WIDTH + Button.PADDING) * button_count - Button.PADDING
button_x_start = (screen_width - button_total_width) // 2
button_y = screen_height - Button.BUTTON_HEIGHT

glider_button = Button(grid.GLIDER_OFFSETS, 'Glider', (button_x_start, button_y))
# Set is_clicked to True to indicate that glider is the default pattern selected
glider_button.set_is_clicked(True)
beacon_button = Button(grid.BEACON_OFFSETS, 'Beacon',
                       (button_x_start + (Button.BUTTON_WIDTH + Button.PADDING), button_y))
beehive_button = Button(grid.BEEHIVE_OFFSETS, 'Beehive',
                        (button_x_start + 2 * (Button.BUTTON_WIDTH + Button.PADDING), button_y))
blinker_button = Button(grid.BLINKER_OFFSETS, 'Blinker',
                        (button_x_start + 3 * (Button.BUTTON_WIDTH + Button.PADDING), button_y))
block_button = Button(grid.BLOCK_OFFSETS, 'Block',
                      (button_x_start + 4 * (Button.BUTTON_WIDTH + Button.PADDING), button_y))
buttons = (glider_button, beacon_button, beehive_button, blinker_button, block_button)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            handle_button_click(event.pos)
            cell_x, cell_y = x // grid.cell_size, y // grid.cell_size
            grid.add_cells(cell_x, cell_y, grid.pattern)


def handle_button_click(pos):
    # Checks whether click action was on buttons or on the screen
    for button in buttons:
        if button.is_button_clicked(pos):
            # Updates button's is_clicked state and sets grid's pattern
            for b in buttons:
                b.set_is_clicked(b is button)
            grid.pattern = button.pattern
            break


while True:
    # Handle events
    handle_events()
    # Clear the screen
    screen.fill(bg_color)
    # Update the cells in the grid
    grid.update_cells()

    for x in range(grid.width):
        for y in range(grid.height):
            rect = pygame.Rect(x * grid.cell_size, y * grid.cell_size, grid.cell_size, grid.cell_size)
            if grid.cells[x][y] == 1:
                pygame.draw.rect(screen, dot_color, rect)
            else:
                pygame.draw.rect(screen, bg_color, rect)
                pygame.draw.rect(screen, line_color,
                                 pygame.Rect(rect.x + 1, rect.y + 1, rect.width - 1, rect.height - 1), 1)

    # Draw graphics
    screen.blit(text, (400, 300))
    # Draw the buttons
    glider_button.draw(screen)
    beacon_button.draw(screen)
    beehive_button.draw(screen)
    blinker_button.draw(screen)
    block_button.draw(screen)

    # Update the display
    pygame.display.flip()
