year = int(input())

# if (year % 4 == 0):
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             print('1')
#         else:
#             print('0')
#     else:
#         print('1')
# else:
#     print('0')

def is_leap_year(year):
    result = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = True
    else:
        result = False
    return result

if is_leap_year(year) == True:
    print('1')
else:
    print('0')