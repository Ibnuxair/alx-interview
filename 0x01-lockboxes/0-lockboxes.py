#!/usr/bin/python3

""" canUnlockAll function """


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    canUnlockAll = False
    keys = {0: True}
    number_boxes = len(boxes)
    while(True):
        number_keys = len(keys)
        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < number_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > number_keys):
            break

    if number_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
