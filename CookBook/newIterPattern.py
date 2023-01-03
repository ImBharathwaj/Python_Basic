def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for _ in frange(0, 4, 0.4335):
    print(_)