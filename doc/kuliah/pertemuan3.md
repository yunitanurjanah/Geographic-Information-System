RETRIEVE DATA GEOSPASIAL

Latar Belakang

Dalam pertemuan ke 4 yaitu membahas dan memperdalam pengetahuan tentang bahasa python yang digunakan untuk mengakses data geospatial. Yang didalamnya menjelaskan mengenai cara menampilkan semua records yang ada di file shp download. Dengan mengetahui cara tersebut mempermudah seorang user atau pemakai dalam menggunakan file shp.

Penjelasan

Data geospasial  adalah lokasi geografis, karakteristik tentang obyek alam dan buatan manusia yang berada dibawah dan diatas permukaan bumi yang bersifat kasat mata ataupun fisik yang berhubungan dengan data.

Dalam memasukan data geospasial yang sudah kita download atau miliki. Dapat menggunakan python dalam mengeksekusinya. Yaitu dengan :

Membuka cmd atau Commant Promn.

Masuk kedalam folder yang berisi file shp download.

Melakukan pengetikan atau penulisan python untuk masuk ke direktori python.

Melakukan import shapefile dan memasukan data shpnya.

Pembacaan goespasial dapat dibedakan menjadi 2 yaitu :

Dbf : Membaca data records. Dapat dilakukan dengan mengetik perintah : sf.recods().

Shp : Membaca geometri records. Dapat dilakukan dengan mengetik perintah : sf.shapes().

Ketika menentukan banyaknya jumlah data yang berada di dalam data geometri dapat diketahui dengan perintah len(&quot;variable&quot;)

Untuk mengetahui nama – nama field yang digunakan dalam data geospasial tersebut dapat melakukan perintah : sf.fields

Shp

Digunakan untuk membuka data geometri didalam file geospasial yang sudah di download. Didalamnya berisi :

Bbox atau singkatan dari boundary box. Yang didalamnya berisi 4 koordinat ditiap sisinya yang digunakan sebagai batas koordinat dalam melihat  peta.

Ports

Point

shapeType  adalah standart penomoran jenis data geometri oleh ESRI.

Pada

Kesimpulan

Dalam pembacaan sebuah data goespasial dapat dilakukan dengan 2 yaitu dbf dan shp

Dbf dilakukan untuk membaca record yang berada dalam file geospasial download.

Shp dilakukan untuk membaca data geometri yang berada pada file geospasial yang didownload

Shp berisi bbox,ports, point dan shapeType.