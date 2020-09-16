import cv2 as cv
import os
import time
import pyttsx3
category, amount = input("Input your category and photos amount").split()
folder_location = '/Users/joshualei/PycharmProjects/2020-Fall detection robot/dataset/stand/' + str(category)
cap = cv.VideoCapture(1)
print(category + ":" + amount)
if not os.path.exists(folder_location):os.mkdir(folder_location)
i = 0
engine = pyttsx3.init()
engine.startLoop(False)
for i in range(int(amount)):
    ret, frame = cap.read()
    print(frame.shape)
    frame = cv.resize(frame, (1080, 640))
    print(frame.shape)
    cv.imshow('frame', frame)
    cv.imwrite(folder_location + '/' + str(i) + '_' + str(time.time()) + '.jpg', frame)
    print(i)
    engine.say(str(i))
    engine.iterate()
    time.sleep(1)
    key_code = cv.waitKey(1)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
engine.endLoop()
cv.destroyAllWindows()