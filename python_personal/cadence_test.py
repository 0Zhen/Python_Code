count = 0
for i in range(3000):
    count = (count + 1) % 1000
    if (count == 999):
        print('99 hi')