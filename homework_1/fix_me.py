def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


test_nums = [10, 15, 20]
result = calculate_average(test_nums)
print("The average is:", result)
