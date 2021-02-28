# Inisialsisasi Variabel
arraykelas = []

# =======
# SETTING
# =======
# Maksimal jumlah matkul per semester
# Jika nol, maka tidak ada maksimum matkul per semester
maksPerSemester = 0

# Menerima nama file input dan baca file
namaFile = input("Masukkan path file input: ")
file = open(namaFile, "r")
isiteks = file.readlines()
file.close()

# Masukkan isi file ke dalam arraykelas
# File diasumsikan ditulis dalam format yang benar
for baris in isiteks:
    a = baris.strip()
    a = a[:-1]
    arr = a.split(', ')
    arraykelas.append(arr)

# Fungsi tambahan
# isDone, mengecek apakah masih ada matkul yang belum diambil
def isDone():
    global arraykelas
    isDone = True
    i = 0
    while(i<len(arraykelas) and isDone):
        if arraykelas[i][0] != " ":
            isDone = False
        i = i + 1
        
    return isDone

# getNoPrereq, mengambil matkul tanpa prereq
def getNoPrereq():
    global arraykelas
    global maksPerSemester
    noprereqarr = []
    for kelas in arraykelas:
        if len(kelas) == 1 and kelas[0] != " ":
            noprereqarr.append(kelas[0])
        else:
            noprereq = True
            for x in kelas:
                if x != kelas[0] and x!= " ":
                    noprereq = False
            if(noprereq) and kelas[0] != " ":
                noprereqarr.append(kelas[0])
    if maksPerSemester == 0:
        return noprereqarr
    else:
        return noprereqarr[:maksPerSemester]

# delMatkul, menghapus semua matkul "X" dari prereq matkul lain
def delMatkul(X):
    global arraykelas
    for i in range(0,len(arraykelas)):
        for j in range(0, len(arraykelas[i])):
            if arraykelas[i][j] == X:
                arraykelas[i][j] = " "

# cetakKelas, mencetak semua matkul dalam sebuah array
def cetakKelas(arr):
    for i in range(0,len(arr)):
        if i<len(arr)-1:
            print(arr[i], end=", ")
        else:
            print(arr[i])
            
# Mulai sort
# Jika tidak ada prereq maka ambil mata kuliah
# Setelah diambil, ubah matkul menjadi " "
semester = 1
print()

while(not isDone()):
    kelas = getNoPrereq()
    if len(kelas) == 0:
        print("Graf tidak berupa Directed Acyclic Graph.")
        break
    else:
        print("Semester", semester, ": ", end="")
        cetakKelas(kelas)
        for x in kelas:
            delMatkul(x)
        
        semester = semester + 1
        
