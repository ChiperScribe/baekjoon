hour, minute = map(int, input().split())
time_to_cook = int(input()) # 요리하는 데 필요한 시간

total_minute = minute + time_to_cook
while total_minute >= 60:
    total_minute = total_minute - 60
    hour = (hour + 1) % 24

minute = total_minute
print(hour, minute)