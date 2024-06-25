# PROGRAM CRUD
# SIMPLE LIBRARY APPLICATION

from tabulate import tabulate

# LIST DAFTAR BUKU
daftarBuku = [
    {
        'ID': '1001',
        'Judul': 'Atomic Habits',
        'Penulis': 'James Clear',
        'Penerbit': 'Gramedia Pustaka Utama',
        'Kategori': 'Non Fiksi',
        'Stok': 3
    },

    {
        'ID': '1002',
        'Judul': 'Filosofi Teras',
        'Penulis': 'Henry Manampiring',
        'Penerbit': 'Penerbit Buku Kompas',
        'Kategori': 'Non Fiksi',
        'Stok': 4
    },

    {
        'ID': '2001',
        'Judul': 'Pulang',
        'Penulis': 'Leila S. Chudori',
        'Penerbit': 'Kepustakaan Populer Gramedia',
        'Kategori': 'Fiksi',
        'Stok': 3
    },

    {
        'ID': '2002',
        'Judul': 'Laut Bercerita',
        'Penulis': 'Leila S. Chudori',
        'Penerbit': 'Kepustakaan Populer Gramedia',
        'Kategori': 'Fiksi',
        'Stok': 2
    },

    {
        'ID': '3001',
        'Judul': 'Hai, Miiko!',
        'Penulis': 'Ono Eriko',
        'Penerbit': 'm&c!',
        'Kategori': 'Komik',
        'Stok': 5
    },

    {
        'ID': '3002',
        'Judul': 'Doraemon',
        'Penulis': 'Fujiko F. Fujio',
        'Penerbit': 'Elex Media Komputindo',
        'Kategori': 'Komik',
        'Stok': 4
    }
]

# DATA AWAL
listPinjam = []
dataPeminjaman = []
nomor_awal = 1

# FUNGSI UNTUK MENAMPILKAN TABEL
def displayData(data):
    while True:
            try:
                print(tabulate(data, headers='keys', tablefmt='grid'))
            except:
                print('\nData buku tidak ada.')
            break

# FUNGSI UNTUK FILTER KATA KUNCI
def filter_books(keywordBuku, pilihan, dataList):
    filtered_books = [i for i in dataList if keywordBuku.lower() in i[pilihan].lower()]
    return filtered_books

# FUNGSI LOOP FILTER KATA KUNCI
def loopFilter(keywordBuku, pilihan, daftarBuku):
    if filter_books(keywordBuku, pilihan, daftarBuku):
        print('\n=============== Hasil Pencarian Buku ===============')
        displayData(filter_books(keywordBuku, pilihan, daftarBuku))
        readMenu()
    else:
        print("\nBuku tidak ditemukan.")
        readMenu()
    

# FUNGSI MENAMPILKAN DAFTAR BUKU
def readMenu():
    print("""
    ========== MENAMPILKAN DAFTAR BUKU ==========
    1. Tampilkan Seluruh Buku
    2. Pencarian Buku
    3. Kembali Ke Menu Utama

    =============================================
    """)
    inputRead = input('\nSilakan masukkan angka menu yang ingin dijalankan [1/2/3]: ')
    if inputRead == '1':
        if len(daftarBuku) == 0:
            print('Data buku tidak ada.')
            readMenu()
        else:
            displayData(daftarBuku)
            readMenu()
    elif inputRead == '2':
        filterBuku()
    elif inputRead == '3':
        mainMenu()
    else:
        print('\nMohon masukkan angka yang sesuai.')
        readMenu()

