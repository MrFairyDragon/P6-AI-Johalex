import pygame

from GameState import GameState
from World import World
from AStar import AStar
from Player import Player


class GameLoop:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")
        self.world = World(11, 11)
        self.world.draw(screen)
        self.game_state = GameState.PLAY
        self.player = Player(0, 3)



        self.StartLoop()

    def StartLoop(self):
        while self.game_state == GameState.PLAY:
            # Event Cycle
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_state = GameState.QUIT
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    clicked_tile = self.world.get_clicked_tile(x, y)
                    a_star = AStar()
                    path = a_star.find_path(self.world.board, self.world.board[self.player.position[0]][self.player.position[1]], clicked_tile)
                    print(path)


                    # Make player walk there

            pygame.display.update()

            # Trigger resource spawn chance

            # Trigger AI update

            # Draw World

            # Draw Entities


if __name__ == '__main__':
    game = GameLoop()
