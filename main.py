from ui.home_page import HomePage
from ui.game_page import start_game
import sys
from PyQt5.QtWidgets import QApplication

from logic.level_creator import generate_level

def main():
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())

def test_level():
    # Example usage of the generate_level function
    length = 5
    width = 5
    
    

if __name__ == "__main__":
    # main()
    start_game(10, 10)  # Start the game with a 5x5 grid
    # Uncomment the line above to run the main application