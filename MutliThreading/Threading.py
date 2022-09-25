import threading

def print_cube(num):
    # function to print cube of give number
    print('Cube of : {}'.format(num*num*num))

def print_square(num):
    print('Square of : {}'.format(num*num))

if __name__ == '__main__':
    # Creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # Starting a threads
    
    t2.start()
    t1.start()

    # Wait until thread 1 is completely executed
    t1.join()
    # Wait until thread 2 is completely executed
    t2.join()
    
    print('Done!')
