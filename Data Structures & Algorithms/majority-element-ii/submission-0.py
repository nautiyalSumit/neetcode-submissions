class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        res=[]
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for h in hashmap:
            if hashmap[h]>len(nums)/3:
                res.append(h)
        return res