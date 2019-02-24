# Python program for implementation of Insertion Sort
# Acknowledgement: InteractivePython

#For any index, the number is compared to the ones behind it until it finds the proper location to insert it
#This ascend sorts as it goes- anything in front of any given index has already been sorted
def insertion_sort(alist):

    for index in range(1, len(alist)): #Assigning the varible 'index' the range of 1 - 8.
        current_value = alist[index]  #Keep track of the value to insert
        position = index #Control variable to search backwards

        while position > 0 and alist[position - 1] < current_value: #Checking to see of further searching needs to be done
            alist[position] = alist[position - 1] #If the above = True, slide the values up one index
            position = position - 1 #Keep searching backwards

        alist[position] = current_value #Found correct position set value
        print(alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]


insertion_sort(alist)
print(alist)
