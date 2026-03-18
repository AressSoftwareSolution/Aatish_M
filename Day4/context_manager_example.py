class myContext:
    def __enter__(self):
        print("Entering in the block")
        return self
    def __exit__(self,exc_type,exc_value,traceback):   #__exit__(error_type, error_message, error_details)

        print("Exiting the block")

with myContext():
    print("Inside the block")
