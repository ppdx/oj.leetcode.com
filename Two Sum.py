class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        temp = [(x, i) for (i, x) in enumerate(num)]
        temp.sort(cmp=lambda x, y: x[0] - y[0])
        i = 0
        j = len(num) - 1
        while i != j:
            sum = temp[i][0] + temp[j][0]
            if sum == target:
                if temp[i][1] < temp[j][1]:
                    return (temp[i][1] + 1, temp[j][1] + 1)
                else:
                    return (temp[j][1] + 1, temp[i][1] + 1)
            elif sum < target:
                i += 1
            else:
                j -= 1

num = [0, 4, 3, 0]
target = 0
print(Solution().twoSum(num, target))
