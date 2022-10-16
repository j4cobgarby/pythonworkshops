before_prev = 0
prev = 1

for i in range(50):
    print(prev)

    current = prev + before_prev
    before_prev = prev
    prev = current