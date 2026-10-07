class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 1
        while right < len(nums):
            if right - left > k:
                left += 1

            slice = nums[left : right + 1]

            if len(set(slice)) != len(slice):
                return True

            else:
                right += 1

        return False
