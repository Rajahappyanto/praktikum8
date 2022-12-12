print("Nama : Raja Happyanto ")
print("Ruangan : TI.22.A2")
print('-'*50)
print("Tugas Bahasa Pemograman")
print('-'*50)
print("\n")
print('*'*50)
print('Menu Data Mahasiswa\ntype "Enter" to Input Data\ntype "Show" to Show Data\ntype "Change" to Change Data\ntype "Delete" to Delete Data\ntype "Exit" to go out\n')
print('*'*50)


data = {}
class Data():
     def __init__(self,data1,data2,data3,data4,data5,data6):
        while True:

            print("\n")
            print('.'*50)
            print('             DATA "MAHASISWA"          ')
            print('.'*50)

            x = input("> Choose the menu : ")

            print("\n")

            if x == 'Enter':
                self.ADD()
            elif x == 'Show':
                self.SHOW()
            elif x == 'Change':
                self.CHANGE()
            elif x == 'Delete':
                self.DELETE()
            elif x == 'Exit':
                self.EXIT()
                break
            
            else:
                exit()

     def ADD(self):
        print("Add Data")
        self.nim    = input('NIM\t            : ')
        self.nama   = input('Name\t        : ')
        self.tugas  = int(input('Duty value\t    : '))
        self.uts    = int(input('UTS value\t    : '))
        self.uas    = int(input('UAS value\t    : '))
        self.akhir = (self.tugas * 30/100) + (self.uts * 35/100) + (self.uas * 35/100)
        data[self.nim] = self.nama, self.tugas, self.uts, self.uas, self.akhir

class rajahappyanto(Data):

    def SHOW(self):  
        if data.items():
            print(100*'=')
            print('|   NO  |    NIM         |     NAME      |  DUTY  |   UTS   |   UAS   |     ENDED    |')
            print(100*'=')
            i = 0
            for a in data.items():
                i += 1
                print("|    {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} |    {5:6.2f}    |".format (a[0][: 14],a[1][0],a[1][1],a[1][2],a[1][3],a[1][4], no = i))
                print(100*'=')
    
    def CHANGE(self):
        print("Change Data")
        self.nim = input("Enter Nim             : ")
        if self.nim in data.keys():
            self.nama = input("Name\t        : ")
            self.tugas = int(input("Duty value\t   : "))
            self.uts = int(input("UTS value\t       : "))
            self.uas = int(input("UAS value\t       : "))
            self.akhir = (self.tugas * 30/100) + (self.uts * 35/100) + (self.uas * 35/100)
            data[self.nim] = self.nama, self.tugas, self.uts, self.uas, self.akhir
        else:
            print("Sorry, Data Not Found")

    def DELETE(self):
        print("Delete Data")
        self.nim = input("Enter NIM  : ")

        if self.nim in data.keys():
            del data[self.nim]
        else:
            print("Sorry,  Data Not Found")

    def EXIT(self):
        print()
        print(50*'*')
        print("            PROGRAM HAS ENDED              ")
        print(50*'*')
        print(50*'.')
        print("Thanks for your atenttion\nHave a good day for you\nRaja Happyanto")
        print(50*'.')

datarjhpp = rajahappyanto("data1", "data2", "data3", "data4", "data5", "data6")