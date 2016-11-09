Dalam sebuah file Geometri terdapat beberapa bagian yaitu :
Poin
Digunakan untuk menunjukan sebuah lokasi
Poliline
Digunakan untuk menunjukan batas- batas suatu lokasi
Poligon 
Digunakan untuk menunjukan suatu pulau. Dimana titi awal dan titik akhir bertemu.
Sf = shapefile.Reader(‘bts_negara’)
Sf adalah variable inisialisasi.
Shapefile adalah sebuah class.
Reader adalah sebuah method.
‘bts_negara’ adalah sebuah parameter.
Dalam menentukan data record sesuai dengan apa yang ingin kita tampilkan dapat menggunak perintah seberti dibawah ini :
sf.records()[1] 
Menampilakn semua data records di colom ke 1.
sf.records(0)[1]
menampilkan data pada baris ke 0 dengan colom ke 1.
Sf.shapes() ? sebuah object
Karena objek harus didalam sebuah variable maka
A = sf.shapes()
Dir a  
