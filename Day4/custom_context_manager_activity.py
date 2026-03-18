class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection...")

with DatabaseConnection():
    print("Working with database")