# FUNGSI MEMFILTER BUKU BERDASARKAN KATA KUNCI
def filterBuku():
    # from tabulate import tabulate
    print("""
    ========== PENCARIAN KATA KUNCI ==========
    Pilih pencarian buku berdasarkan:
    1. ID Buku
    2. Judul
    3. Penulis
    4. Penerbit
    5. Kategori
    6. Kembali ke menu utama
    
    ===========================================
    """)
    inputFilter = input('\nSilakan masukkan angka untuk pencarian: ')
    if inputFilter == '1':
        keywordBuku = input('\nSilakan masukkan keyword yang ingin dicari: ')
        filter_books(keywordBuku, 'ID', daftarBuku)
        loopFilter(keywordBuku, 'ID', daftarBuku)
    elif inputFilter == '2':
        keywordBuku = input('\nSilakan masukkan keyword yang ingin dicari: ')
        filter_books(keywordBuku, 'Judul', daftarBuku)
        loopFilter(keywordBuku, 'Judul', daftarBuku)
    elif inputFilter == '3':
        keywordBuku = input('\nSilakan masukkan keyword yang ingin dicari: ')
        filter_books(keywordBuku, 'Penulis', daftarBuku)
        loopFilter(keywordBuku, 'Penulis', daftarBuku)
    elif inputFilter == '4':
        keywordBuku = input('\nSilakan masukkan keyword yang ingin dicari: ')
        filter_books(keywordBuku, 'Penerbit', daftarBuku)
        loopFilter(keywordBuku, 'Penerbit', daftarBuku)
    elif inputFilter == '5':
        keywordBuku = input('\nSilakan masukkan keyword yang ingin dicari: ')
        filter_books(keywordBuku, 'Kategori', daftarBuku)
        loopFilter(keywordBuku, 'Kategori', daftarBuku)
    elif inputFilter == '6':
        readMenu()
    else:
        print('\nMohon masukkan angka yang sesuai.')
        filterBuku()

def createMenu():
    print("""
    =========== MENAMBAHKAN BUKU BARU ===========
    1. Menambahkan Buku Baru Ke List
    2. Kembali Ke Menu Utama

    =============================================
    """)
    inputCreate = input('\nSilakan masukkan angka menu yang ingin dijalankan [1/2]: ')
    if inputCreate == '1':
        while True:
            input_ID = input('\nSilakan masukkan ID buku yang akan ditambahkan: ')
            if len(input_ID) == 4 and input_ID.isdigit() == True:
                input_ID
                break
            else:
                print('\nMohon masukkan 4 digit angka sebagai ID buku.')
        ListValue = [value for databuku in daftarBuku for value in databuku.values()]
        if input_ID in ListValue:
            print('\nData buku sudah ada.')
        else:
            while True:
                input_judul = input('\nSilakan masukkan judul buku yang akan ditambahkan: ').title()
                if input_judul == "":
                    print('\nJudul harus diisi.')
                else:
                    input_judul
                    break
            while True:
                input_penulis = input('\nSilakan masukkan penulis buku yang akan ditambahkan: ').title()
                if input_penulis.isdigit() == True or input_penulis == "":
                    print('\nMohon hanya memasukkan nilai berupa huruf.')
                else:
                    input_penulis
                    break
            while True:
                input_penerbit = input('\nSilakan masukkan penerbit buku yang akan ditambahkan: ').title()
                if input_penerbit == "":
                    print('\nPenerbit harus diisi.')
                else:
                    input_penerbit
                    break
            while True:
                input_kategori = input('\nSilakan masukkan kategori buku yang akan ditambahkan: ').title()
                if input_kategori == "":
                    print('\nkategori harus diisi.')
                else:
                    input_kategori
                    break
            while True:
                try:
                    input_stok = int(input('\nSilakan masukkan jumlah buku yang akan ditambahkan: '))
                    if input_stok > 0:
                        print(f'Buku yang akan ditambahkan {input_judul} penulis {input_penulis} penerbit {input_penerbit}\nkategori {input_kategori} jumlah buku {input_stok}')
                        break
                    else:
                        print('\nMohon masukkan jumlah buku diatas 0.')
                except:
                    print('\nInvalid input. Mohon masukkan jumlah buku yang akan ditambahkan.')

            daftarBaru = [{
                'ID': input_ID,
                'Judul': input_judul,
                'Penulis': input_penulis,
                'Penerbit': input_penerbit,
                'Kategori': input_kategori,
                'Stok': input_stok
            }]
            displayData(daftarBaru)
        
            simpan = input('\nApakah data tersebut akan disimpan? [Ya/Tidak]: ').lower()
            if simpan == 'ya':
                daftarBuku.extend(daftarBaru)
                displayData(daftarBuku)
                print('\nBuku berhasil ditambahkan.')
            else:
                print('\nData tidak tersimpan.')
        createMenu()

    elif inputCreate == '2':
        mainMenu()
    else:
        print('\nMohon masukkan angka yang sesuai.')
        createMenu()

