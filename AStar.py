from queue import PriorityQueue


def make_path(current, parent):
    path = []
    while current in parent:
        path.append(current)
        current = parent[current]
    return path


def calc_h_score(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


class AStar:

    def find_path(self, board, start, end):
        counter = 0
        queue = PriorityQueue()
        queue.put((0, counter, start))
        parent = {}
        g_score = {Tile: float("inf") for row in board for Tile in row}
        g_score[start] = 0
        f_score = {Tile: float("inf") for row in board for Tile in row}
        f_score[start] = calc_h_score(start.worldPosition, end.worldPosition)
        tiles_needs_checking = {start}
        while tiles_needs_checking:
            current = queue.get()[2]
            tiles_needs_checking.remove(current)
            if current == end:
                return make_path(current, parent)
            for neighbour in current.neighbors:
                print(neighbour)
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbour]:
                    parent[neighbour] = current
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_g_score + calc_h_score(neighbour.worldPosition, end.worldPosition)

                    if neighbour not in tiles_needs_checking:
                        counter += 1
                        queue.put((f_score[neighbour], counter, neighbour))
                        tiles_needs_checking.add(neighbour)
        return False
