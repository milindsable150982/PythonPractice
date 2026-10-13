class Employee:
    """Simple Employee class placeholder."""
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Employee(name={self.name!r}, id={self.id!r})"

# Example helper function
def example_employee():
    return Employee("Alice", 1)
