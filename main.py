import pyautogui, os, pygetwindow, time, json


def impath(filename):
    return os.path.join('images', filename)

def itempath(filename):
    return os.path.join('images/items', filename)

def locate(item):
    rock = pyautogui.locateOnScreen(item)
    return rock

def region():
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

        storage_region = (top_left_corner[0], top_left_corner[1], top_right_corner[0] - top_left_corner[0],
                  bot_right_corner[1] - top_right_corner[1])

    except pyautogui.ImageNotFoundException:
        storage_region = 0

    return storage_region

def locate_all(path, region = region(), confidence=0.8, distance=10):
    distance = pow(distance, 2)
    elements = []
    for element in pyautogui.locateAllOnScreen(path, region=region, confidence=confidence):
        if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
            elements.append(element)
    return elements


if __name__ == '__main__':
    ITEM_DIRECTORY = os.getcwd() + '/images/items'

    bdo = pygetwindow.getWindowsWithTitle('BLACK DESERT - 516771')[0]
    bdo.activate()
    time.sleep(2)

    items = {}
    low_items = []
    for item in os.listdir(ITEM_DIRECTORY):
        try:
            amount = len(locate_all(itempath(item)))

        except pyautogui.ImageNotFoundException:
            amount = 0

        items[item[:-4]] = amount
        if amount < 4:
            low_items.append(item[:-4])

    with open('data.json', 'w') as f:
        json.dump(items, f, sort_keys = True, indent = 4,
               ensure_ascii = False)

    print(low_items)