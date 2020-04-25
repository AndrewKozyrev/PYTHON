def list_to_int(digits):
    
    # Converting integer list to string list 
    # and joining the list using join()
    res = int("".join(map(str, digits)))
    
    return res

def int_to_list(number):
    res = [int(i) for i in str(number)]
    
    return res


# Initialization of variables
digits_count = 6     # given: number of digits in our number
number_initial = 461235    # given: a number
number_digits = [int(i) for i in str(number_initial)]     # a split number, i.e. digits of our number in a list
distance = 0                 # metrics for distance between serial numbers in steps
serial_numbers = [number_initial]  # Filling a list with serial numbers in queue manner

# This function finds equivalent serial numbers from a given initial number
def serialTransform(split_number, distance):
    # let's make a backup of our digits, just in case
    original_number = list_to_int(split_number)
    
    print("Entering function:\nOriginal number is: {}".format(original_number))
    # we shall begin with the first digit
    position = 0
    while position < digits_count-1:
        print("The number is: {}".format(split_number))
        print("Position is: {}".format(position))
        # go ahead and grap two digits (position, and position+1)
        left_digit, right_digit = split_number[position], split_number[position+1]
        print("working with neighbours ({}, {})".format(left_digit, right_digit))
        if position:  # if left digit is not the first
            adjacent_left = split_number[position - 1]  # there exists an adjacent digit from the left
        else:  # impossible to grab, there is none
            adjacent_left = 9  # set it to 9, because 9 will never be between two neighbouring digits
        
        if position < digits_count-2:       # check if we are not at the right end
            adjacent_right = split_number[position + 2] 
        else:  # impossible to select right adjacent digit to our pair
            adjacent_right = 9   # set it to 9 , because 9 so that our pair won't swap
        
        print("Looking at adjacent pair ({}, {})".format(adjacent_left, adjacent_right))
        # swap the digits if conditions are met
        condition1 = left_digit < adjacent_left < right_digit or right_digit < adjacent_left < left_digit
        condition2 = left_digit < adjacent_right < right_digit or right_digit < adjacent_right < left_digit
        
        if condition1 or condition2:
            split_number[position] = right_digit        #swapping digits
            split_number[position+1] = left_digit
            if not list_to_int(split_number) in serial_numbers:      # check if my number is not repeating
                serial_numbers.append(list_to_int(split_number))
                print("\tCurrent list: {}".format(serial_numbers))
                distance = distance + 1
                print("\t!Distance: {}".format(distance))
                backup_position = position
                print("Entering recursion, the number is: {}".format(original_number))
                distance = serialTransform(split_number, distance) + 1
                split_number = int_to_list(original_number)
                position = backup_position
                print("Returned from recursion, the number is: {}".format(split_number))
            else:     # reverse the changes made, need to move forward
                print("Resulting number {} is already in list".format(list_to_int(split_number)))
                split_number[position] = left_digit
                split_number[position+1] = right_digit
        print("The number is: {}\nSwitching to position {}".format(list_to_int(split_number), position + 1))
        position+=1
    print("\t\tExiting function\n\n")
    return 1

result = serialTransform(number_digits, distance)
#while result:
 #   print("Calling function")
  #  new_number = int_to_list(serial_numbers[-1])
   # result = serialTransform(new_number, distance)