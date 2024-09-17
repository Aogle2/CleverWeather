from netconnection import *
from sensors import *


Connection("airCube-79E","local#123")#.ConnectNow()

print(TempHumiditySensor(2).ReadSensorOverall())




