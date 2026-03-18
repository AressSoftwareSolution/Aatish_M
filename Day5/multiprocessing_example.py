from multiprocessing import Process

def task():
    print("Running............")

if __name__ == "__main__":
    m1 = Process(target=task)
    m2 = Process(target=task)

    m1.start()
    m2.start()