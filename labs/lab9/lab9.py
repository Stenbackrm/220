"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
def addTen(nums):
    x = 0
    for i in nums:
        nums[x] = nums[x] + 10
        x = x + 1

def squareEach(nums):
    x = 0
    for _ in nums:
        nums[x] = nums[x] ** 2
        x = x + 1

def sumList(nums):
    x = 0
    for _ in nums:
        nums[x] = nums[x] ** 2
        x = x + 1
    return sum(nums)


def main():
    num_list = [1,2,3,4,5,6]
    addTen(num_list)
    print(num_list)
    squareEach(num_list)
    print(num_list)
    print(sumList(num_list))

if __name__ == '__main__':
    main()