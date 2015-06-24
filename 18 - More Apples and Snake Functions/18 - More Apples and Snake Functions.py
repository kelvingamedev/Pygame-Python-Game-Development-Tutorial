# Libaries import

import pygame
import time
import random
#==============================================================================
# Functions

# Show a message on screen
def MessageToScreen(gameDisplay, textPos,msg, color):

    # Type of font (ex: "arial", "comicsansms", "None")
    typeFont = None

    # Size of the font
    sizeFont = 25

    # Standard font to screen output
    FONT = pygame.font.SysFont(typeFont, sizeFont)

    # Tells if the text will be smooth borders or not
    ANTIALIAS = True

    # Put the text on a new surface (PyGame not provides a way to do that in a existing surface)
    screenText = FONT.render(msg, ANTIALIAS, color)

    # Put the surface screenText on the gameDisplay surface 
    gameDisplay.blit(screenText, textPos)

     # Render the text on screen
    pygame.display.update()

# Draw a snake
def DrawSnake(surface, color, arraySnake):

    pygame.draw.rect(surface, color, arraySnake)
    

# Primary function
def Main():

    # Initialize PyGame (return sucessful inicialization or not)
    pygame.init()

    # Define some colors (RGB)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0, 155, 0)

    # The defined size of the screen
    SCREEN_WIDTH = 800   
    SCREEN_HEIGHT = 600
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Camera view for the player see the game
    gameDisplay = pygame.display.set_mode(SCREEN_SIZE) # BOTTOM NOTE 1

    # Title of the window representing the name of the game
    GAME_NAME = "Slither"
    
    # Set the title of window
    pygame.display.set_caption(GAME_NAME)

    # Tells the the game will not quit or finish by now
    gameLoop = True

    # Tells to the game receive actions until the end of the game
    gameOver = False

    # Size of the blocks of the game
    sizeBlocks = {'x': 10, 'y': 10}

    # Coordinates to put text on screen
    textScreen = (SCREEN_WIDTH / 2 ,  SCREEN_HEIGHT / 2)

    # Receive values to exchange the Snake position
    changePos = {'x': 0, 'y': 0} 

    # Tells how much the snake position will change
    BLOCK_CHANGE = 10

    # Tells how many frames the computer will show for second
    FPS = 15

    # Receive a clock to control Frames per second
    clock = pygame.time.Clock()

    # The size of the apple puts limits in the last possible and random position on screen
    SCREEN_LIMIT = {'x': SCREEN_WIDTH - sizeBlocks['x'], 'y': SCREEN_HEIGHT - sizeBlocks['y'] }

    # Generate an random x and y axis positions
    randomX = random.randrange(0, SCREEN_LIMIT['x'], sizeBlocks['x'])
    randomY = random.randrange(0, SCREEN_LIMIT['y'], sizeBlocks['y'])

    # While in the game loop
    while gameLoop == True:

        # Put the snake in the inital position
        posSnake = {'x': SCREEN_WIDTH / 2, 'y': SCREEN_HEIGHT / 2}

        # Create an apple in a random position
        posApple = {'x': randomX, 'y': randomY}

        # While the game not over...
        while gameOver == False:

            # Check the events that are hapenning in the game
            for event in pygame.event.get():

                # Print they in console
                print(event)

                # If an event correspond to the exit or quit of PyGame
                if event.type == pygame.QUIT:

                    # Change the loop variable to go out of loop
                    gameExit = True

                # If the player press some key...
                elif event.type == pygame.KEYDOWN:

                    # If the player press the left key
                    if event.key == pygame.K_LEFT:

                        # Make the snake go left on screen
                        changePos['x'] = -BLOCK_CHANGE
                        changePos['y'] = 0

                    # If the player press the left key
                    elif event.key == pygame.K_RIGHT:

                        # Make the snake go right on screen
                        changePos['x'] = BLOCK_CHANGE
                        changePos['y'] = 0

                    elif event.key == pygame.K_UP:

                        # Make the snake go up on screen
                        changePos['y'] = -BLOCK_CHANGE
                        changePos['x'] = 0

                    elif event.key == pygame.K_DOWN:

                        # Make the snake go down on screen
                        changePos['y'] = BLOCK_CHANGE
                        changePos['x'] = 0

            # Change the snake position
            posSnake['x'] += changePos['x']
            posSnake['y'] += changePos['y']

            # Clean the screen 
            gameDisplay.fill(WHITE)

            # Snake array to the draw function
            arraySnake = (posSnake['x'], posSnake['y'], sizeBlocks['x'], sizeBlocks['y'])

            # Apple array to the draw function
            arrayApple = (posApple['x'], posApple['y'],sizeBlocks['x'], sizeBlocks['y'])

            # Draw the snake on screen
            DrawSnake(gameDisplay, GREEN, arraySnake)

            # Draw the Apple
            pygame.draw.rect(gameDisplay, RED, arrayApple)

            # Render on screen
            pygame.display.update()

            # If the snake position is same as apple 
            if posSnake['x'] == posApple['x'] and posSnake['y'] == posApple['y']:

                # Snake eat the apple, so...

                # Generate an random x and y axis positions
                randomX = random.randrange(0, SCREEN_LIMIT['x'], sizeBlocks['x'])
                randomY = random.randrange(0, SCREEN_LIMIT['y'], sizeBlocks['y'])

                # Create a new apple in a random position
                posApple = {'x': randomX, 'y': randomY}

                # Create an apple in a random position
                posApple = {'x': randomX, 'y': randomY}

            # Or if the snake overpass the limits of screen # BOTTOM NOTE 3
            elif posSnake['x'] < 0 or posSnake['x'] >= SCREEN_WIDTH or posSnake['y'] < 0 or posSnake['y'] >= SCREEN_HEIGHT:

                # End of the game
                gameOver = True

            # Control the update with Frames per second
            clock.tick(FPS) # BOTTOM NOTE 2

        # Clear the screen
        gameDisplay.fill(WHITE)
        
        # Output game over message
        MessageToScreen(gameDisplay, textScreen, "GAME OVER! Try Again? (y / n)", RED)

        # Confirm if the player answered above question or not
        playerAnswer = False

        # While player not answer the question...
        while playerAnswer == False:

            # Check for player answer
            for event in pygame.event.get():

                # Print the events in console
                print(event)

                # If the event correspond a press of a key...
                if event.type == pygame.KEYDOWN:                     
                
                    # If the player pressed the 'y' button
                    if event.key == pygame.K_y:

                        # Restart the game loop
                        gameOver = False
                        playerAnswer = True

                    # If the player pressed the 'n' button
                    elif event.key == pygame.K_n:

                        # Turn the variable value to go out the loop (end of the game)
                        gameLoop = False
                        playerAnswer = True
          
    # Unintilize the modules that have previously initialized 
    pygame.quit()

    # Quit the surface (End of the program)
    quit()
    
#================================================================================
# Game execution
Main()

#================================================================================
# BOTTOM NOTES
"""
1 - pygame.display.setmode returns a surface that is, nothing more than a
a blank surface to draw things

2- Avoide change the Frames per Second to turn the difficulty or speed of your game,
because change it cause more processing than just change the coordinates or other
variables

3 - This is be impossible if the first condition is true, because the position of the apple
can be only a valid position on the screen, and not off it

"""