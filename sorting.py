# Sorting algorithms

# List of Numbers -> Boolean (True or False)
# Returns True if the given list is sorted
# False otherwise
def sorted(nums):
    if len(nums) > 1:
        ii = 0
        while ii < len(nums) - 1:
            if nums[ii] > nums[ii+1]:
                return False
            ii += 1
    return True

# List of Numbers -> List of Numbers
# Compares an element in the list with the
# element next to it, and "bubbles" the largest
# element to the top each iteration
# Returns the list of numbers sorted from smallest
# to largest
def bubbleSort(nums):
    iteration = 0
    while not sorted(nums):
        num_i = 1
        while num_i < len(nums) - iteration:
            if nums[num_i - 1] > nums[num_i]:
                # swap numbers at indexes
                # nums_i and nums_i-1
                temp = nums[num_i - 1]
                nums[num_i - 1] = nums[num_i]
                nums[num_i] = temp
                
            num_i += 1
            continue
        print("Iteration:{}".format(iteration), nums)
        iteration += 1
            
    return nums        

def insertionSort(nums):
    sorted_to = 0
    while not sorted(nums):
        num_i = sorted_to + 1
        while num_i > 0:
            print("Iteration:{}".format(sorted_to), nums)
            if nums[num_i - 1] > nums[num_i]:
                # swap numbers at indexes
                # nums_i and nums_i-1
                temp = nums[num_i - 1]
                nums[num_i - 1] = nums[num_i]
                nums[num_i] = temp
                num_i -= 1
            else:
                break

        sorted_to += 1


    print("Iteration:{}".format(sorted_to), nums)
    return nums      



import random
randomList = [random.randint(1, 30) for x in range(10)]
print("Original List: ", randomList)
print("Bubble Sort")
print(bubbleSort(randomList))

randomList = [random.randint(1, 30) for x in range(10)]
print("Original List: ", randomList)
print("Insertion Sort")
print(insertionSort(randomList))
