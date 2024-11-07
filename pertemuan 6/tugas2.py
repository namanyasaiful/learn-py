kelamin = input("Masukan Jenis kelamin: ")
umur = int(input("Masukan Umur: "))
tinggi = int(input("masukan tinggi badan: "))
iq = int(input("masukan iq: "))

if 18 <= umur <= 25 : 
    if kelamin == "pria" and tinggi >= 170 and iq >= 130  : 
        print("anda masuk kategori catwalk!")
    elif kelamin == "wanita" and tinggi >= 175 and iq >= 130 :
        print("anda masuk kategori catwalk!")
    else : 
        print("anda tidak masuk kategori catwalk!")
else : 
    print("anda tidak masuk kategori catwalk!")
# saifulloh fattah bintoro_2408256