import pygame
import random
pygame.init()

WIDTH = 600
ROWS = 20
gap = WIDTH // ROWS

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake")

class Node:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.x = col * size
        self.y = row * size
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(win, (211, 211, 211), (self.x, self.y, self.size, self.size), 1)

class Snake:
    def __init__(self, row, col, size):
        self.body = [(row, col)]
        self.size = size
    
    def Sdraw(self, win):
        for (row, col) in self.body:
            x = col * self.size
            y = row * self.size
            pygame.draw.rect(win, (0, 255, 0), (x, y, self.size, self.size))
    
    def move(self,dx,dy,food_pos):
        head_row,head_col = self.body[0]
        new_head = (head_row+dy, head_col+dx)
        self.body.insert(0,new_head)

        if new_head == food_pos:
            return True
        else: 
            self.body.pop()
            return False

def draw_grid(win, grid):
    for row in grid:
        for node in row:
            node.draw(win)
def main():
    clock = pygame.time.Clock()
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            grid[i].append(Node(i, j, gap))

    snake = Snake(10, 10, gap)
    food_pos = (random.randint(0,ROWS-1),random.randint(0,ROWS-1))
    
    run = True
    dx, dy = 1, 0 

    while run:
        win.fill((255, 255, 255))
        draw_grid(win, grid)
        snake.Sdraw(win)

        fx,fy = food_pos[1]*gap,food_pos[0]*gap
        pygame.draw.rect(win, (255, 0, 0), (fx, fy, gap, gap))

        ate_food = snake.move(dx, dy, food_pos)

        head = snake.body[0]
        print("Snake Body:", snake.body)

        if head in snake.body[1:]:
            print("GAME OVAAAA: Snake HIT itself!! GG")
            run = False

        if ate_food:
            while True:
                food_pos = (random.randint(0, ROWS - 1), random.randint(0, ROWS - 1))
                if food_pos not in snake.body:
                    break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dx,dy = 0,-1
                if event.key == pygame.K_a:
                    dx,dy = -1,0 
                if event.key == pygame.K_s:
                    dx,dy = 0,1
                if event.key == pygame.K_d:
                    dx,dy = 1,0
        clock.tick(10)
    pygame.quit()

main()
