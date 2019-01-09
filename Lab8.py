"""
Developer: Isaac Neace
Program: Lab8
Email: isneace@lcmail.lcsc.edu
Date: 10/25/18

Description: This program uses the bubble sort
             to sort a list alternating from
             right to left until it meets in
             the middle with a sorted list.
"""




def main():

        myList=[11,5,78,3,14,67,22,37,19,25,99]
        #myList=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

        print "Before Sort: ",myList

        myList = bubbleSort(myList)

        print "\n\nAfter Sort: ",myList

        print "\n\n"


def bubbleSort(myList):

        print "\n"
        current = 0
        Sorted  = False
        last    = len(myList) - 1

        while current <= last and Sorted==False :

                Sorted = True
                index  = last

                print "Pass:", current, "\n"

                while ( index > current):
                        if myList[index] < myList[index-1] :
                                #print "Swapping: %d And : %d\n" % (myList[index], myList[index-1])
                                Sorted = False
                
                                #Swap Values:
                                tmp             = myList[index]         
                                myList[index]   = myList[index-1]       
                                myList[index-1] = tmp   


                        index = index - 1

                print myList, "\n"

                current = current + 1
                index = current

                while (index < last):
                        if myList[index] > myList[index+1]:
                                Sorted = False

                                tmp = myList[index]
                                myList[index] = myList[index+1]
                                myList[index+1] = tmp
                        index += 1

                last -= 1
                                

        return myList

main()

"""
Output:
Before Sort:  [11, 5, 78, 3, 14, 67, 22, 37, 19, 25, 99]


Pass: 0 

[3, 11, 5, 78, 14, 19, 67, 22, 37, 25, 99] 

Pass: 1 

[3, 5, 11, 14, 19, 22, 67, 25, 37, 78, 99] 

Pass: 2 

[3, 5, 11, 14, 19, 22, 25, 37, 67, 78, 99] 



After Sort:  [3, 5, 11, 14, 19, 22, 25, 37, 67, 78, 99]

"""
