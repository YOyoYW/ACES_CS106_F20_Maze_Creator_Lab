import pygame
import time
import random

## Direction Constants
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

## Color Constants
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
CYAN   = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE  = (255, 255, 255)

class Maze:
    def __init__(self, width=20, height=20, tile_size=20, border_width=20):
        ## Maze grid width
        self.width        = width
        
        ## Maze grid height
        self.height       = height

        ## The size of one grid square
        self.tile_size    = tile_size

        ## The amount of space between the edge of the maze and the edge of the screen
        self.border_width = border_width

        pygame.init()

        ## Animate maze creation if True, skip animation if False
        self.animate= True

        pwidth = (self.width * tile_size) + (2 * border_width)
        pheight = (self.height * tile_size) + (2 * border_width)

        ## TODO: Using pwidth and pheight, create a pygame screen
        ## http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/
        ## Just fill in the blank, don't add any other lines.
        self.screen = pygame.display.set_mode((pwidth, pheight))

        ## TODO: Change the background color if you want
        self.screen.fill(CYAN)

        ## TODO: Change the window title
        pygame.display.set_caption("Maze Creator")

    ## Build an empty grid
    def build_grid(self):
        global screen
        s = self.tile_size
        b = self.border_width

        x = b
        y = b

        ## TODO: Using self.width and self.height, fill in the blanks
        for i in range(0, self.width):
            for j in range(0, self.height):
                ## Draw 4 lines to make a square with (x, y) as the top-right corner.
                pygame.draw.line(self.screen, BLACK, [x, y], [x + s, y])
                pygame.draw.line(slf.screen, BLACK, [x + s, y], [x + s, y + s])
                pygame.draw.line(self.screen, BLACK, [x + s, y + s], [x, y + s])
                pygame.draw.line(self.screen, BLACK, [x, y + s], [x, y])
                x += s

            x = b
            y += s
                
        

        if self.animate == True:
            pygame.display.update()


    ## Push down wall at (x, y) in direction
    def push(self, x, y, direction):
        s = self.tile_size
        b = self.border_width

        px = (x * s) + b + (direction[0] * s) + 1
        py = (y * s) + b + (direction[1] * s) + 1

    

        if direction in (UP, DOWN):
            pygame.draw.rect(self.screen, WHITE, (px, py, s - 1, (2 * s) - 1), 0)
        else:
            pygame.draw.rect(self.screen, WHITE, (px, py, (2 * s) - 1, s - 1), 0)

        
        pygame.display.update()

    ## Draw a colored square at x, y
    def draw_tile(self, x, y, color):
        s = self.tile_size
        b = self.border_width
        
        px = (x * s) + b + 1
        py = (y * s) + b + 1
        
        pygame.draw.rect(self.screen, color, (px, py, s - 1, s - 1), 0)

        
        pygame.display.update()

    ## Generate a maze using DFS (Depth First Search)
    def make_maze(self, start_x, start_y, animate=True):
        ## Set the animate flag
        self.animate = animate

        ## TODO: One line, make the grid
        self.build_grid()

        ## If we are animating, make the program wait 1 second before continuing
        if animate == True:
            time.sleep(1)
            ## TODO: One line, make the program sleep for 1 second
            ## https://www.tutorialspoint.com/python/time_sleep.htm
        
        
        
        clock = pygame.time.Clock()

        fps = 0

        ## TODO: Two lines
        ## If we are animating, set FPS to 20
        if animate == True:
            fps = 20
        ## Our special list that we use as a stack
        stack = list()

        ## A 2-Dimensional list that starts out all False
        ## When we visit a coordinate, we set it to true in visited
        visited = [[False for _ in range(self.height)] for _ in range(self.width)]

        ## We start at coordinates (x, y)
        x = start_x
        y = start_y
        
        ## TODO: One line, Add the coordinates to the stack as a tuple
        stack.append((x,y))

        ## Set the (x, y) coordinate of visited to True
        visited[x][y] = True

        ## Begin traveling around the grid
        ## Randomly pick a direction to travel and push down the wall
        ## Add the coordinate to the stack and mark it as visited
        ## If we reach a dead end, pop the last coordinates off the stack and go back

        ## TODO: We stop when we have reached ever tile in the grid
        ## How do we know that we have reached every tile in the grid?
        ## It has something to do with the stack.
        while len(stack) > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            clock.tick(fps)

            ## This will contain all the branches that determine which direction we can move.
            branches = list()

            ## Loop through all the directions
            for direction in (UP, DOWN, LEFT, RIGHT):

                ## TODO: Fill in the blanks
                ## (newx, newy) should be the coordinates after moving in "direction" from (x, y)
                ## This is the same move equation from Snake Project
                newx = x + direction[0]
                newy = y + direction[1]

                ## TODO: Check if newx is outisde the grid
                ## Is a negative coordinate in the grid?
                ## If my grid is 20 tiles wide, is (20, 0) still in the grid?
                if newx < 0 or newx >= self.width:
                    continue
                
                ## TODO: Check if newy is outisde the grid
                if newy < 0 or newy >= self.height:
                    continue

                ## TODO: If we have not visited (newx, newy) add the direction to the branch
                ## Remember the 'visited' variable
                if not visited[newx][newy]:
                    branches.append(direction)


            ## TODO: Check that we are not at a dead end
            ## How many branches does a dead end have?
            ## True == not a dead end, False == a dead end
            if len(branches) > 0:
                ## TODO: One line, pick a random direction from branch
                ## https://www.w3schools.com/python/module_random.asp
                ## HINT: It is one of the first 10 methods in the list
                rand_direction = random.choice(branches)

                ## TODO: One line, push down the wall in the direction
                self.push(x,y, rand_direction)

                ## Move the coordinates in rand_direction
                ## Again just the same move equation from Snake Project
                x += rand_direction[0]
                y += rand_direction[1]
                
                ## TODO: One line, now that we have just moved, mark our location as visited
                ## There is an example of this somewhere earlier in make_maze()
                visited[x][y] = True

                ## TODO: One line, add our current coordinate to the stack
                stack.append((x,y))

            ## We are at a dead end
            else:
                x, y = stack.pop()
                self.draw_tile(x, y, RED)
                time.sleep(0.1)
                self.draw_tile(x, y, BLUE)

                ## TODO: Pop the previous coordinate from the stack
                ## Set x and y to the old coordinate values
                x = coord[0]
                y = coord[0]

                ## When backtracking, show the tile we are popping by flashing it red
                ## We can do this by drawing a red square, and then drawing a white square quickly after
                
                ## TODO: One line, draw a red tile at (x, y)
                "write something here"
                
                clock.tick(fps)

                ## TODO: One line, draw a white tile at (x, y)
                "write something here"

        pygame.display.update()

    ## Save an image of the maze
    def save_maze(self, filename="maze.jpg"):
        pygame.image.save(self.screen, filename)


if __name__ == "__main__":
    pygame.init()

    ## TODO: One Line
    ## Instantiate a Maze object
    "write something here"

    ## TODO: One Line
    ## Create the maze
    maze = Maze()

    ## OPTIONAL: Save your maze as an image
    ## There is a function written that does this for you.
    

    ## Some stuff so that the window exits properly
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                break
            
