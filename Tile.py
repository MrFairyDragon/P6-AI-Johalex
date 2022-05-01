import pygame

from TileList import TileList


class Tile:
    def __init__(self, tileType, posX, posY, worldX, worldY):
        self.neighbors = []
        self.img = pygame.image.load(tileType.value)
        self.type = tileType
        self.position = (posX, posY)
        self.worldPosition = (worldX, worldY)

    def draw(self, screen):
        screen.blit(self.img, self.position)

    def update_type(self, tileType):
        self.type = tileType

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], 56, 56)

    def get_center_pos(self):
        return self.position[0]+28, self.position[1]+28

    def update_neighbours(self, board):
        self.neighbors = []
        if self.worldPosition[1] % 2 == 0:
            if self.worldPosition[1]+1 < board.shape[1]:
                if not board[self.worldPosition[0]][self.worldPosition[1]+1].type == TileList.WATER: #1 o'clock
                    self.neighbors.append(board[self.worldPosition[0]][self.worldPosition[1]+1])

            if self.worldPosition[0]+1 < board.shape[0]:
                if not board[self.worldPosition[0]+1][self.worldPosition[1]].type == TileList.WATER: #3 o'clock
                    self.neighbors.append(board[self.worldPosition[0]+1][self.worldPosition[1]])

            if self.worldPosition[1]-1 >= 0:
                if not board[self.worldPosition[0]][self.worldPosition[1]-1].type == TileList.WATER: #5 o'clock
                    self.neighbors.append(board[self.worldPosition[0]][self.worldPosition[1]-1])

            if self.worldPosition[0]-1 >= 0 and self.worldPosition[1]-1 >= 0:
                if not board[self.worldPosition[0]-1][self.worldPosition[1]-1].type == TileList.WATER: #7 o'clock
                    self.neighbors.append(board[self.worldPosition[0]-1][self.worldPosition[1]-1])

            if self.worldPosition[0]-1 >= 0:
                if not board[self.worldPosition[0]-1][self.worldPosition[1]].type == TileList.WATER: #9 o'clock
                    self.neighbors.append(board[self.worldPosition[0]-1][self.worldPosition[1]])

            if self.worldPosition[0]-1 >= 0 and self.worldPosition[1]+1 < board.shape[1]:
                if not board[self.worldPosition[0]-1][self.worldPosition[1]+1].type == TileList.WATER: #11 o'clock
                    self.neighbors.append(board[self.worldPosition[0]-1][self.worldPosition[1]+1])

        elif self.worldPosition[1] % 2 == 1:
            if self.worldPosition[0]+1 < board.shape[0] and self.worldPosition[1]+1 <= board.shape[1]:
                if not board[self.worldPosition[0]+1][self.worldPosition[1]+1].type == TileList.WATER: #1 o'clock
                    self.neighbors.append(board[self.worldPosition[0]+1][self.worldPosition[1]+1])

            if self.worldPosition[0]+1 < board.shape[0]:
                if not board[self.worldPosition[0]+1][self.worldPosition[1]].type == TileList.WATER: #3 o'clock
                    self.neighbors.append(board[self.worldPosition[0]+1][self.worldPosition[1]])

            if self.worldPosition[0] + 1 < board.shape[0] and self.worldPosition[1] - 1 >= 0:
                if not board[self.worldPosition[0]+1][self.worldPosition[1]-1].type == TileList.WATER: #5 o'clock
                    self.neighbors.append(board[self.worldPosition[0]+1][self.worldPosition[1]-1])

            if self.worldPosition[1]-1 >= 0:
                if not board[self.worldPosition[0]][self.worldPosition[1]-1].type == TileList.WATER: #7 o'clock
                    self.neighbors.append(board[self.worldPosition[0]][self.worldPosition[1]-1])

            if self.worldPosition[0]-1 >= 0:
                if not board[self.worldPosition[0]-1][self.worldPosition[1]].type == TileList.WATER: #9 o'clock
                    self.neighbors.append(board[self.worldPosition[0]-1][self.worldPosition[1]])

            if self.worldPosition[1]+1 < board.shape[1]:
                if not board[self.worldPosition[0]][self.worldPosition[1]+1].type == TileList.WATER: #11 o'clock
                    self.neighbors.append(board[self.worldPosition[0]][self.worldPosition[1]+1])
