# Code written by Daniel Gooch for students on the Open University course TM129 in 2019.

# Version 1.0


# imports image processing functions
from PIL import Image
# needed for some of the array manipulation
import numpy as np
# needed for file handling
import os
# needed for processing inputs
import sys
# needed for timing the algorithms
import time

# output array. Global variable to assist with the clustering processing
global output

# function for comparing three arrays and returning the median values
def median(array1, array2, array3, size, size2, split_key):

    # initialises an ouput array of the correct size
    local_output = np.arange(size*size2*4).reshape(size,size2,4)

    # for each pixel in the x dimension
    for x in range(size):
        # for each pixel in the y dimension
        for y in range(size2):
            # for each pixel value RGBA
            for z in range(4):

                # get the pixel value form each image
                a = array1[x][y][z]
                b = array2[x][y][z]
                c = array3[x][y][z]

                # find the median pixel value
                if a > b:
                    if a < c:
                        median = a
                    elif b > c:
                        median = b
                    else:
                        median = c
                else:
                    if a > c:
                        median = a
                    elif b < c:
                        median = b
                    else:
                        median = c
            
                # set the output to the median pixel value
                local_output[x][y][z] = median
                
    # return the processed image array
    return local_output, split_key 



# this is the starting function
if __name__== "__main__":

    # read in how many cores to run across the cluster. Must be a value between 2 and 32 [7 * 4-core Raspberry pis] + additional
    cores = int(sys.argv[4])
    
    # open three images and treat them as arrays of pixels iar1, iar2 and iar3 [short for imageArray1 etc]
    i1 = Image.open(str(sys.argv[1]))
    iar1 = np.asarray(i1)


    i2 = Image.open(str(sys.argv[2]))
    iar2 = np.asarray(i2)


    i3 = Image.open(str(sys.argv[3]))
    iar3 = np.asarray(i3)
    
    
    
    
    
    
        # start of the second algorithm using the cluster algorithm. Start the timer.
    print('Starting timing using the cluster algorithm')
    start = time.time()
    

    # split each of the input image arrays into 7
    split_array1 = np.array_split(iar1, cores)
    split_array2 = np.array_split(iar2, cores)
    split_array3 = np.array_split(iar3, cores)

    
    # create the maximum - 32 - empty arrays for recieving processed output data
    return_array_1 = []
    return_array_2 = []
    return_array_3 = []
    return_array_4 = []
    return_array_5 = []
    return_array_6 = []
    return_array_7 = []
    return_array_8 = []
    return_array_9 = []
    return_array_10 = []
    return_array_11 = []
    return_array_12 = []
    return_array_13 = []
    return_array_14 = []
    return_array_15 = []
    return_array_16 = []
    return_array_17 = []
    return_array_18 = []
    return_array_19 = []
    return_array_20 = []
    return_array_21 = []
    return_array_22 = []
    return_array_23 = []
    return_array_24 = []
    return_array_25 = []
    return_array_26 = []
    return_array_27 = []
    return_array_28 = []
    return_array_29 = []
    return_array_30 = []
    return_array_31 = []
    return_array_32 = []

    # for each split
    for split in range(cores):
        return_local_split = 99

        # run the comparison on a segment of the image
        return_local_output, return_local_split = median(split_array1[split], split_array2[split], split_array3[split], len(split_array1[split]), len(split_array1[split][0]), split)        

        # based on which segment has been processed, save the output to the correct return array
        if return_local_split == 0:
            return_array_1 = return_local_output
        elif return_local_split == 1:
            return_array_2 = return_local_output
        elif return_local_split == 2:
            return_array_3 = return_local_output
        elif return_local_split == 3:
            return_array_4 = return_local_output
        elif return_local_split == 4:
            return_array_5 = return_local_output
        elif return_local_split == 5:
            return_array_6 = return_local_output
        elif return_local_split == 6:
            return_array_7 = return_local_output
        elif return_local_split == 7:
            return_array_8 = return_local_output
        elif return_local_split == 8:
            return_array_9 = return_local_output
        elif return_local_split == 9:
            return_array_10 = return_local_output
        elif return_local_split == 10:
            return_array_11 = return_local_output
        elif return_local_split == 11:
            return_array_12 = return_local_output
        elif return_local_split == 12:
            return_array_13 = return_local_output
        elif return_local_split == 13:
            return_array_14 = return_local_output
        elif return_local_split == 14:
            return_array_15 = return_local_output
        elif return_local_split == 15:
            return_array_16 = return_local_output
        elif return_local_split == 16:
            return_array_17 = return_local_output
        elif return_local_split == 17:
            return_array_18 = return_local_output
        elif return_local_split == 18:
            return_array_19 = return_local_output
        elif return_local_split == 19:
            return_array_20 = return_local_output
        elif return_local_split == 20:
            return_array_21 = return_local_output
        elif return_local_split == 21:
            return_array_22 = return_local_output
        elif return_local_split == 22:
            return_array_23 = return_local_output
        elif return_local_split == 23:
            return_array_24 = return_local_output
        elif return_local_split == 24:
            return_array_25 = return_local_output
        elif return_local_split == 25:
            return_array_26 = return_local_output
        elif return_local_split == 26:
            return_array_27 = return_local_output
        elif return_local_split == 27:
            return_array_28 = return_local_output
        elif return_local_split == 28:
            return_array_29 = return_local_output
        elif return_local_split == 29:
            return_array_30 = return_local_output
        elif return_local_split == 30:
            return_array_31 = return_local_output
        elif return_local_split == 31:
            return_array_32 = return_local_output
    

    # based on the number of cores, concatenate the correct set of return arrays to construct the output image
    if cores == 2:
        output = np.concatenate((return_array_1, return_array_2))
    elif cores == 3:
        output = np.concatenate((return_array_1, return_array_2, return_array_3))
    elif cores == 4:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4))
    elif cores == 5:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5))
    elif cores == 6:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6))
    elif cores == 7:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7))

    elif cores == 8:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8))
    elif cores == 9:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9))
    elif cores == 10:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10))
    elif cores == 11:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11))
    elif cores == 12:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12))
    elif cores == 13:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13))
    elif cores == 14:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14))
    elif cores == 15:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15))
    elif cores == 16:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16))
    elif cores == 17:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17))
    elif cores == 18:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18))
    elif cores == 19:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19))
    elif cores == 20:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20))
    elif cores == 21:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21))
    elif cores == 22:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22))
    elif cores == 23:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23))
    elif cores == 24:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24))
    elif cores == 25:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25))
    elif cores == 26:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26))
    elif cores == 27:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26, return_array_27))
    elif cores == 28:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26, return_array_27, return_array_28))
    elif cores == 29:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26, return_array_27, return_array_28, return_array_29))
    elif cores == 30:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26, return_array_27, return_array_28, return_array_29, return_array_30))
    elif cores == 31:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26, return_array_27, return_array_28, return_array_29, return_array_30, return_array_31))
    elif cores == 32:
        output = np.concatenate((return_array_1, return_array_2, return_array_3, return_array_4, return_array_5, return_array_6, return_array_7, return_array_8, return_array_9, return_array_10, return_array_11, return_array_12, return_array_13, return_array_14, return_array_15, return_array_16, return_array_17, return_array_18, return_array_19, return_array_20, return_array_21, return_array_22, return_array_23, return_array_24, return_array_25, return_array_26, return_array_27, return_array_28, return_array_29, return_array_30, return_array_31, return_array_32))

    # output the output array as a png
    if os.path.exists("output2.png"):
        os.remove("output2.png")

    output = output.astype('uint8')

    new_im = Image.fromarray(output, 'RGBA')
    new_im.save("output2.png")

    
    # end the timer
    end = time.time()
    end_timer = end-start
    end_timer = float("{0:.5f}".format(end_timer))

    print('The cluster algorithm took ' + str(end_timer) + ' seconds')
    
    
    
    
    
    
    # start of the first algorithm on an individual process. Start the timer.
    print('Starting timing on an individual process')
    start = time.time()



    # get the dimensions for the image array of image 1. The assumptions are 1) all three input images
    # are the same size and 2) we are dealing with RGBA images
    size = len(iar1)
    size2 = len(iar1[0])

    # initialise an empty array of the correct size
    output = np.arange(size*size2*4).reshape(size,size2,4)

    # run the processing of the images across the whole image
    output, temp = median(iar1, iar2, iar3, size, size2, 0)

    # output the output array as a png
    if os.path.exists("output1.png"):
        os.remove("output1.png")

    output = output.astype('uint8')

    new_im = Image.fromarray(output, 'RGBA')
    new_im.save("output1.png")

    # end the timer
    end = time.time()
    end_timer = end-start
    end_timer = float("{0:.5f}".format(end_timer))

    print('The single process algorithm took ' + str(end_timer) + ' seconds')




