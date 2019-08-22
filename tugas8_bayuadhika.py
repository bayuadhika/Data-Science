mainDictionary = {"key":"value", "nama":"baban", "umur":"20", "mobil":"honda estilo 1992"}

def printDict():
    for x,y in mainDictionary.items():
        print(x,y)


def showDict():
    print(printDict())


def addDict():
    kaliMasukan = int(input('Berapa kali masukan dictionary? '))
    jenisMasukan = input('1. String \n2. Number \nMasukan angka pilihan: ')
    
    if(jenisMasukan == '1'):
        i = 0
        while(i < kaliMasukan):
            while(i < kaliMasukan):
                newKey = input('Masukan key baru: ')
                newValue = input('Masukan value baru: ')
                mainDictionary[newKey] = newValue
                print('Dictionary berhasil ditambahkan \n' + str(showDict()))
                i += 1
            return mainDictionary

    elif(jenisMasukan == '2'):
        i = 0
        while(i < kaliMasukan):
            while(i < kaliMasukan):
                newKey = int(input('Masukan key baru: '))
                newValue = int(input('Masukan value baru: '))
                mainDictionary[newKey] = newValue
                print('Dictionary berhasil ditambahkan \n' + str(showDict()))
                i += 1
            return mainDictionary


def searchDict():
    search = input('Masukan kata kunci yang dicari: ')
    if search in mainDictionary:
        print('Yang anda cari ada dalam dictionary, ', search, ':', mainDictionary[search])
    else:
        print('Tidak ditemukan')


def keluar():
    print('Good Bye ')    


backToMenu = 'y'
while(backToMenu == 'y'):
    pilihMenu = input('Main Menu \n1. Lihat full dictionary \n2. Isi Dictionary \n3. Searching Dictionary \n4. Keluar \nMasukan angka pilihan: ')
    index = int(pilihMenu) -1
    menu = [showDict, addDict, searchDict, keluar]
    menu[index]()
    backToMenu = input('Kembali ke Menu Utama? y/n ')