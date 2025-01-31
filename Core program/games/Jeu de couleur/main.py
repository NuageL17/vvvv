import pygame
from settings import *
from sprites import *
import random
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jeux de couleur")  # Changer le titre ici
        self.clock = pygame.time.Clock()
        self.flash_colours = [YELLOW, BLUE, RED, GREEN]
        self.colours = [DARKYELLOW, DARKBLUE, DARKRED, DARKGREEN]

        self.buttons = [
            Button(110, 50, DARKYELLOW),
            Button(330, 50, DARKBLUE),
            Button(110, 270, DARKRED),
            Button(330, 270, DARKGREEN),
        ]

    def get_high_score(self):
        if not os.path.exists("high_score.txt"):
            with open("high_score.txt", "w") as file:
                file.write("0")
        with open("high_score.txt", "r") as file:
            score = file.read().strip()
            try:
                return int(score)
            except ValueError:
                return 0  # Return 0 if the score is invalid

    def save_score(self):
        with open("high_score.txt", "w") as file:
            if self.score > self.high_score:
                file.write(str(self.score))
            else:
                file.write(str(self.high_score))

    def new(self):
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0
        self.high_score = self.get_high_score()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.clicked_button = None
            self.events()
            self.draw()
            self.update()

    def update(self):
        if not self.waiting_input:
            pygame.time.wait(1000)
            self.pattern.append(random.choice(self.colours))
            for button in self.pattern:
                self.button_animation(button)
                pygame.time.wait(200)
            self.waiting_input = True

        else:
            # pushed the correct button
            if self.clicked_button and self.clicked_button == self.pattern[self.current_step]:
                self.button_animation(self.clicked_button)
                self.current_step += 1

                # pushed the last button
                if self.current_step == len(self.pattern):
                    self.score += 1
                    self.waiting_input = False
                    self.current_step = 0

            # pushed the wrong button
            elif self.clicked_button and self.clicked_button != self.pattern[self.current_step]:
                self.game_over_animation()
                self.save_score()
                self.playing = False

    def button_animation(self, colour):
        for i in range(len(self.colours)):
            if self.colours[i] == colour:
                flash_colour = self.flash_colours[i]
                button = self.buttons[i]

        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = flash_colour
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, ANIMATION_SPEED * step):
                self.screen.blit(original_surface, (0, 0))
                flash_surface.fill((r, g, b, alpha))
                self.screen.blit(flash_surface, (button.x, button.y))
                pygame.display.update()
                self.clock.tick(FPS)
        self.screen.blit(original_surface, (0, 0))

    def game_over_animation(self):
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((self.screen.get_size()))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = WHITE
        for _ in range(3):
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, ANIMATION_SPEED * step):
                    self.screen.blit(original_surface, (0, 0))
                    flash_surface.fill((r, g, b, alpha))
                    self.screen.blit(flash_surface, (0, 0))
                    pygame.display.update()
                    self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BGCOLOUR)
        UIElement(170, 20, f"Score: {str(self.score)}").draw(self.screen)
        UIElement(370, 20, f"High score: {str(self.high_score)}").draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.clicked(mouse_x, mouse_y):
                        self.clicked_button = button.colour

game = Game()
while True:
    game.new()
    game.run()
