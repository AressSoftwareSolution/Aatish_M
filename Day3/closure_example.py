def outer():
    def inner():
        print("Python Training!")
    return inner


inner = outer()
inner()