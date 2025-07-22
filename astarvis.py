import pygame
from queue import PriorityQueue

WIDTH = 600
ROWS = 20

win = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Grid Test")

gap = WIDTH//ROWS

class Node:
    def __init__(self,row,col,size):
        self.row = row
        self.col = col
        self.x = col*size
        self.y = row*size
        self.size = size
        self.color = (255,255,255)
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.size,self.size))
    
    def make_wall(self):
        self.color = (0,0,0)

    def reset(self):
        self.color = (255, 255, 255)  

    def make_start(self):
        self.color = (255, 165, 0)  

    def make_end(self):
        self.color = (64, 224, 208) 

    def is_start(self):
        return self.color == (255, 165, 0)

    def is_end(self):
        return self.color == (64, 224, 208)

    def update_neighbors(self,grid):
        self.neighbors = []

        if self.row<ROWS-1 and not grid[self.row+1][self.col].color == (0,0,0): #down
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row>0 and not grid[self.row-1][self.col].color == (0,0,0): #up
            self.neighbors.append(grid[self.row-1][self.col])

        if self.col<ROWS-1 and not grid[self.row][self.col+1].color == (0,0,0):
            self.neighbors.append(grid[self.row][self.col+1])

        if self.col>0 and not grid[self.row][self.col-1].color == (0,0,0):
            self.neighbors.append(grid[self.row][self.col-1])

    def get_pos(self):
        return self.row, self.col

def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.color = (128, 0, 128)
        draw()

def a_star(draw,grid,start,end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}

    g_score = {node : float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    f_score = {node : float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(),end.get_pos()) 

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from,end,draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score+h(neighbor.get_pos(),end.get_pos())

                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.color = (0,255,0)
        draw()

        if current != start:
            current.color(255,0,0)

    return False

            
def draw_grid(win,grid):

    for row in grid:
        for node in row:
            node.draw(win)

    for i in range(ROWS):
        pygame.draw.line(win,(200,200,200),(0, i * gap), (WIDTH, i * gap))
        pygame.draw.line(win,(200,200,200),(i * gap, 0), (i * gap, WIDTH))

def main():
    run = True
    start = None
    end = None

    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            node = Node(i, j, gap)
            grid[i].append(node)

    while run:
        win.fill((255,255,255))
        draw_grid(win, grid)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    a_star(lambda: draw_grid(win, grid), grid, start, end)

            if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = []
                    for i in range(ROWS):
                        grid.append([])
                        for j in range(ROWS):
                            node = Node(i, j, gap)
                            grid[i].append(node)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                row = y // gap
                col = x // gap
                node = grid[row][col]

                #print("start =", start, "end =", end)

                if event.button == 1:
                    if start is None and node != end:
                        start = node
                        start.make_start()
                        print("Start node at",row,col)
                    elif end is None and node != end:
                        end = node
                        end.make_end()
                        print("End node at",row,col)
                    elif node != start and node != end:
                        node.make_wall()
                        #print("Wall")
                
                elif event.button == 3:
                    if node == start:
                        start = None
                        print("Start Reset")
                    elif node == end:
                        end = None
                        print("End reset")
                    node.reset()

    pygame.quit()

main()