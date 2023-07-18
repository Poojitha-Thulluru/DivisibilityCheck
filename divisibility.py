def is_divisible_by_3(num_array: list) -> int:
    if sum(num_array) % 3 == 0:
        return 1
    return 0


try:
    nums_array = list(map(int, input("Enter integers separated by space : ").split()))
    print(is_divisible_by_3(nums_array))
except ValueError:
    print("Invalid Input. Please Enter only integers")