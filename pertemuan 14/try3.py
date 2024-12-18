import pandas as pd

series1 = ("harry potter", "detective conan", "doremon")
series2 = (20,4,14)
series3 = ("not available", "available", "not available")
dataFrame = pd.DataFrame({"judul buku":series1, "stok buku":series2, "status":series3 })
print(dataFrame)