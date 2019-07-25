def colorPercentage(img):
    import cv2
    import numpy as np 

    imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    blue = [0, 15]
    cyan = [16, 33]
    green = [34, 82]
    yellow = [83, 96]
    orange = [97, 112]
    red = [113, 137]
    magenta = [138, 179]

    colors = [blue, cyan, green, yellow, orange, red, magenta]
    colorStrings = ["blue", "cyan", "green", "yellow", "orange", "red", "magenta"]

    cp = {}
    ranges = []  
    
    for i in range(len(colors)):
        ranges.append([np.array([colors[i][0], 20, 40]), np.array([colors[i][1], 255, 255])])
        mask = cv2.inRange(imgHSV, ranges[i][0], ranges[i][1])
        percentage = round(np.sum(mask == 255) / (mask.shape[0] * mask.shape[1]) * 100)
        cp[colorStrings[i]] = percentage

    whiteRange = [np.array([0, 0, 240]), np.array([255, 20, 255])]
    blackRange = [np.array([0, 0, 0]), np.array([255, 255, 39])]
    
    bw = [whiteRange, blackRange]
    bwStrings = ["white", "black"]

    '''# visual masking
    mask = cv2.inRange(imgHSV, np.array([120, 20, 150]), np.array([179, 200, 255]))
    kernelOpen = np.ones((5,5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    cv2.imwrite('mask.jpg', mask)
    conts, h = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contImg = cv2.drawContours(img, conts, -1, (0, 0, 0), 3)
    cv2.imwrite("contImg.jpg", contImg)'''


    for i in range(len(bw)):

        ranges.append(bw[i])
        mask = cv2.inRange(imgHSV, ranges[i+7][0], ranges[i+7][1])
        percentage = round(np.sum(mask == 255) / (mask.shape[0] * mask.shape[1]) * 100)
        print(bwStrings[i], percentage)
        cp[bwStrings[i]] = percentage

    return cp