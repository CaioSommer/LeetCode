class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterates through the list of nums
        for i in nums:
            for j in nums:
                # checks if the current number + other numbers in the list is equal to target
                if nums[j] + nums[i] == target:
                    # in the question you cannot use the same number twice
                    if j != i:
                        # finally, returns the numbers which you have to add!
                        return [j, i]
        # if there are no numbers that add u to the target, return False
        return False
