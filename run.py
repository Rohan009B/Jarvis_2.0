# TO Run JArvis 

import multiprocessing

def startJarvis():
    #process
    print("Process 1 Is running")
    from main import start
    start()

#TO run HotWord

def listenHotWord():
    #Process 2
    print("Process To is Running")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotWord)
    p1.start()
    p2.start()
    p1.join()

    if p1.is_alive():
        p2.terminate()
        p2.join()

    print("Sytem Stop")