import os
import numpy as np
from PIL import Image

# declare variables
picNum = 0
fileNum = 0
counter = 0
d = {}

# list variable to store barcodes with image name as key and barcode as value
dictionary = []

# open file to write into
file = open("barcodes.txt", "w")

# runs a for loop to loop through all the class files in MNIST_DS
for i in range(10):
    # runs a for loop to loop through all the files inside each class file in MNIST_DS
    for j in range(10):
        # saves the image name into the dictionary with specific keys
        d[counter] = 'img_' + str(i) + str(j) + '.jpg'
        # adds 1 to counter
        counter = counter + 1

# runs for loop 100 times to loop through all the files in MNIST_DS
for i in range(100):
    image_name = d[picNum]
    image_path = os.path.join(os.getcwd(), 'MNIST_DS/' + str(fileNum), image_name)
    # print(image_path)
    image = Image.open(image_path)
    arr = np.asarray(image)

    # lists to store projections
    proj_1 = []
    proj_2 = []
    proj_3 = []
    proj_4 = []

    # Projection 1
    for r in range(28):
        proj_1.append(sum(arr[r]))  # sums all values in each row from top to bottom

    # Projection 2
    for r in range(26, -27, -1):
        proj_2.append(sum(np.diagonal(arr, r)))  # sums all values in each diagonal '\'
        # starting from top right to bottom left

    # Projection 3
    for r in range(27, -1, -1):
        proj_3.append(sum(arr[:, r]))  # sums all values in each column from right to left

    # Projection 4
    for r in range(-26, 27):
        proj_4.append(sum(np.fliplr(arr).diagonal(r)))  # sums all values in each diagonal '/'
        # starting from bottom right to top left

    # Gets the average of each projection
    def average(p):
        proj_average = round((sum(p) / len(p)), 0)
        return proj_average

    # Takes the projection list, gets the average, and compares the average
    # against each value in the list, and if the value in the list is greater than the average,
    # a 1 is placed in that spot, otherwise place 0
    def generate_c(p):
        c = []
        for item in p:
            if item > average(p):
                c.append(1)
            else:
                c.append(0)
        return c


    # Generate the code fragments for each projection
    c1 = generate_c(proj_1)
    c2 = generate_c(proj_2)
    c3 = generate_c(proj_3)
    c4 = generate_c(proj_4)

    # Add all code fragments together to get complete barcode for image
    barcode = c1 + c2 + c3 + c4

    # Print out each barcode with its image name
    print("\nbarcode for " + image_name)
    print(barcode)

    # Removes all commas and whitespace from barcode
    h = ""
    for i in range(162):
        h += str(barcode[i])

    # Adds each barcode into text file with corresponding image name
    print(image_name)
    file.write("barcode for " + str(image_name) + ": ")
    file.write(h)
    file.write("\n")
    file.write("\n")

    # Add all barcode to dictionary with key as image name and value as barcode
    nameAppend = {image_name: barcode}
    dictionary.append(nameAppend)

    picNum = picNum + 1

    if picNum % 10 == 0:
        fileNum = fileNum + 1

# print dictionary
print("\n")
print(dictionary)

# close text file
file.close()
