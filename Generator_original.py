import os, random
import cv2, argparse
import numpy as np
import sys

sys.path.append(os.getcwd())
sys.path.append('.')

def random_bright(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img = np.array(img, dtype=np.float64)
    random_bright = .5 + np.random.uniform()
    img[:, :, 2] = img[:, :, 2] * random_bright
    img[:, :, 2][img[:, :, 2] > 255] = 255
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img

class ImageGenerator:
    def __init__(self, save_path):
        self.save_path = save_path
        # Plate
        self.plate = cv2.imread("plate.jpg")
        self.plate2 = cv2.imread("plate_y.jpg")
        self.plate3 = cv2.imread("plate_g.jpg")

        # loading Number
        file_path = "./num/"


        file_list = os.listdir(file_path)
        self.Number = list()
        self.number_list = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number.append(img)
            self.number_list.append(file[0:-4])

        # loading Char
        file_path = "./char1/"
        file_list = os.listdir(file_path)
        self.char_list = list()
        self.Char1 = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1.append(img)
            self.char_list.append(file[0:-4])

        # loading Number ====================  yellow-two-line  ==========================
        file_path = "./num_y/"
        file_list = os.listdir(file_path)
        self.Number_y = list()
        self.number_list_y = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number_y.append(img)
            self.number_list_y.append(file[0:-4])

        # loading Char
        file_path = "./char1_y/"
        file_list = os.listdir(file_path)
        self.char_list_y = list()
        self.Char1_y = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1_y.append(img)
            self.char_list_y.append(file[0:-4])

        # loading Resion
        file_path = "./region_y/"
        file_list = os.listdir(file_path)
        self.Resion_y = list()
        self.resion_list_y = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Resion_y.append(img)
            self.resion_list_y.append(file[0:-4])
        #=========================================================================

        # loading Number ====================  green-two-line  ==========================
        file_path = "./num_g/"
        file_list = os.listdir(file_path)
        self.Number_g = list()
        self.number_list_g = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number_g.append(img)
            self.number_list_g.append(file[0:-4])

        # loading Char
        file_path = "./char1_g/"
        file_list = os.listdir(file_path)
        self.char_list_g = list()
        self.Char1_g = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1_g.append(img)
            self.char_list_g.append(file[0:-4])

        # loading Resion
        file_path = "./region_g/"
        file_list = os.listdir(file_path)
        self.Resion_g = list()
        self.resion_list_g = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Resion_g.append(img)
            self.resion_list_g.append(file[0:-4])
        #=========================================================================


    def Type_1(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate, (520, 110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (520, 110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_2(self, num, save=False):
        number = [cv2.resize(number, (45, 83)) for number in self.Number]
        char = [cv2.resize(char1, (49, 70)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate, (355, 155))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (355, 155))
            label = "Z"
            row, col = 46, 10  # row + 83, col + 56

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 3
            label += self.char_list[i%37]
            Plate[row + 12:row + 82, col + 2:col + 49 + 2, :] = char[i%37]
            col += 49 + 2

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col + 2:col + 45 + 2, :] = number[rand_int]
            col += 45 + 2

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_3(self, num, save=False):
        number1 = [cv2.resize(number, (44, 60)) for number in self.Number_y]
        number2 = [cv2.resize(number, (64, 90)) for number in self.Number_y]
        resion = [cv2.resize(resion, (88, 60)) for resion in self.Resion_y]
        char = [cv2.resize(char1, (64, 62)) for char1 in self.Char1_y]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate2, (336, 170))

            label = str()
            # row -> y , col -> x
            row, col = 8, 76

            # resion
            label += self.resion_list_y[i % 16]
            Plate[row:row + 60, col:col + 88, :] = resion[i % 16]
            col += 88 + 8

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]
            col += 44

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]

            row, col = 72, 8

            # character 3
            label += self.char_list_y[i % 37]
            Plate[row:row + 62, col:col + 64, :] = char[i % 37]
            col += 64

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_4(self, num, save=False):
        number1 = [cv2.resize(number, (44, 60)) for number in self.Number_g]
        number2 = [cv2.resize(number, (64, 90)) for number in self.Number_g]
        resion = [cv2.resize(resion, (88, 60)) for resion in self.Resion_g]
        char = [cv2.resize(char1, (64, 62)) for char1 in self.Char1_g]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate3, (336, 170))

            label = str()
            # row -> y , col -> x
            row, col = 8, 76

            # resion
            label += self.resion_list_g[i % 16]
            Plate[row:row + 60, col:col + 88, :] = resion[i % 16]
            col += 88 + 8

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]
            col += 44

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]

            row, col = 72, 8

            # character 3
            label += self.char_list_g[i % 37]
            Plate[row:row + 62, col:col + 64, :] = char[i % 37]
            col += 64

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_5(self, num, save=False):
        number1 = [cv2.resize(number, (60, 65)) for number in self.Number_g]
        number2 = [cv2.resize(number, (80, 90)) for number in self.Number_g]
        char = [cv2.resize(char1, (60, 65)) for char1 in self.Char1_g]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate3, (336, 170))
            random_width, random_height = 336, 170
            label = "Z"

            # row -> y , col -> x
            row, col = 8, 78

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 65, col:col + 60, :] = number1[rand_int]
            col += 60

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 65, col:col + 60, :] = number1[rand_int]
            col += 60

            # character 3
            label += self.char_list_g[i%37]
            Plate[row:row + 65, col:col + 60, :] = char[i%37]
            row, col = 75, 8

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80


            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]

            Plate = random_bright(Plate)

            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
