hour, minute = map(int, input().split())
time_to_cook = int(input()) # 요리하는 데 필요한 시간

total_minute = minute + time_to_cook
hour = (hour + (total_minute // 60)) % 24
minute = total_minute % 60

print(hour, minute)