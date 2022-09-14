# Function for the formula for hamming distance between the bit-strings of barcode
def hamming_distance(string_1, string_2):
    if len(string_1) == len(string_2):
        d = 0
        for c1, c2 in zip(string_1, string_2):
            # For any difference between the values of 2 barcodes increase the distance by 1
            if c1 != c2:
                d += 1

        return d
    else:
        return 0


# Retrieve barcodes list from the file
def get_barcodes_data_list(file):
    line = file.readline()
    split_list = []  # Get the barcode data list in an array

    while line:
        line = line.strip()  # Removes the leading and trailing characters and spaces
        split_data = line.split(' ')  # Splits a string into a list
        split_list.append(split_data)
        line = file.readline()
        line = file.readline()
    return split_list


# Function to find the distance comparing all possible combinations of 2 barcodes along the full length of each barcode
def find_distance(barcode_list, number):
    size_list_barcode = len(barcode_list) # Gets the length of each barcode
    str1 = barcode_list[int(number)][3]  # Gets the entire barcode as an integer
    distance_list = []  # Gets the distances in an array as a list

    for x in range(0, size_list_barcode):  # Iterates over every barcode starting from 0
        str2 = barcode_list[x][3] # Gets the barcode of the second string to compare with the first string
        res = hamming_distance(str1, str2) # hamming distance is stored in a varible
        distance_list.append(res)

    return distance_list  # Returns the distance list


# Checks to see whether the input image number is present in the barcode list
def check_input_number(list_barcode, number):
    check = 0
    for x in range(len(list_barcode)): # Iterates over the length of all images i.e. 100
        compare_data = list_barcode[x][2][4:6] # Checks for the image number by going through the syntax of each image
        if number == compare_data: # If the number entered is present in either of the image sytanx then it returns 1
            check = 1
            return check
        else:
            check = -1
    return check


# Function arranges the number of images within the same class digit
def arrange_image_data(image_data):
    image_syntax = image_data[:4]  # Gets the "img_" part from image barcode syntax
    image_number = int(image_data[4:6]) # Gets the image number from the image barcode syntax
    image_name = ''

    if 0 <= image_number <= 9:
        image_name = image_syntax + '00' + '.jpg'

    elif 9 < image_number <= 19:
        image_name = image_syntax + '01' + '.jpg'

    elif 19 < image_number <= 29:
        image_name = image_syntax + '02' + '.jpg'

    elif 29 < image_number <= 39:
        image_name = image_syntax + '03' + '.jpg'

    elif 39 < image_number <= 49:
        image_name = image_syntax + '04' + '.jpg'

    elif 49 < image_number <= 59:
        image_name = image_syntax + '05' + '.jpg'

    elif 59 < image_number <= 69:
        image_name = image_syntax + '06' + '.jpg'

    elif 69 < image_number <= 79:
        image_name = image_syntax + '07' + '.jpg'

    elif 79 < image_number <= 89:
        image_name = image_syntax + '08' + '.jpg'

    elif 89 < image_number <= 99:
        image_name = image_syntax + '09' + '.jpg'

    return image_name


# Function arranges the exact image number labelled as an x value here to differentiate from the above function created
# to arrange classes wihtin the range of 10's
def arrange_x_value(value):
    number = 0

    if 0 <= value <= 9:
        number = 0

    elif 9 < value <= 19:
        number = 1

    elif 19 < value <= 29:
        number = 2

    elif 29 < value <= 39:
        number = 3

    elif 39 < value <= 49:
        number = 4

    elif 49 < value <= 59:
        number = 5

    elif 59 < value <= 69:
        number = 6

    elif 69 < value <= 79:
        number = 7

    elif 79 < value <= 89:
        number = 8

    elif 89 < value <= 99:
        number = 9

    return number


# function to replace the  numbers (swaps the image being searched with 1000)
def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with
            if item == item_to_replace
            else item for item in list_to_replace]


file = open('barcodes.txt', 'r')  # Read The File (barcodes.txt)
List_barcode = get_barcodes_data_list(file)  # read the file and append the List

restart = True

while restart:
    number = input('Enter the Image Number that you want to compare from 00-99 : ')  # Get the image number from user
    print("\n")
    check_res = check_input_number(List_barcode, number)  # Check the Input Image number

    if check_res == 1:
        Distance_List = find_distance(List_barcode, number)  # Find the hamming distance
        Distance_List = replace_values(Distance_List, 0, 1000)  # Replace the 0 , 1000
        print('Hamming Distances between the barcodes of the Image Number entered and the rest of the Images : \n',
              Distance_List)  # Display all the Hamming Distances
        print("\n")
        minimum_hamming_distance = min(Distance_List)  # Find the minimum Number
        minimum_index = Distance_List.index(min(Distance_List))  # Find the minimum number Index
        Image_Data = List_barcode[minimum_index][2]  # Get The Image Data of minimum number
        actual_image = arrange_image_data(Image_Data)
        # Display the Data
        print('The most similar Image is : {} and the Hamming Distance of the Image is: {}'.format(Image_Data,
                                                                                        minimum_hamming_distance))
        print("\n")
    else:
        print('Please Enter Correct Number : ')

        print("\n")

    answer = input("If you would like to search another image, type 'Y'. OTHERWISE, type 'N' to get "
                   "the hit ratio results: ")
    print("\n")
    if answer == "N" or answer == "n":
        restart = False

# Find the Accuracy and hit ratio

Total_Images = 100
count = 0

for x in range(0, 100):

    Distance_Data = find_distance(List_barcode, x)  # Finds Distance
    Distance_Data = replace_values(Distance_Data, 0, 1000)  # Replaces the 0 , 1000
    minimum_hamming_distance = min(Distance_List)  # Finds the minimum Number
    Minimum_Data_Index = Distance_Data.index(min(Distance_Data))  # Finds the minimum number Index
    image_data = List_barcode[Minimum_Data_Index][2]  # Gets The Image Data of minimum number
    Actual_Image = arrange_image_data(image_data)  # Gets the Actual Image Number
    Actual_Image = int(Actual_Image[4:6])  # Gets the class digit number
    z = x # Stores values of x in another variable to get the exact image number from a class
    x = arrange_x_value(x)
    if x == Actual_Image:  # Check the similar Images and Count
        print('The Image# : {} is in class digit : {} -> Hit'.format(z, Actual_Image))
        count += 1
    else:
        print('The Image# : {} is in class digit : {} -> Miss'.format(z, Actual_Image))

acc = count / Total_Images  # Finding the Accuracy

print('Accuracy : {} %'.format(int(acc * 100))) # Gets the percentage of acccuracy
