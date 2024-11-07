def login():
    Username = "Daspro2023"
    Password = "Latihan"

    username = input("Masukkan username: ")
    
    if username != Username:
        print("Username tidak dikenal.")
        return

    kesempatan = 3
    while kesempatan > 0:
        password = input("Masukkan password: ")
        
        if password == Password:
            print("Login berhasil!")
            return 
        else:
            kesempatan -= 1 
            print(f"Password salah. Kesempatan tersisa: {kesempatan}")
    print("Login gagal. Anda telah mencoba 3 kali. Akses ditolak.")

login()
# saifulloh fattah bintoro_2408256