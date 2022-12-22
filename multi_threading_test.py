import threading
import time

def pub():
    while True:
        print('Publishing data: GG')
        time.sleep(2)

if __name__ == '__main__':
    T = threading.Thread(target = pub, args=[])
    T.setDaemon(True)
    T.start()
    while True:
        IN = input('Command:\n')
        if IN == '0':
            print('The whole thread is terminating!')
            break
        elif IN == '1':
            if T.is_alive():
                print('T is  alive')
            else:
                print('T is dead')
        else:
            continue
    
