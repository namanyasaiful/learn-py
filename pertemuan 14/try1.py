import pandas as pd

list1 = ["andi", "beni", "cika", "dodo"]
list2 = ["rpl", "multimedia", "pgsd", "pgpaud"]
list3 = [3.81, 3.21, 2.74, 2.65]

dataFrameList = pd.DataFrame(list(zip(list1,list2,list3)),
columns = ["nama", "prodi", "ipk"])

print(dataFrameList)