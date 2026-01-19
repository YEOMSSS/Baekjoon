# 머리를 쓰지 않겠다

current = input()
start = input()

second = int(start[6:]) + 60 - int(current[6:])
minute = int(start[3:5]) + 60 - int(current[3:5])
hour = int(start[0:2]) + 24 - int(current[0:2])

if second >= 60:
    second -= 60
else:
    minute -= 1

if minute >= 60:
    minute -= 60
else:
    hour -= 1

if hour >= 24:
    hour -= 24

if second < 10:
    second = "0" + str(second)

if minute < 10:
    minute = "0" + str(minute)

if hour < 10:
    hour = "0" + str(hour)


print(f"{hour}:{minute}:{second}")


