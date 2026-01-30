import pygame
import math
from queue import PriorityQueue

# Setup
WIDTH = 600
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Dijkstra's Algorithm Visualizer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)      # Visited (Closed)
GREEN = (0, 255, 0)    # Queued (Open)
BLUE = (0, 0, 255)     # Final Path
ORANGE = (255, 165, 0)  # Start
TURQUOISE = (64, 224, 208)  # End


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row, self.col = row, col
        self.x, self.y = row * width, col * width
        self.color = WHITE
        self.neighbors = []
        self.width, self.total_rows = width, total_rows

    def get_pos(self): return self.row, self.col
    def is_barrier(self): return self.color == BLACK
    def reset(self): self.color = WHITE
    def make_visited(self): self.color = RED
    def make_queued(self): self.color = GREEN
    def make_barrier(self): self.color = BLACK
    def make_end(self): self.color = TURQUOISE
    def make_path(self): self.color = BLUE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # Check adjacent nodes (Up, Down, Left, Right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < self.total_rows and 0 <= c < self.total_rows:
                if not grid[r][c].is_barrier():
                    self.neighbors.append(grid[r][c])


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        if current.color != ORANGE:  # Don't paint over start
            current.make_path()
        draw()


def dijkstra(draw, grid, start, end):
    count = 0
    pq = PriorityQueue()
    pq.put((0, count, start))
    came_from = {}

    # Distance from start to all nodes is infinity initially
    distance = {node: float("inf") for row in grid for node in row}
    distance[start] = 0

    visited_hash = {start}

    while not pq.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = pq.get()[2]
        visited_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_dist = distance[current] + 1  # Assuming edge weight of 1

            if temp_dist < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = temp_dist
                if neighbor not in visited_hash:
                    count += 1
                    pq.put((distance[neighbor], count, neighbor))
                    visited_hash.add(neighbor)
                    if neighbor != end:
                        neighbor.make_queued()

        draw()
        if current != start:
            current.make_visited()
    return False


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([Node(i, j, gap, rows) for j in range(rows)])
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GRAY, (i * gap, 0), (i * gap, width))


def draw_all(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def main():
    grid = make_grid(ROWS, WIDTH)
    start, end = None, None
    run = True

    while run:
        draw_all(WIN, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left Click
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // (WIDTH // ROWS), pos[1] // (WIDTH // ROWS)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.color = ORANGE
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right Click
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // (WIDTH // ROWS), pos[1] // (WIDTH // ROWS)
                grid[row][col].reset()
                if grid[row][col] == start:
                    start = None
                if grid[row][col] == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    dijkstra(lambda: draw_all(
                        WIN, grid, ROWS, WIDTH), grid, start, end)
                if event.key == pygame.K_c:
                    start, end = None, None
                    grid = make_grid(ROWS, WIDTH)

    pygame.quit()


main()
