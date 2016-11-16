Import shapefile
a = shapefile.writer(parameter) ? a.shapetype = 1/3/5
shp = a.point(x,y)
shp = a.poly([x,y],[v,w])
dbf = a.field(‘nama folder’,’c’,’4’)
dbf = a.record(‘Bandung’)
File yang berisi record dbf disimpan menggunakan method a.save(‘file shp’)
Arti method di writer
Point(x,y)
Memasukan data berbentuk point kedalam shp dan seluruh data harus format ESRI = 1
Poly[[[a,b],[c,d]]]
Memasukan data geospasial berbentuk polygon (kembali ke titik awal) dan polyline tidak kembali ke titik awal
Field(‘kota’,’c’,’40’)
Membuat atribut table bernama budaya dengan tipe data varchar dengan panjang 40 karakter, jika ingin tambah field. Contoh : field(‘budaya’,’c’,’40’)
Record(‘Bandung’)
Mengisi table yang hanya 1 field dengan value = Bandung. Jika ada 2 field maka record(‘Bandung’,’kota’)
Save(‘nama file’)
Menyimpan file shapefile di computer
Parameter pada Writer
Shapefile POLIGON
Shapefile POINT
Shapefile POLYLINE
Contoh dalam aplikasi 
POINT :
Import.shapefile
a=shapefile.Writer()
a.point(10,12)

POLYLINE:
Import.shapefile
a=shapefile.Writer()
a.poly(parts[(1,5),(5,5),(3,3)])
shapetype=shapefile.POLYLINE

POLIGON
Import.shapefile
a=shapefile.Writer()
a.poly(parts=[(1,5),(5,5),(3,3)])
