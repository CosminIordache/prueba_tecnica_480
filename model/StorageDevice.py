from model.File import File

class StorageDevices():
    def __init__(self, name, storage_tipe, brand, total_storage):
        self.name = name
        self.data = []
        self.storage_tipe = storage_tipe
        self.total_storage = total_storage
        self.brand = brand
        self.is_rotating = False

    def rotateDisk(self):
        self.is_rotating = True
        print(f"{self.name} rotating...")

    def insertData(self, file):
        if not self.is_rotating:
            print(f"Cannot insert data into {self.name}. The disk is not rotating.")      
        else:
            if self.storage + file.size <= self.total_storage:
                self.data.append(file)
                self.storage += file.size 
                print(f"{file.name} inserted in {self.name}")
            else:
                print(f"Not enough space in {self.name} to insert {file.name}")

    def removeData(self, file):
        if file in self.data:
            self.data.remove(file)
            print(f"File '{file.name}' removed from {self.name}")
        else:
            print(f"File '{file.name}' not found in {self.name}")
            
    def readData(self):
        if self.is_rotating:
            print("Files in the storage:")
            for file in self.data:
                print(file.name)
        else:
            print(f"Cannot insert data into {self.name}. The disk is not rotating.")  

    def __str__(self) -> str:
        return (f"Name: {self.name}\n"
                f"Data: {[str(file.name) for file in self.data]}\n"
                f"Disk type: {self.storage_tipe}\n"
                f"Total Storage: {self.total_storage} GB\n"
                f"Brand: {self.brand}\n"
                f"Rotating: {'Yes' if self.is_rotating else 'No'}")


        
