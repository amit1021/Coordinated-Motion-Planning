import pygame


class boardgame1():

    def __init__(self, height):
        self.robot = [[0] * height for i in range(height)]
        self.robot1 = [[0] * height for i in range(height)]
        self.height = height

    def cratetable(self):
        pygame.init()
        if (self.height == 20): WIDTH = 800
        if (self.height == 30): WIDTH = 900
        if (self.height == 60): WIDTH = 900

        ROWS = self.height
        win = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("robot")
        gap = WIDTH // ROWS
        # Starting points
        x = 0
        y = 0
        bg1 = pygame.image.load('try2.jpg')
        win.blit(bg1, (0, 0))
        # win.fill((0, 0, 0))

        for i in range(ROWS):
            x = i * gap
            pygame.draw.line(win, (0, 0, 0), (x, 0), (x, WIDTH), 2)
            pygame.draw.line(win, (0, 0, 0), (0, x), (WIDTH, x), 2)

        dis_to_cen = WIDTH // ROWS // 2
        for i in range(len(self.robot)):
            for j in range(len(self.robot)):
                x = dis_to_cen * (2 * j + 1)
                y = dis_to_cen * (2 * i + 1)

                if (self.robot[i][j] != 0 and self.height == 30):
                    if self.robot[i][j] != self.robot1[i][j]:
                        pygame.draw.circle(win, (255, 0, 0), (x, y+4), 10)
                        font = pygame.font.Font('freesansbold.ttf', 10)
                        text = font.render(str(self.robot[i][j]), True, (255, 255, 51))
                        textRect = text.get_rect()
                        textRect.center = (x, y+4)
                        win.blit(text, textRect)
                    if self.robot[i][j] == self.robot1[i][j]:
                       pygame.draw.circle(win, (0, 0, 128), (x, y+4), 10)
                       font = pygame.font.Font('freesansbold.ttf', 10)
                       text = font.render(str(self.robot[i][j]), True, (255, 255, 51))
                       textRect = text.get_rect()
                       textRect.center = (x, y+4)
                       win.blit(text, textRect)

        for i in range(len(self.robot)):
            for j in range(len(self.robot)):
                x = dis_to_cen * (2 * j + 1)
                y = dis_to_cen * (2 * i + 1)
                if (self.robot1[i][j] != 0 and self.robot1[i][j] != -1 and self.height == 30):
                    font = pygame.font.Font('freesansbold.ttf', 10)
                    text = font.render(str(self.robot1[i][j]), True, (51, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (x - 5, y - 9)
                    win.blit(text, textRect)
                if (self.robot1[i][j] == -1 and self.height == 30):
                    #pygame.draw.circle(win, (0, 0, 0), (x, y + 4), 10)
                    #pygame.draw.rect(win, (204, 102, 0), [x-8, y-8, 18, 18])
                    font = pygame.font.Font('freesansbold.ttf', 25)
                    text = font.render(str("x"), True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (x, y)
                    win.blit(text, textRect)
        pygame.display.flip()
        pygame.time.delay(5)
        return
