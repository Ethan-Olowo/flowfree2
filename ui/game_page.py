import sys
import pygame
from logic.level_creator import generate_level
from ui.theme import lineColors


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
PADDING = 25  # Padding on each side in pixels
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

def draw_grid(screen, columns, rows, cell_width, cell_height):
    # Draw vertical lines
    for x in range(columns + 1):
        start_pos = (PADDING + x * cell_width, PADDING)
        end_pos = (PADDING + x * cell_width, PADDING + rows * cell_height)
        pygame.draw.line(screen, GRAY, start_pos, end_pos)
    # Draw horizontal lines
    for y in range(rows + 1):
        start_pos = (PADDING, PADDING + y * cell_height)
        end_pos = (PADDING + columns * cell_width, PADDING + y * cell_height)
        pygame.draw.line(screen, GRAY, start_pos, end_pos)

def start_game(columns, rows):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flow Free 2")
    clock = pygame.time.Clock()

    # Calculate cell size based on padding and grid dimensions
    cell_width = (SCREEN_WIDTH - 2 * PADDING) // columns
    cell_height = (SCREEN_HEIGHT - 2 * PADDING) // rows

    # Generate level paths
    paths = generate_level(rows, columns)
    print("Generated Level:")
    for path in paths:
        print(path)
    # Assign a color to each path from lineColors (dictionary)
    color_list = list(lineColors.values())
    path_colors = [color_list[i % len(color_list)] for i in range(len(paths))]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen, columns, rows, cell_width, cell_height)
        
        # Draw paths
        for idx, path in enumerate(paths):
            color = path_colors[idx]
            # Draw the path lines
            for i in range(len(path) - 1):
                start = (PADDING + path[i][0] * cell_width + cell_width // 2,
                         PADDING + path[i][1] * cell_height + cell_height // 2)
                end = (PADDING + path[i + 1][0] * cell_width + cell_width // 2,
                       PADDING + path[i + 1][1] * cell_height + cell_height // 2)
                pygame.draw.line(screen, color, start, end, 10)
            # Draw a circle at the start of the path
            if path:
                start_circle = (PADDING + path[0][0] * cell_width + cell_width // 2,
                               PADDING + path[0][1] * cell_height + cell_height // 2)
                pygame.draw.circle(screen, color, start_circle, min(cell_width, cell_height) // 3)
                end_circle = (PADDING + path[-1][0] * cell_width + cell_width // 2,
                              PADDING + path[-1][1] * cell_height + cell_height // 2)
                pygame.draw.circle(screen, color, end_circle, min(cell_width, cell_height) // 3)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
