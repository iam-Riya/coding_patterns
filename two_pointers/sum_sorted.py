def pair_sum_sorted(nums, target):

    left = 0
    right = len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]

        if sum < target:
            left += 1

        elif sum > target:
            right -= 1

        else:

            return [left, right]
        
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = pair_sum_sorted(nums, target)
    print(f"Test case 1: nums = {nums}, target = {target} -> result = {result}")

    # Test case 2
    nums = [1, 2, 3, 3]
    target = 6
    result = pair_sum_sorted(nums, target)
    print(f"Test case 2: nums = {nums}, target = {target} -> result = {result}")

    # Test case 3
    nums = [4, 4, 4, 4]
    target = 8
    result = pair_sum_sorted(nums, target)
    print(f"Test case 3: nums = {nums}, target = {target} -> result = {result}")

   
