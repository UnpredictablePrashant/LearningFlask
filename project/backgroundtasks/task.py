import time

def threaded_task(duration):
    for i in range(duration):
        print("Doing task  {}/{}".format(i + 1, duration))
        time.sleep(5)