# Bubble Sort (derived from Mod 7 Assignment)
running = ''

#ghost sort list to get total number of iterations
def iterations(numlist):
    sorted_list = numlist[:]
    for iteration in range(len(sorted_list)):
        swapped = False
        index = 0
        while index < len(sorted_list)-1:
            if (sorted_list[index] > sorted_list[index+1]):
                storage = sorted_list[index]
                sorted_list[index] = sorted_list[index+1]
                sorted_list[index+1] = storage
                swapped = True
            index +=1
        if swapped == False:
            break
    index = index-1
    return index

#sort list
def sort_list(numlist):
    print('~'*15)
    sorted_list = numlist[:]
    total = 0

    #sort list
    for iteration in range(len(sorted_list)):
        swapped = False
        index = 0
        while index < len(sorted_list)-1:
            if (sorted_list[index] > sorted_list[index+1]):
                storage = sorted_list[index]
                sorted_list[index] = sorted_list[index+1]
                sorted_list[index+1] = storage
                swapped = True
            index +=1
        if swapped == False:
            break   
        sorted_list_string = ', '.join(str(lindex) for lindex in sorted_list)
        print("Run through list, time #",iteration+1,":",sorted_list_string)
    sorted_list_string = ', '.join(str(lindex) for lindex in sorted_list)
    return sorted_list
    

#main loop
while running != 'quit':
    
    numbers = input("Enter a list of numbers separated by ',': ").split(',')
    numbers = [int(num) for num in numbers]

    #get sorted list
    sorted_list = sort_list(numbers)
    #get iterations
    iteration_ttl = iterations(numbers)
    #convert user input to 'string list'
    numbers = ', '.join(str(lindex) for lindex in numbers)
    #convert from list to 'string list' 
    sorted_list = ', '.join(str(lindex2) for lindex2 in sorted_list)

    print('~'*15)
    print('Original list:\n',numbers)
    print('Sorted list:\n',sorted_list)
    print('Took',iteration_ttl,'passes')
    running = input("Enter 'quit' when finished: ")
    
