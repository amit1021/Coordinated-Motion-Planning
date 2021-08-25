import pygame
import time


# The object that create GUI is boardgame1
class Gui():
    def __init__(self, height):
        self.src = [[0] * height for i in range(height)]     # Place of the robot
        self.dest = [[0] * height for i in range(height)]    # Destination of robot
        self.height = height           # Size of bord
        self.bgx = 0                   # bgx, bgy - for big boards
        self.bgy = 0

    # The function that creates the gui screen
    # In this function we use "pygame"

    def cratetable(self):

        pygame.init()               # Basic pygame

        ROWS = self.height          # Size of the board
        WIDTH = self.height*30      # The size of the Surface, depends on the size of the board

        # Create Surface
        win = pygame.Surface((WIDTH, WIDTH))

        # Title to screen
        pygame.display.set_caption("Coordinated-Motion-Planning")

        # Size of any row
        gap = WIDTH // ROWS
        # Starting points
        x = 0
        y = 0

        # Background
        # bg1 = pygame.image.load('try2.jpg')
        # win.blit(bg1, (0, 0))
        white = [255, 255, 255]
        win.fill(white)

        # This 'for' to create lines to the board
        for i in range(ROWS):

            x = i * gap
            pygame.draw.line(win, (0, 0, 0), (x, 0), (x, WIDTH), 2)
            pygame.draw.line(win, (0, 0, 0), (0, x), (WIDTH, x), 2)

        dis_to_cen = WIDTH // ROWS // 2

        #  Move across the board and draw the objects
        for i in range(len(self.src)):
            for j in range(len(self.src)):
                x = dis_to_cen * (2 * j + 1)
                y = dis_to_cen * (2 * i + 1)

                if (self.src[i][j] != 0):

                    # Draw the the robots that have not yet reached their destination
                    if self.src[i][j] != self.dest[i][j]:
                        pygame.draw.circle(win, (255, 0, 0), (x, y+4), 10)
                        font = pygame.font.Font('freesansbold.ttf', 10)
                        text = font.render(str(self.src[i][j]), True, (255, 255, 51))
                        textRect = text.get_rect()
                        textRect.center = (x, y+4)
                        win.blit(text, textRect)

                    # Draw the the robots that reached their destination
                    if self.src[i][j] == self.dest[i][j]:
                       pygame.draw.circle(win, (0, 0, 128), (x, y+4), 10)
                       font = pygame.font.Font('freesansbold.ttf', 10)
                       text = font.render(str(self.src[i][j]), True, (255, 255, 51))
                       textRect = text.get_rect()
                       textRect.center = (x, y+4)
                       win.blit(text, textRect)

                # Draw destination of any robot
                if (self.dest[i][j] != 0 and self.dest[i][j] != -1):
                    font = pygame.font.Font('freesansbold.ttf', 10)
                    text = font.render(str(self.dest[i][j]), True, (51, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (x - 5, y - 9)
                    win.blit(text, textRect)

                # Draw obstacles
                if (self.dest[i][j] == -1 ):
                    font = pygame.font.Font('freesansbold.ttf', 25)
                    text = font.render(str("x"), True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (x, y)
                    win.blit(text, textRect)

        # The display screen , size 900x900
        screen = pygame.display.set_mode((1100, 1100))

        # Time for while
        timeout = time.time() + 0.01

        # For the keyboard commands
        # Listens to commands
        while True:

            test = 0
            if test == 5 or time.time() > timeout:
                break
            test = test - 1

            # The part that the screen will show in the win
            # win is a screen, define in line 23
            screen.blit(win, (self.bgy, self.bgx - self.height*30))
            screen.blit(win, (self.bgy, self.bgx))
            screen.blit(win, (self.bgy, self.bgx + self.height*30))
            pygame.display.update()

            # Event for the keyboard
            for event in pygame.event.get():

                # Close the screen
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    exit()
                # Move according keyboard
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_UP:
                        self.bgx = self.bgx + 3 * self.height

                    elif event.key == pygame.K_LEFT:
                        self.bgy = self.bgy + 3 * self.height

                    elif event.key == pygame.K_DOWN:
                        self.bgx = self.bgx - 3 * self.height

                    elif event.key == pygame.K_RIGHT:
                        self.bgy = self.bgy - 3 * self.height









