from model.StorageDevice import StorageDevices

class CD(StorageDevices):
    
    def __init__(self, name, brand, total_storage):
        super().__init__(name, "CD", brand, total_storage)
        self.storage = 0