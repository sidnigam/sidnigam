# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         pass

nums = [1,7,3,6,5,6]

# we want to select and index that is not on the edge and then sum all the values to the left and sum all the values to the right


for i in range(len(nums)):
    leftsum = sum(nums[:i])
    rightsum = sum(nums[i+1:])
    if leftsum == rightsum:
        print(i)
        break
    elif i+1 == len(nums):
        print("-1")