# FUNGSI UNTUK MENGUPDATE BUKU
def ganti_item(daftarBuku, id_buku, key, nilai_baru):
    data = input('\nApakah data yang dimasukkan sudah benar? [Ya/Tidak]: ').lower()
    if data == 'ya':
        for buku in daftarBuku:
            if buku['ID'] == id_buku:
                if key in buku:
                    buku[key] = nilai_baru
                    print(f"Data buku dengan ID {id_buku} telah diperbarui. {key} baru: {nilai_baru}")
                else:
                    print(f"key '{key}' tidak ditemukan dalam buku dengan ID {id_buku}.")
    elif data == 'tidak':
        print('\nBuku gagal di-update!')
    else:
        print('\nMohon input pilihan yang sesuai.')

# FUNGSI UNTUK MENGUPDATE DATA BUKU
def updateMenu():
    print('''
    ============ MENGUBAH DAFTAR BUKU ============
    1. Mengubah Daftar Buku
    2. Kembali Ke Menu Utama

    ==============================================
    ''')
    inputUpdate = input('Silakan input angka menu yang ingin dijalankan [1/2]: ')
    if inputUpdate == '1':
        displayData(daftarBuku)
        updateBook = input('Silakan input ID buku yang akan diupdate: ')
        ListValue = [value for databuku in daftarBuku for value in databuku.values()]
        if updateBook in ListValue:
            displayData(filter_books(updateBook, 'ID', daftarBuku))
            inputUpdate = (input("\tUpdate data berikut? (Ya/Tidak): ")).lower()
            if inputUpdate== "ya":
                print("""
            ========== UPDATE DATA BUKU ==========
            Update data buku berdasarkan:  
                1. Judul Buku
                2. Penulis
                3. Penerbit
                4. Kategori
                5. Stok
            ======================================
                """)
                inputKategori = input('\nMasukkan data yang ingin diubah: ')
                if inputKategori == '1':
                    while True:
                        MasukkanData = input("\nMasukkan data baru: ").title()
                        if MasukkanData == "":
                            print('Judul harus diisi.')
                        else:
                            MasukkanData
                            break
                    ganti_item(daftarBuku, updateBook, 'Judul', MasukkanData)
                    displayData(daftarBuku)
                elif inputKategori == '2':
                    while True:
                        MasukkanData = input("\nMasukkan data baru: ").title()
                        if MasukkanData.isdigit() == True or MasukkanData == '':
                            print('\nMohon masukkan nilai berupa huruf.')
                        else:
                            MasukkanData
                            break
                    ganti_item(daftarBuku, updateBook, 'Penulis', MasukkanData)
                    displayData(daftarBuku)
                elif inputKategori == '3':
                    while True:
                        MasukkanData = input("\nMasukkan data baru: ").title()
                        if MasukkanData == "":
                            print('\nPenerbit harus diisi.')
                        else:
                            MasukkanData
                            break
                    ganti_item(daftarBuku, updateBook, 'Penerbit', MasukkanData)
                    displayData(daftarBuku)
                elif inputKategori == '4':
                    while True:
                        MasukkanData = input("\nMasukkan data baru: ").title()
                        if MasukkanData == "":
                            print('\nKategori harus diisi.')
                        else:
                            MasukkanData
                            break
                    ganti_item(daftarBuku, updateBook, 'Kategori', MasukkanData)
                    displayData(daftarBuku)
                elif inputKategori == '5':
                    while True:
                        try:
                            MasukkanData = int(input("\nMasukkan data baru: "))
                            if MasukkanData > 0:
                                break
                            else:
                                print('\nMohon masukkan jumlah buku diatas 0.')
                        except:
                            print('\nInvalid input. Mohon masukkan jumlah buku yang akan ditambahkan.')
                    ganti_item(daftarBuku, updateBook, 'Stok', MasukkanData)
                    displayData(daftarBuku)
                else: 
                    print("\nKategori buku tidak ada.")
            elif inputUpdate== "tidak":
                print('\nBuku gagal di-update!')
            else:
                print('\nMohon input pilihan yang sesuai.')
        else:
            print('\nData ID buku tidak ditemukan.')
        updateMenu()
    elif inputUpdate == '2':
        mainMenu()
    else:
        print('\nMohon input angka yang sesuai.')
        updateMenu()

