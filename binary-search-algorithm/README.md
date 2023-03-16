# Binary Search Algorithm in Python

- Limitation

    1. I don't think there are any limitations in this code, but if you find any, please let me know as I am a beginner and would work on your feedback to improve the code and myself as well.
---
- Explaination

    1. The input array must be sorted in ascending order, but no worries about that; I have used the `sort()` at the start of the function to sort the array first.

    2. We initialize `start_element` and `last_element` pointers to the beginning and end of the array.

    3. While `start_element` is less than or equal to `last_element`, we calculate the middle index using integer division. If the target value is found at the middle index, we return the index.

    4. If the value at the middle index is less than the target, we update the `start_element` pointer to the index after the middle index.

    5. If the value at the middle index is greater than the target, we update the `last_element` pointer to the index before the middle index.

    6. We continue the loop until we have either found the target value or determined that it is not in the array. If the target value is not found, we return -1.
