import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from game_of_life_3d import GameOfLife3D


def init_window(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
    glEnable(GL_DEPTH_TEST)

def init_gl(width, height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / float(height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    width, height = 800, 600
    init_window(width, height)
    init_gl(width, height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game.step()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -30)  # Move the camera back to see the grid
        glRotatef(25, 1, 0, 0)       # Rotate the view to see the grid better

        game = GameOfLife3D(size=10)

        for x in range(game.size):
            for y in range(game.size):
                for z in range(game.size):
                    if game.grid[x, y, z] == 1:
                        draw_cube(x - game.size / 2, y - game.size / 2, z - game.size / 2)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
