import pandas as pd

tuple1 = ("harry potter", 20)
tuple2 = ("detective conan", 4)
tuple3 = ("doraemon", 14)
dataFrameList = pd.DataFrame(((tuple1,tuple2,tuple3)),
columns = ["judul buku", "stok"])

print(dataFrameList)
