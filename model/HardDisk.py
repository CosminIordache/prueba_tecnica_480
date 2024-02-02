from model.StorageDevice import StorageDevices

class HardDisk(StorageDevices):

    def __init__(self, name, brand, total_storage):
        super().__init__(name, "HardDisk", brand, total_storage)
        self.storage = 0