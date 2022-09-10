#!/usr/bin/python3
class InclusiveRange:

    def __init__(self, *args):
        numberOfArguments = (len(args))
        if numberOfArguments < 1:
            raise TypeError('At least one argument is required')
        elif numberOfArguments == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numberOfArguments == 2:
            # start and stop will be tuple
            (self.start, stop) = args
            self.step = 1
        elif numberOfArguments == 3:
            # all start, stop and step will be tuple
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('Maximum three arguments. you have {}'.format(
                numberOfArguments))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step
def main():
    ranges = InclusiveRange(5, 210, 10)
    for x in ranges:
        print(x, end=' ')
if __name__ == "__main__":
    main()
