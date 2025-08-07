import cv2
import numpy as np
import time, random

img = cv2.imread("assets/americanis_2.png", 1)
template = cv2.imread("assets/americanis template 2.png", 0)

img = cv2.resize(img, (0, 0), fx=4, fy=4)
template = cv2.resize(template, (0, 0), fx=4, fy=4)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = template.shape

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED) # returns array where higher value = better match

threshold = 0.85
locations = np.where(result >= threshold) # returns array of indexes where the value in result is greater than threshold
#print(len(locations[0]))

matches = [(0, 0)]
circles = []

# locations is a tuple w/ 2 corresponding arrays, one with x values and one with y values
for i in range(len(locations[0])):
    x, y = locations[1][i], locations[0][i]
    #print("coords:", x, y)

    for pt in matches:
        dist = cv2.norm(np.array(pt), np.array((x, y)))
        #print(dist)

        if dist <= 7:
            unique = False
            #print("duplicate:", pt)
            break
        else:
            unique = True
    
    if unique:
        matches.append((x, y))
        #print("APPENDED")

        center = (int(x+(w/2)), int(y+(h/2)))
        circles.append(center)
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(img, center, 7, (255, 255, 255), -1, cv2.LINE_AA)
        #cv2.putText(img, str(center), center, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
    
    #time.sleep(1)
    #print("")


for i in range(len(circles)):
    for j in range(i + 1, len(circles)):
        pt1 = np.array(circles[i])
        pt2 = np.array(circles[j])
        dist = cv2.norm(pt1, pt2)
        if (20 <= dist <= 100):
            b = random.randint(25, 255)
            g = random.randint(25, 255)
            r = random.randint(25, 255)

            midpoint = (int((pt1[0] + pt2[0]) / 2), int((pt1[1] + pt2[1]) / 2))

            cv2.line(img, pt1, pt2, (b, g, r), 1, cv2.LINE_AA)
            cv2.circle(img, midpoint, 2, (b, g, r), -1, cv2.LINE_AA)
            cv2.putText(img, str(round(dist/4, 2)), midpoint, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.4, (b, g, r), 1, cv2.LINE_AA)


print(len(matches))
cv2.imwrite("assets/template_result.png", img)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows