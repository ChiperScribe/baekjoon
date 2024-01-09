def extract_digit(number):
    digit_array = []
    for i in range(3):
        digit_array.append(number % 10)
        number = int(number / 10)
    return digit_array

num1 = int(input())
num2 = int(input())
num2_digit_array = extract_digit(num2)
for i in range(3):
    print(num1 * num2_digit_array[i])
print(num1 * num2)