class Customer:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f"Full name: {self._first_name} {self._last_name}")
        # if any feature of a class begins with an _ it is regarded as a private feature - it is not intended to be used in other pieces of code

    @property
    def first_name(self):
        print("in get method")
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        print("in set method")
        self._first_name = new_first_name