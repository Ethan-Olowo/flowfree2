import random
import json

import heapq
import math

def is_grid_full(grid):
    return all(cell == 1 for row in grid for cell in row)

def get_empty_cells(grid):
    """Returns a list of the empty cells in the grid."""
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
    if not empty_cells:
        return None
    return empty_cells

def count_surrounding_obstacles(grid, x, y):
    """Counts walls/edges around a square to prefer tight areas over open ones."""
    rows, cols = len(grid), len(grid[0])
    obstacle_count = 0
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] == 1:
            obstacle_count += 1
    return obstacle_count

def heuristic(current, goal, grid):
    """Heuristic with added weight for tight/corner spaces."""
    # Base: Euclidean distance
    base = math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

    # Add bonus: more obstacles near => prefer it
    surrounding_obstacles = count_surrounding_obstacles(grid, current[0], current[1])

    # Encourage tight/corner areas with a small reward
    bonus = -0.2 * surrounding_obstacles  # subtract because lower h(n) = more attractive

    return base + bonus

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = [(heuristic(start, goal, grid), 0, start, [])]
    visited = set()

    while open_set:
        est_total, cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]

        if current == goal:
            print(f"Path found from {start} to {goal} with cost {cost}")
            return path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                g = cost + 1
                h = heuristic(neighbor, goal, grid)
                heapq.heappush(open_set, (g + h, g, neighbor, path))
    return None

def fill_empty_paths(grid, empty_cells, paths):
    """
    Attempts to incorporate remaining empty cells into existing paths by checking if any empty cell is adjacent to the start or end of a path.
    For each empty cell, if it matches the start or end of a path, it is added to that path and removed from the empty cell list.
    The process repeats until no more empty cells can be filled.
    Edge cases:
        - If no empty cells are adjacent to any path endpoints, the function stops and prints a failure message.
        - If the empty_cells list is empty or None, the function returns the paths unchanged.
    Returns the updated list of paths.
    """
    last_empty = None
    
    while empty_cells:
        
        last_empty = empty_cells.copy()
        cells_to_remove = []
        for cell in empty_cells[:]:  # Iterate over a copy to avoid modifying during iteration
            x, y = cell
            # Check if the cell is adjacent to any path start or end points
            for path in paths:
                # Check adjacency to start of path
                if abs(path[0][0] - x) + abs(path[0][1] - y) == 1:
                    # Check if the cell is adjacent to any other cell in the path
                    if not any(abs(px - x) + abs(py - y) == 1 for px, py in path[1:]):
                        print(f"Adding empty cell {cell} adjacent to start of path {path}")
                        path.insert(0, (x, y))
                        cells_to_remove.append(cell)
                        break
                # Check adjacency to end of path
                elif abs(path[-1][0] - x) + abs(path[-1][1] - y) == 1:
                    # Check if the cell is adjacent to any other cell in the path
                    if not any(abs(px - x) + abs(py - y) == 1 for px, py in path[:-1]):
                        print(f"Adding empty cell {cell} adjacent to end of path {path}")
                        path.append((x, y))
                        cells_to_remove.append(cell)
                        break
        
        # Remove cells after iteration
        for cell in cells_to_remove:
            if cell in empty_cells:
                empty_cells.remove(cell)
        
        # If no paths were updated, it means there are no more empty cells to fill
        if last_empty == empty_cells:
            print("No more empty cells to fill, failed to fix level.")
            break

    return paths

    
def check_cell_isolation(grid, cell):
    """
    Checks if a cell is isolated (surrounded by walls or edges).
    Returns True if the cell is isolated, False otherwise.
    """
    x, y = cell
    rows, cols = len(grid), len(grid[0])
    
    # Check all four directions
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            return False  # Found an adjacent empty cell
    
    return True  # No adjacent empty cells found, cell is isolated
                


def generate_level(length, width):
    """
    Generates a level with the length and width of the grid.
    """
    # Create a grid the size of the level
    grid = [[0 for _ in range(width)] for _ in range(length)]

    # Variable to store paths
    paths = []

    #while the grid isnt full
    while not is_grid_full(grid):
        empty_cells = get_empty_cells(grid)
        if all(check_cell_isolation(grid, cell) for cell in empty_cells):
            print("All remaining cells are isolated, trying to fix level.")
            if empty_cells:
                paths = fill_empty_paths(grid, empty_cells.copy(), paths)
            break

        # Randomly select a starting point from the empty cells
        starting_point = random.choice(empty_cells)
        
        ending_point = random.choice(empty_cells)

        while starting_point == ending_point:
            ending_point = random.choice(empty_cells)
        

        # Generate the shortest path using A* algorithm
        path = astar(grid, starting_point, ending_point)

        # Save path
        if path:
            paths.append(path)
            
            # Mark the path in the grid
            for x, y in path:
                grid[x][y] = 1  # Mark path with 1
    
        # If there are only 2 empty cells left, the level generation has failed
        # This is because the starting and ending points are the only two empty cells left
        elif (get_empty_cells(grid) == 2):
            print("Level generation failed.")
            # paths = []
            # grid = [[0 for _ in range(width)] for _ in range(length)]
    

    return paths