# FUNGSI UNTUK MENGHAPUS DATA BUKU DALAM LIST
def deleteMenu():
    print('''
    ============ MENGHAPUS DAFTAR BUKU ============
    1. Menghapus Daftar Buku
    2. Kembali Ke Menu Utama

    ===============================================
    ''')
    inputHapus = input('\nSilakan input angka menu yang ingin dijalankan [1/2]: ')
    if inputHapus == '1':
        displayData(daftarBuku)
        hapusBook = input('nSilakan input ID buku yang akan dihapus: ')
        ListValue = [value for databuku in daftarBuku for value in databuku.values()]
        if hapusBook not in ListValue:
            print('\nData buku tidak ada.')
            deleteMenu()
        else:
            tanya = input(f'Apakah yakin akan menghapus buku dengan ID {hapusBook}? [Ya/Tidak]: ').lower()
            if tanya == 'ya':
                for e in filter_books(hapusBook, 'ID', daftarBuku) :
                    daftarBuku.remove(e)
                displayData(daftarBuku)
                print("\nData berhasil dihapus!")
            else: 
                print("\nData tidak berhasil dihapus.")
        deleteMenu()
    elif inputHapus == '2':
        mainMenu()
    else:
        print('\nMohon input angka yang sesuai.')
        deleteMenu()

# FUNGSI UNTUK PINJAM BUKU
def borrowMenu():
    print('''
    ================ MEMINJAM BUKU ================
    1. Meminjam Buku
    2. Kembali Ke Menu Utama

    ===============================================
    ''')
    inputPinjam = input('\nSilakan input angka menu yang akan dijalankan [1-2]: ')
    if inputPinjam == '1':
        displayData(daftarBuku)
        while True:
            pinjam = input('\nSilakan input ID buku yang akan dipinjam: ')
            ListValue = [value for databuku in daftarBuku for value in databuku.values()]
            if pinjam not in ListValue:
                print('\nData buku tidak ada.')
                borrowMenu()
            else:
                data = filter_books(pinjam, 'ID', daftarBuku)
                displayData(data)
                tambahkan = (input('\nApakah Anda akan meminjam buku ini? [Ya/Tidak]: ')).lower()
                if tambahkan == 'ya':
                    while True:
                        try:
                            qty = int(input('\nSilakan masukkan jumlah buku yang akan dipinjam: '))
                            if qty > 0:
                                break
                            else:
                                print('\nMohon masukkan jumlah buku diatas 0.')
                        except:
                            print('\nInvalid input. Mohon masukkan jumlah buku yang akan ditambahkan.')
                    if qty > data[0]['Stok']:
                        print("\nMohon maaf stok buku tidak cukup")
                        listPinjam.clear()
                    else :
                        listPinjam.append({
                        'ID Buku': (data[0]['ID']),
                        'Judul': (data[0]['Judul']), 
                        'Qty': qty
                        })
                else:
                    print("\nPeminjaman buku dibatalkan.")
                    listPinjam.clear()
                    borrowMenu()

            lagi = input('\nApakah Anda akan meminjam buku lain? [Ya/Tidak]: ').lower()
            if lagi == 'ya':
                True
            if lagi == 'tidak':
                break

        displayData(listPinjam)
        checkout = input('\nApakah Anda yakin akan meminjam buku tersebut? [Ya/Tidak]: ').lower()
        if checkout == 'ya':
            global nomor_awal
            while True:
                namaPeminjam = input('\nSilakan masukkan nama Anda: ').title()
                if namaPeminjam.isdigit() == True or namaPeminjam == "":
                    print('\nMohon masukkan nilai berupa huruf.')
                else:
                    namaPeminjam
                    break
            while True:
                alamatPeminjam = input('\nSilakan masukkan alamat Anda: ').title()
                if namaPeminjam.isdigit() == True or namaPeminjam == "":
                    print('\nMohon masukkan nilai berupa huruf.')
                else:
                    namaPeminjam
                    break
            noPeminjaman = nomor_awal
            nomor_awal += 1
            dict_peminjaman = {
                'No Pinjaman': noPeminjaman,
                'Nama Peminjam': namaPeminjam,
                'Alamat' : alamatPeminjam
            }
            for item in range(len(listPinjam)):
                listPinjam[item].update(dict_peminjaman)
            dataPeminjaman.extend(listPinjam)
            print('\nSilakan lakukan pengembalian buku 14 hari dari sekarang.')
            for item in listPinjam:
                (filter_books(item['ID Buku'], 'ID', daftarBuku))[0]['Stok'] -= item['Qty']
            print('\n======= Stok buku sudah update =======')
        elif checkout == 'tidak':
            print("\nPeminjaman batal.")
            listPinjam.clear()
            borrowMenu()
        else:
            print('\nMohon masukkan pilihan yang sesuai.')
            listPinjam.clear()
        
        listPinjam.clear()
        displayData(daftarBuku)
        print("\n ======= Data Peminjam =======\n")
        displayData(dataPeminjaman)
        borrowMenu()

    elif inputPinjam == '2':
        mainMenu()
    else:
        print('\nMohon input angka yang sesuai.')
        borrowMenu()


