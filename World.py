import math

from Tile import Tile
import random
from TileList import TileList
import numpy as np


class World:
    def __init__(self, sizeX, sizeY):
        self.board = np.ndarray(shape=(sizeX, sizeY), dtype=Tile)
        for i in range(sizeX):
            for j in range(sizeY):
                type = random.choice(list(TileList))
                if j % 2 == 0:
                    self.board[i][j] = Tile(type, i*48, j*40, i, j)
                else:
                    self.board[i][j] = Tile(type, i*48+24, j*40, i, j)

    def draw(self, screen):
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i][j].draw(screen)

    def update_neighbours(self):
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i][j].update_neighbours(self.board)

    def get_clicked_tile(self, x, y):
        image_clicked = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                img_rect = self.board[i][j].get_rect()
                if img_rect.collidepoint(x, y):
                    image_clicked.append(self.board[i][j])
        if image_clicked:
            first_center_pos = image_clicked[0].get_center_pos()
            distance = math.dist(first_center_pos, (x, y))
            tile = image_clicked[0]
            for i in range(len(image_clicked)):
                center_pos = image_clicked[i].get_center_pos()
                if distance > math.dist(center_pos, (x, y)):
                    distance = math.dist(center_pos, (x, y))
                    tile = image_clicked[i]
            return tile
        else:
            return None



