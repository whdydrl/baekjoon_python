arr=[input() for _ in range(3)]
def sum(num):
    if num == "black":
        result = 0
    elif num == "brown":
        result = 1
    elif num == "red":
        result = 2
    elif num == "orange":
        result = 3
    elif num == "yellow":
        result = 4
    elif num == "green":
        result = 5
    elif num == "blue":
        result = 6
    elif num == "violet":
        result = 7
    elif num == "grey":
        result = 8
    elif num == "white":
        result = 9
    return int(result)
print(((sum(arr[0]) * 10) + (sum(arr[1]))) * (10 ** (sum(arr[2]))))