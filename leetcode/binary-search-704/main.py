def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    start = 0
    end = len(nums) - 1
    # i = len(nums) // 2

    while end >= start:
        i = (start + end) // 2
        if nums[i] < target:
            start = i + 1
        elif nums[i] > target:
            end = i - 1
        elif nums[i] == target:
            return i
        # 0 1 2 3 4 5
        # s=3 e=5 => 8//2 = 4         
        # update i when not found

    return -1

# You can test your code here or simply just copy it and paste it to leetcode

