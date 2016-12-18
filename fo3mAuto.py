'''
Created on Dec 3, 2016

@author: oliver
'''
import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages

# various coordinates of objects in the game
GAME_REGION = () # (left, top, width, height) values coordinates of the entire game window

def main():
    """Runs the entire program. The FO3M game must be visible on the screen and the PLAY button visible."""
    logging.debug('Program Started. Press Ctrl-C to abort at any time.')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    getGameRegion()
    navigateStartGameMenu()
 

def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('images', filename)


def getGameRegion():
    """Obtains the region that the FO3M is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the PLAY button is visible)."""
    global GAME_REGION

    # identify the top-left corner
    logging.debug('Finding game region...')
    region = pyautogui.locateOnScreen(imPath('top_right_corner.png'))
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] + region[2] # left + width
    topRightY = region[1] # top
    GAME_REGION = (topRightX - 387, topRightY, 387, 619) # the game screen is always 640 x 480
    logging.debug('Game region found: %s' % (GAME_REGION,))
    
 

    
    
    
    
def navigateStartGameMenu():
    pos = pyautogui.locateCenterOnScreen(imPath('top_right_corner.png'), region=GAME_REGION)
    pyautogui.doubleClick(pos, duration=1)
    logging.debug('Clicked on Play button.')
    pyautogui.click(pos, duration=0.25)


if __name__ == '__main__':
    main()     
