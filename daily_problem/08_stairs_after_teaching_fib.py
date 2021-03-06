def stair_count(num, steps):
    if num <= 1:
        return 1

    total = 0
    total += stair_count(num-1,0)
    total += stair_count(num-2,0)
    return total

print(stair_count(25,0))

def s_count(num):
    if num <= 1:
        return 1
    return s_count(num-1) + s_count(num-2)

print(s_count(25))

def iterative(num):
    cache = {}
    cache[0] = 1
    cache[1] = 2

    for x in range(2, num):
        cache[x] = cache[x-1] + cache[x-2]
    return cache[num-1]

print(iterative(25))

def stair_counts(num):
    cache = [0 for x in range(num)]
    cache[0] = 1
    cache[1] = 2
    for x in range(2, num):
        cache[x] = cache[x-1] + cache[x-2]
    return cache[-1]

print(stair_counts(25))

def any_count(num,arr):

    cache = [0 for _ in range(num+1)]
    cache[0] = 1

    for x in range(1, num+1):
        cache[x] = sum(cache[x - int] for int in arr if x-int >= 0)
    return cache[-1]
print(any_count(4,[1,2]))
