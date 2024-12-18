def menu(menuR,menuD):
    if menuD in menuR:
        print(f"menu {menuD} ada")
    else:
        print(f"menu {menuD} tidak ada")

def main():
    menuR = [
        "ayam gulai",
        "babat",
        "cumi",
        "ikan kembung",
        "kikil",
        "limpa",
        "otak",
        "paru",
        "rendang",
        "telur",
        "usus"
    ]
    print("selamat datang di restoran padang")
    while True:
        menuD = input("masukan menu yang ingin dicari:").strip()
        if menuD.lower() == "keluar":
            print("terima kasih telah berkunjung")
            break
        menu(menuR,menuD)
            
if __name__ == "__main__":
    main()
# saifulloh fattah bintoro_2408256