'''
=================================================
Graded Challenge 1

Nama  : Emmanuel Gallant Sadenna Tibian
Batch : HCK-023

Program ini dibuat untuk membantu proses belanja menjadi lebih efisien
=================================================
'''



class cartItem:
    def _init_(self, nama, harga):
        self.nama = nama
        self.harga = harga

class shoppingCart:
    def _init_(self):
        self.items = [] #untuk menyimpan item yang dibuat

        #function menambahkan barang
    def menambahkanBarang(self):
            nama = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga barang: "))
            #muntuk menambahkan item yang ingin ditambahkan
            self.items.append([nama,harga])
            print(f"Barang {nama} berhasil ditambahkan")

        #function hapus barang
    def hapusBarang(self):
            for nama in self.items:
               print("Masukkan barang yang ingin dihapus: ") 
               #untuk menghapus barang yang sudah tidak diinginkan
               if nama == nama.items():
                   self.nama.remove(nama)  
                   print("Barang berhasil dihapus")
        
        #function total harga
    def totalHarga(self, harga):
            total = 0
            #menjumlahkan total harga dari barang yang diinput
            for harga in self.items:
                harga = sum(harga)
            return total
        
        #funtion tampilkan barang        
    def showBarang(self,nama,harga):
            if not self.items:
                print("Data belum tersedia")
            else:
            #menampilkan barang yang sudah diinput
                i = [nama,harga]
                n = 0
                for i in range(len(nama)):
                    n+=1
                    print(n, nama)

        #function menjalankan program        
    def runningProgram(self):
            pilihanMenu = 0
            while pilihanMenu != 5:
                #menu utama pada prgoram
                print("menu: ")
                print("1. Menambah barang")
                print("2. Hapus barang")
                print("3. Tampilkan barang di keranjang")
                print("4. Lihat total belanja")
                print("5. Exit")

                pilihanMenu = input("Pilih menu: ")

                if pilihanMenu == "1":
                    self.menambahkanBarang()
                elif pilihanMenu == "   2":
                    self.hapusBarang()
                elif pilihanMenu == 3:
                    self.showBarang()
                elif pilihanMenu == 4:
                    self.totalHarga()
                else:
                    print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")
if __name__ == "__main__":

    tempObject = shoppingCart()
    tempObject.runningProgram()
