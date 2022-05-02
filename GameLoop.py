import pygame

from GameState import GameState
from World import World
from AStar import AStar
from Player import Player


class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((580, 480))
        pygame.display.set_caption("Game")
        self.world = World(11, 11)
        self.world.update_neighbours()
        self.world.draw(self.screen)
        self.game_state = GameState.PLAY
        self.player = Player(0, 3)
        self.player.draw(self.screen)
        self.path = False
        self.pathStepCounter = 0
        self.pathTimer = 0
        self.pathCounter = 100

        self.StartLoop()

    def StartLoop(self):
        while self.game_state == GameState.PLAY:
            # Event Cycle
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_state = GameState.QUIT
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and self.path is False:
                    x, y = event.pos
                    clicked_tile = self.world.get_clicked_tile(x, y)
                    a_star = AStar()
                    self.path = a_star.find_path(self.world.board, self.world.board[self.player.world_position[0]][
                        self.player.world_position[1]], clicked_tile)
                    if self.path is not False:
                        self.path.reverse()

            # Make player walk if they have a destination
            if self.path is not False:
                self.pathCounter = self.pathCounter - 1
                if self.pathCounter <= 0:
                    self.player.move(self.path[self.pathStepCounter].worldPosition)
                    self.pathStepCounter += 1
                    self.pathCounter = 100
                    if self.pathStepCounter == len(self.path):
                        self.path = False
                        self.pathStepCounter = 0
            pygame.display.update()
            # Trigger resource spawn chance

            # Trigger AI update

            # Draw World
            self.screen.fill((0, 0, 0))
            self.world.draw(self.screen)
            self.player.draw(self.screen)
            # Draw Entities


if __name__ == '__main__':
    game = GameLoop()
