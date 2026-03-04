import pyautogui, os, pygetwindow, pyscreeze, time


def impath(filename):
    return os.path.join('images', filename)

def locate(item):
    rock = pyautogui.locateOnScreen(item)
    return rock


if __name__ == '__main__':
    IMG_DIRECTORY = os.getcwd()+'/images'

    win = pygetwindow.getWindowsWithTitle('BLACK DESERT - 516771')[0]
    win.activate()
    time.sleep(2)

    try:
        top_left = pyautogui.locateOnScreen(impath('top_left.png'), confidence=0.8)
        top_right = pyautogui.locateOnScreen(impath('top_right.png'), confidence=0.8)
        bot_left = pyautogui.locateOnScreen(impath('bot_left.png'), confidence=0.8)

        # Get absolute coordinates for top left corner of storage inventory
        top_left_corner = (top_left[0] + top_left[2], top_left[1] + top_left[3])

        # Get absolute coordinates for top right corner of storage inventory
        top_right_corner = (top_right[0], top_right[1] + top_right[3])

        # Get absolute coordinates for bottom left corner of storage inventory
        bot_left_corner = (bot_left[0], bot_left[1])

        # Get absolute coordinates for bottom right corner of storage inventory
        bot_right_corner = (top_right_corner[0], bot_left_corner[1])

    except pyautogui.ImageNotFoundException:
        print('Image not found')

    breakpoint()
    # Average dimensions of an item = 33pt x 33pt
    # for image in os.listdir(IMG_DIRECTORY):
    #     try:
    #         location = pyautogui.locateOnScreen(impath('potion.png'), region=[bot_right_x, bot_right_y, 34, 34], confidence=0.8)
    #         print(image)
    #
    #     except pyautogui.ImageNotFoundException:
    #         print('Image not found')
