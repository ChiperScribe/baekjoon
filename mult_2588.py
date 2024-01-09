# def extract_digit(number):
#     digit_array = []
#     for i in range(3):
#         digit_array.append(number % 10)
#         number = int(number / 10)
#     return digit_array

# num1 = int(input())
# num2 = int(input())
# num2_digit_array = extract_digit(num2)
# for i in range(3):
#     print(num1 * num2_digit_array[i])
# print(num1 * num2)

#파이썬을 처음 써봐서 이렇게 간단하게 코딩할 수 있다는 사실을 몰랐다.
num1, num2 = int(input()), input()
for element in reversed(num2):
    digit = int(element)
    print(num1 * digit)
print(num1 * int(num2))