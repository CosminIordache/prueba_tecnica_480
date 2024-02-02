from model.CD import CD
from model.StorageDevice import StorageDevices
from model.File import File
from model.HardDisk import HardDisk

file = File(name="test.txt", data="informacion del archivo", size=110)
file1 = File(name="test1.txt", data="informacion del archivo", size=110)

cd = CD(name="cd1", brand="Samsung", total_storage=1000)
hd = HardDisk(name="hd1",brand="Seageate", total_storage=1000)

cd.rotateDisk()
# hd.rotateDisk()

# hd.insertData(file)
cd.insertData(file)
cd.insertData(file1)
print(cd)
cd.removeData(file)
print(cd)