#Fungsi Mengembalikan
def returnMenu():
    print('''
        ============== PENGEMBALIAN BUKU ==============
        1. Pengembalian Buku
        2. Kembali Ke Menu Utama

        ===============================================
        ''')
    inputReturn = input('\nSilakan input angka menu yang akan dijalankan [1-2]: ')
    if inputReturn == '1':
        displayData(dataPeminjaman)
        while True:
            try:
                kembali = int(input('\nMasukkan No Pinjaman untuk mengembalikan buku: '))
            except:
                print('\nMasukkan No. Peminjaman Buku')
                returnMenu()
            ListValue = [value for datapinjaman in dataPeminjaman for value in datapinjaman.values()]
            if kembali not in ListValue:
                print("\nNo Peminjaman tidak ada.")
                returnMenu()
            else:
                x = (list(filter(lambda data: data['No Pinjaman'] == (kembali), dataPeminjaman)))
                hapus = input('\nApakah Anda akan mengembalikan semua buku? [Ya/Tidak]: ')
                if hapus == 'ya':
                    for i in x:
                        (filter_books(i['ID Buku'], 'ID', daftarBuku))[0]['Stok'] += i['Qty']
                        dataPeminjaman.remove(i)
                    print('\n***Buku telah berhasil dikembalikan***\n')
                    print('\n======= Stok buku sudah update ========')
                    displayData(daftarBuku)
                else:
                    print('\nBuku belum dikembalikan.')
            returnMenu()
            lagi = input('\nApakah mau mengembalikan buku lain? [Ya/Tidak]: ')
            if lagi == 'ya':
                True
            if lagi == 'tidak':
                print('\nTerima Kasih!')
                break
            returnMenu()
    elif inputReturn == '2':
        mainMenu()
    else:
        print('\nMohon input angka yang sesuai.')
        returnMenu()

# FUNGSI KELUAR PROGRAM
def exitMenu():
    print('\nTerima kasih telah berkunjung.')
    exit()


# FUNGSI UTAMA
def mainMenu():
    print("""
    =========== SELAMAT DATANG DI MINI PERPUSTAKAAN ELISA ===========
                            ***MENU UTAMA ***
    1. Menampilkan Daftar Buku
    2. Menambah Daftar Buku
    3. Mengubah Daftar Buku
    4. Menghapus Daftar Buku
    5. Meminjam Buku
    6. Mengembalikan Buku
    7. Keluar Program

    ======================== SELAMAT MEMBACA ========================
""")
    inputMenu = input('\nSilakan input angka menu yang akan dijalankan [1-7]: ')
    if inputMenu == '1':
        readMenu()
    elif inputMenu == '2':
        createMenu()
    elif inputMenu == '3':
        updateMenu()
    elif inputMenu == '4':
        deleteMenu()
    elif inputMenu == '5':
        borrowMenu()
    elif inputMenu == '6':
        returnMenu()
    elif inputMenu == '7':
        exitMenu()
    else:
        print('\nMohon input angka yang sesuai.')
        mainMenu()

# MEMANGGIL FUNGSI MENU UTAMA
mainMenu()