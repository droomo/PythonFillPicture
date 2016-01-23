fileName = "10.jpg"

from PIL import Image
import random

def fill(x, y, thisColor, colorRgb):
        #BFS fill color block
        head = 0
        tail = 1

        wayx = []
        wayy = []

        wayx.append(x)
        wayy.append(y)

        while (head < tail):
                for i in range(0, 4):
                        tempx = wayx[head] + dx[i]
                        tempy = wayy[head] + dy[i]
                        
                        #if  (tempx >= 0) and (tempy >= 0) and (tempx < width) and (tempy < height):
                        if (imgArray[tempx, tempy] != (0, 0, 0)) and (flag[tempx][tempy] == 0):
                                imgArray[tempx, tempy] = colorRgb
                                flag[tempx][tempy] = thisColor
                                wayx.append(tempx)
                                wayy.append(tempy)
                                tail += 1
                head += 1
                
        return thisColor + 1

print "Loading image and initializing program."
img = Image.open(fileName)
imgArray = img.load()

width = img.size[0]
height = img.size[1]

flag = [[0 for i in range(height)] for j in range(width)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
        
color = 1

print "Load completed, initializing scaner."
for i in range(0, width):
        imgArray[i, 0] = (0,0,0)
        imgArray[i, height-1] = (0,0,0)
for j in range(0, height):
        imgArray[0, j] = (0,0,0)
        imgArray[width-1, j] = (0,0,0)

print "Initialize scaner completed, start fill block."
persent = (width - 1) / 100

for i in range(1, width-1):
        if (i % persent == 0):
                temp = i * 100 / width
                if temp % 5 == 0:
                        print "complete:", temp, "%"
        for j in range(1, height-1):
                if (imgArray[i, j] == (255,255,255)) and (flag[i][j] == 0):
                        colorRgb = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
                        color = fill(i, j, color, colorRgb)

print "Fill block completed, the number of color is", color, ", saving new image."

img.save('new_' + fileName)

print 'Complete!'
