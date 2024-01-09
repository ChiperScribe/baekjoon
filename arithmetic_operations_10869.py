num1, num2 = map(int, input().split())
result_array = [num1 + num2, num1 - num2, num1 * num2, int(num1 / num2), num1 % num2]
for element in result_array:
    print(element)