# Recursive sorting
# "Divide and conquer"

# - Take a large list
# - Divide it into 2 or more smaller lists
# - Sort the smaller lists, put the sorted smallers lists
#    back together

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        # choose a pivot point
        pv = len(nums) // 2
        l1 = nums[:pv]
        l2 = nums[pv:]
        
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        print(l1)
        print(l2)

        # merge two sorted lists
        ret_list = []
        ii, jj = 0, 0
        while ii < len(l1) and jj < len(l2):
            if l1[ii] < l2[jj]:
                ret_list.append(l1[ii])
                ii += 1
            else:
                ret_list.append(l2[jj])
                jj += 1

        # if one of the lists has an element remaining
        # add it to the end of the list
        if ii < len(l1):
            ret_list = ret_list + l1[ii:]
        elif jj < len(l2):
            ret_list = ret_list + l2[jj:]
        print(ret_list)

        return ret_list




# Take the first number in a list, use as a pivot
# Put every other element into one of two smaller lists
#   - One list: list_1 has elements < pv
#   - Other list: list_ 2 has elements >= pv

# Recursive quick_sort on list_1 and list_2
# return sorted list_1 + [pv] + sorted list_2

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pv = nums[0]
        larger = []
        smaller = []
        for ii in nums[1:]:
            if ii >= pv:
                larger.append(ii)
            else:
                smaller.append(ii)
        l2 = quick_sort(larger)
        l1 = quick_sort(smaller)
        return l1 + [pv] + l2
                
    

