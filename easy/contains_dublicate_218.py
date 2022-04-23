class Solution(object):
    def containsDuplicate(self, nums):
        counter = set()
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True
            
        return False
        