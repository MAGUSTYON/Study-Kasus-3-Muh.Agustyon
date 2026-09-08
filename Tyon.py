daftar_buku = ("bumi", "langit", "laut", "gunung", "hutan")
pinjaman = []

print("Silahkan masukkan buku yang ingin dipinjam.")
while True:
    print("Daftar buku yang tersedia:", daftar_buku)
    print("Ketik 'selesai' kalau sudah tidak ingin meminjam lagi.")
    buku = input("Masukkan buku: ")
    if buku == "selesai":
            break
    elif buku == "hapus":
        print("Silahkan masukkan buku yang ingin dikembalikan.")
        while True:
            print("Daftar buku yang dipinjam:", pinjaman)
            print("Ketik 'selesai' kalau sudah tidak ingin mengembalikan lagi.")
            hapus = input("Masukkan buku yang ingin dikembalikan: ")
            if hapus == "selesai": 
                break
            elif hapus in pinjaman: 
                pinjaman.remove(hapus)
                print(hapus, "berhasil dikembalikan.")
            else: 
                print(hapus, "tidak ada dalam daftar pinjaman.")
    elif buku in pinjaman:
        print(buku, "sudah dipinjam.")
    elif buku in daftar_buku:
        pinjaman.append(buku)
        print(buku, "berhasil dipinjam.")
    else:
        print("Buku tidak tersedia.")


print("STRUK PEMINJAMAN")
print("Buku yang dipinjam:")
for buku in pinjaman:
    print("- " + buku)
