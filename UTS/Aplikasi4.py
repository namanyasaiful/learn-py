nim = int(input("Masukan NIM: "))

if 1 <= nim <= 50 : 
    if nim %2 == 0 :
        print("silahkan masuk ke kelas k2")
    else : 
        print("silahkan masuk ke kelas k1")
    
if 51 <= nim <= 100 : 
    if nim %2 == 0 :
        print("silahkan masuk ke kelas k4")
    else : 
        print("silahkan masuk ke kelas k3")

if 101 <= nim <= 150 : 
    if nim %2 == 0 :
        print("silahkan masuk ke kelas k6")
    else : 
        print("silahkan masuk ke kelas k5")

if nim > 150 : 
    if nim %2 == 0 :
        print("silahkan masuk ke kelas k8")
    else : 
        print("silahkan masuk ke kelas k7")
# saifulloh fattah bintoro_2408256