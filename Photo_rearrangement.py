import cv2 as cv
import os
directory = '/Users/joshualei/PycharmProjects/2020-Fall detection robot/dataset/stand/angle03/'
directory2 = '/Users/joshualei/PycharmProjects/2020-Fall detection robot/dataset/stand/angle05/'

images_list = []
list = []
i = 0

def image_list():
    for filename in os.listdir(directory):
        index, name = filename.split("_")
        number, _, _ = name.split(".")
        images_list.append([index, number, filename])

def get_num(i):
    list = []
    for suitable_number in images_list:
        if suitable_number[0] == str(i):
            list.append(suitable_number)
    return list

def find_max_img(list):
    file_01 = list[0][2]
    number_01 = list[0][1]
    file_02 = list[1][2]
    number_02 = list[1][1]
    if number_01 > number_02:
        return file_01
    else:
        return file_02

while True:
    image_list()
    list = get_num(i)
    image_name = find_max_img(list)
    print(image_name)
    # os.remove(directory+image_name)
    image = cv.imread(directory+image_name)
    cv.imshow('image', image)
    cv.waitKey(1)
    cv.imwrite(directory2+image_name, image)
    i = i + 1



