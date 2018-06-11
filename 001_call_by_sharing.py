# 这是一个典型的call by sharing的例子, nums在函数里面被传参的时候,nums等于变成实
# 参的一个alias. 而在函数体内部nums指向另外的nums[::-1]的时候,只是这个alias改变
# 了,实参并没有改变
def incorrect_reverse_list(nums):
    nums = nums[::-1]
    print("innner: nums:", nums)
    return


if __name__ == '__main__':
    input = [1, 2, 3]
    print("before", input)
    incorrect_reverse_list(input)
    print("after", input)
