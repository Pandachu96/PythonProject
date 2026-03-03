import pyautogui, os, pygetwindow, pyscreeze, time


def impath(filename):
    return os.path.join('images', filename)

def locate(item):
    rock = pyautogui.locateOnScreen(item)
    return rock


if __name__ == '__main__':
    # coords = 1216, 338, 1558, 612
    # REGION = [1216, 338, 342, 274]
    IMG_DIRECTORY = r'C:\Users\yangz\PycharmProjects\PythonProject\images'

    win = pygetwindow.getWindowsWithTitle('BLACK DESERT - 516771')[0]
    win.activate()
    time.sleep(2)

    top_left = pyautogui.locateOnScreen(impath('top_left.png'), confidence=0.8)

    # Get absolute coordinates for top left corner of first item: (x, y) = (bot_right_x, bot_right_y)
    bot_right_x = top_left[0] + top_left[2]
    bot_right_y = top_left[1] + top_left[3]

    # Average dimensions of an item = 33pt x 33pt

    # for image in os.listdir(IMG_DIRECTORY):
    #     location = list(pyautogui.locateAllOnScreen(impath(image), confidence=0.96, grayscale=True, region=REGION))
    #     print(image, len(location))

