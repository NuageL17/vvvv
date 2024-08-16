import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Color Matching Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.color_list = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue')]
        self.target_color = random.choice(self.color_list)

    def new(self):
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.check_color('red')
                elif event.key == pygame.K_g:
                    self.check_color('green')
                elif event.key == pygame.K_b:
                    self.check_color('blue')

    def draw(self):
        self.screen.fill(pygame.Color('white'))
        pygame.draw.rect(self.screen, self.target_color, (350, 250, 100, 100))
        pygame.display.flip()

    def check_color(self, color):
        if color == self.target_color:
            self.target_color = random.choice(self.color_list)
        else:
            self.running = False

if __name__ == "__main__":
    game = Game()
    game.new()
