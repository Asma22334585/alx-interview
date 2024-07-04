#!/usr/bin/python3
"""BOXES"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened."""
    visit = {0}
    queue = [boxes[0]]
    
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in visit and key < len(boxes):
                visit.add(key)
                queue.append(boxes[key])
    return len(visit) == len(boxes)
