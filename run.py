from src.game_of_life_3d import GameOfLife3D

if __name__ == "__main__":
    game = GameOfLife3D(size=10)
    game.run_simulation(steps=10)
