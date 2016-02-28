class Solution:
    # @return an integer

    def threeSumClosest(self, num, target):
        num.sort()
        res = sum(num[:3])
        for i in range(len(num) - 2):
            if res == target:
                return target
            this = self.twoSum(num[i + 1:], target - num[i]) + num[i]
            if abs(this - target) < abs(res - target):
                res = this
        return res

    def twoSum(self, num, target):
        i = 0
        j = len(num) - 1
        res = num[i] + num[j]
        while i != j:
            sum = num[i] + num[j]
            if sum == target:
                return target
            elif sum < target:
                res = sum if abs(res - target) > target - sum else res
                i += 1
            else:
                res = sum if abs(res - target) > sum - target else res
                j -= 1
        return res


def test(*arrays):
    for a, t in arrays:
        print(a, t, Solution().threeSumClosest(a, t))

test(([-1, 2, 1, -4], 1))
