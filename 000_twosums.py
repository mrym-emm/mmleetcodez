print("This is solution for 2 sums from leetcode")

"""
The problem is basically, given an list of numbers `nums`, return the number's index in the array that matches a defined `target`.
It is assumed that there is ONE exact solution for any given list, and each number can be used once only.

ie: 
nums = [2,3,4,9]
target = 5
output = [0,1] --> bcs 2 + 3 = 5 and the respective numbers are at index nums[0] and  nums[1]
"""
# iterate over the numbers by making a double for loop. im pretty sure this isnt optimal but it works
# this line will check index 0 till index len(nums) - 1. we minus 1 bcs remember, indexing starts from 0, and we dont want it to go out of bounds
for i in range(len(nums) - 1):

  # remember, (inc, exc). 
  for j in range( i +1 , len(nums)):

    # checking every pair ie --> nums[0],nums[1] / nums[0], nums[2] etc... 
    if nums[i] + nums[j] == target:
      return [i,j] # return the index
