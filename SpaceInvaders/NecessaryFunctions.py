"""
@author lb809 on 12/21/2016
"""

def distanceBetweenTwoPoints(x1, y1, x2, y2):
    diffX = (x1 - x2) ** 2
    diffY = (y1 - y2) ** 2

    distance = (diffX + diffY) ** (0.5)

    return distance
