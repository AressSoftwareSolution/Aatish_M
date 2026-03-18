

def decorator(func):
    def inner():
        print("Before the transaction\n")
        func()
        print("After the transaction")
    return inner

@decorator
def processing():
    print("Your tansaction is process wait........\n")

processing()
