import pygame, sys, random
from pygame import Vector2
# create a snake game with main menu, then create an ai that completely destroys the game

class snake:
    def __init__(self, start_body:list[Vector2], start_direction:Vector2) -> None:
        self.body = start_body
        self.direction = start_direction
        self.add_block = False

    def move(self, direction:Vector2) -> None:
        new_body = self.body.append(self.body[-1] + self.direction)
    
        if not self.add_block: new_body = new_body[1:]
        else: self.add_block = False

        self.body = new_body
    
    def render(self) -> None:
        for block in self.body:
            continue
    
    def add_block(self) -> None:
        self.add_block = True

class food:
    def __init__(self, game_size:Vector2) -> None:
        self.randomize()
        self.game_size = game_size

    def randomize(self) -> None:
        self.pos = Vector2(
            random.randint(0, self.game_size.x - 1), 
            random.randint(0, self.game_size.y - 1)
        )

class game:
    def __init__(self) -> None:
        start_body = [Vector2(0, 0), Vector2(0, 1), Vector2(0, 1)]
        self.snake = snake(start_body, Vector2(0, 1))
        self.size = Vector2(15, 10)
        self.tile_size = 10
    
    def update(self) -> None:
        self.snake.move()

    def render(self) -> None:
        self.snake.render()
        self.food.render

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
games:list[game] = [game()]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for game in games:
        game.update()
        game.render()

    screen.fill((0, 200, 100))
    pygame.display.update()
    clock.tick(60)