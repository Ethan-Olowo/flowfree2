# Flow Free 2

Flow Free 2 is a puzzle game inspired by the original Flow Free. The objective is to connect pairs of colored dots on a grid, filling the entire board with lines without overlapping. This project is built with Python, using PyQt5 for the UI and pygame for grid rendering.

## Features
- Interactive grid-based gameplay
- Procedural level generation using A* pathfinding
- Colorful lines and themes
- Home page UI (PyQt5)
- Game page with grid and path visualization (pygame)

## File Structure

```
flowfree2/
│
├── main.py                # Entry point for the application
├── requirements.txt       # Python dependencies (PyQt5, pygame)
├── readme.md              # Project documentation
│
├── logic/
│   ├── level_creator.py   # Level generation logic (A*, grid filling)
│   ├── levels.json        # Placeholder for level data
│   └── __pycache__/       # Python cache files
│
├── ui/
│   ├── controller.py      # (Empty, for future game logic control)
│   ├── game_page.py       # Pygame-based grid and path rendering
│   ├── home_page.py       # PyQt5 home screen UI
│   ├── theme.py           # Color and style definitions
│   └── __pycache__/       # Python cache files
```

## Current Progress

- **Level Generation:**
  - Uses A* pathfinding to create paths between random points on the grid.
  - Handles edge cases like isolated cells and attempts to fill all grid spaces.
  - Logic is implemented in `logic/level_creator.py`.

- **UI:**
  - Home page built with PyQt5 (`ui/home_page.py`).
  - Game page uses pygame to render the grid and paths (`ui/game_page.py`).
  - Color themes defined in `ui/theme.py`.

- **Main Application:**
  - `main.py` can launch either the home page or directly start a game for testing.

- **Requirements:**
  - All dependencies listed in `requirements.txt`.

## Next Steps
- Implement game logic controller (`ui/controller.py`).
- Add level saving/loading (`logic/levels.json`).
- Improve UI/UX and add menus.
- Add win/loss conditions and user interaction for drawing lines.

---
This project is in early development. Contributions and suggestions are welcome!
