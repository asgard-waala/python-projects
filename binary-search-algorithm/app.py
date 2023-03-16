def binary_search(arr, target):

    arr.sort()
    start_element = 0
    last_element = len(arr) - 1
    steps = 0

    while(start_element <= last_element):

        print("Steps:", steps, ":", str(arr[start_element:last_element+1]) + "\n")
        steps = steps + 1
        middle_element = (start_element + last_element) // 2

        #print("Middle element is: ", middle_element)

        if target == arr[middle_element]:

            return middle_element
        if target < arr[middle_element]:

            last_element = middle_element - 1 
        else:
            start_element = middle_element + 1

    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

target = 0

result = binary_search(arr, target)

if result == -1:
    print("Target value not found in the array.\n")
else:
    print("Target value found at index: ", result)
