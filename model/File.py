class File:
    def __init__(self, name, data, size):
        self.name = name
        self.data = data
        self.size = size

    def insertData(self, data):
        self.data = data

    def __str__(self) -> str:
        return f"File Name: {self.name}, Data: {self.data}, Size: {self.size}"