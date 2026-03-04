# **LAPORAN PRAKTIKUM OOP – GAME RPG PYTHON**

## Identitas Siswa

* **Nama** : Fadi Alyuliansyah
* **Kelas** : XI RPL 5
* **Absen** : 13
* **Mata Pelajaran** : KKA (Pemrograman Berorientasi Objek)
* **Bahasa Pemrograman** : Python
* **Tema Project** : Implementasi Konsep OOP pada Game RPG Sederhana

---

## Pendahuluan

Praktikum ini bertujuan untuk memahami serta mengimplementasikan konsep **Object Oriented Programming (OOP)** menggunakan bahasa Python. Studi kasus yang digunakan adalah pembuatan sistem sederhana game RPG, di mana setiap karakter direpresentasikan sebagai object.

Melalui 6 tahap praktikum, siswa mempelajari konsep dasar hingga lanjutan dalam OOP seperti class, interaksi object, inheritance, encapsulation, abstract class, dan polymorphism.

---

## Praktikum 1 – Dasar Class dan Object

**File:** `latihan1_rpg.py`

### Tujuan

Memahami struktur dasar pembuatan class beserta atribut dan method.

### Pembahasan

Pada tahap awal dibuat class `Hero` dengan atribut:

* `name`
* `hp`
* `attack_power`

Class ini memiliki method `info()` untuk menampilkan data karakter.
Object dibuat dari class tersebut dan nilai atributnya dapat diubah langsung.

### Analisis

Praktikum ini menunjukkan bahwa class merupakan blueprint, sedangkan object adalah hasil instansiasi dari class tersebut.
Namun, karena atribut masih bersifat public, nilainya dapat dimodifikasi secara langsung dari luar class.

---

## Praktikum 2 – Interaksi Antar Object

**File:** `latihan2_rpg.py`

### Tujuan

Memahami cara object berkomunikasi satu sama lain.

### Pembahasan

Ditambahkan method `serang()` dan `diserang()` sehingga satu hero dapat menyerang hero lainnya dan mengurangi HP lawan.

### Analisis

Konsep ini penting dalam pengembangan game karena hampir seluruh sistem dalam game melibatkan interaksi antar object.
Setiap object dapat memanggil method milik object lain.

---

## Praktikum 3 – Inheritance (Pewarisan)

**File:** `latihan3_rpg.py`

### Tujuan

Mempelajari konsep pewarisan dalam OOP.

### Pembahasan

Class `Mage` dibuat sebagai turunan dari `Hero`.
Class ini memiliki atribut tambahan `mana` serta method khusus `skill_fireball()`.

### Analisis

Dengan inheritance, kode menjadi lebih efisien karena tidak perlu menuliskan ulang atribut dan method dari class induk.
Konsep ini mempermudah pengembangan karakter baru dalam game.

---

## Praktikum 4 – Encapsulation

**File:** `latihan4_rpg.py`

### Tujuan

Memahami pembatasan akses terhadap atribut class.

### Pembahasan

Atribut `__hp` diubah menjadi private sehingga tidak dapat diakses langsung dari luar class.
Digunakan method `get_hp()` dan `set_hp()` sebagai pengontrol akses.

### Analisis

Encapsulation bertujuan menjaga keamanan data agar tidak sembarang diubah.
Konsep ini membuat program lebih terstruktur dan aman.

---

## Praktikum 5 – Abstract Class

**File:** `latihan5_rpg.py`

### Tujuan

Mempelajari penggunaan abstract class.

### Pembahasan

Dibuat class abstrak `GameUnit` menggunakan modul `abc`.
Class turunan seperti `Hero` dan `Monster` wajib mengimplementasikan method `serang()` dan `info()`.

### Analisis

Abstract class berfungsi sebagai kerangka dasar agar setiap turunan memiliki struktur method yang sama.
Hal ini sangat berguna dalam sistem yang besar dan kompleks.

---

## Praktikum 6 – Polymorphism

**File:** `latihan6_rpg.py`

### Tujuan

Memahami konsep polymorphism.

### Pembahasan

Beberapa class seperti `Mage`, `Archer`, `Fighter`, dan `Healer` memiliki method `serang()` dengan implementasi berbeda.

### Analisis

Polymorphism memungkinkan pemanggilan method dengan nama yang sama tetapi menghasilkan perilaku berbeda sesuai object-nya.
Konsep ini membuat sistem game lebih fleksibel dan dinamis.

---

## Kesimpulan

Berdasarkan seluruh rangkaian praktikum yang telah dilakukan, dapat disimpulkan bahwa:

1. OOP membantu menyusun program secara lebih terstruktur.
2. Penggunaan inheritance dan polymorphism membuat kode lebih fleksibel.
3. Encapsulation meningkatkan keamanan data dalam program.
4. Abstract class menjaga konsistensi struktur antar class.

Melalui project game RPG sederhana ini, pemahaman terhadap konsep OOP menjadi lebih mudah karena langsung diterapkan dalam studi kasus nyata.

---

## Penutup

Laporan ini dibuat sebagai bentuk dokumentasi dan pertanggungjawaban atas pelaksanaan praktikum Pemrograman Berorientasi Objek.

