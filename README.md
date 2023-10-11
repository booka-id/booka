# Booka
Repo untuk tugas kelompok PBP

## Daftar isi
1. [Anggota Kelompok](#meet-the-team)
2. [Deskripsi Aplikasi](#what-is-booka)
3. [Module Aplikasi](#module-aplikasi)
4. [Dataset](#dataset)
5. [Peran Pengguna](#peran-pengguna)

## Meet The Team 
- Muh. Syarief Mulyadi
- Fathan  Naufal Adhitama
- Neina Akada Maula
- Rayhan Dwi Sakha

## What is Booka
Di era digital yang terus berkembang, memperkenalkan Booka, aplikasi inovatif yang mendukung kecintaan Anda terhadap literatur. Booka hadir sebagai sahabat setia Anda untuk menjelajahi dunia literasi dengan cara yang tak terlupakan.

   - Bayangkan Anda memiliki perpustakaan pribadi yang tak terbatas, tetapi berada di ujung jari Anda. Dengan **Book Catalogue**, Anda dapat menjelajahi ribuan buku dari berbagai genre dan penulis. 

   - Booka tak hanya tentang halaman buku, tetapi juga tentang acara dan kegiatan yang berkaitan dengan dunia literasi. Ikuti acara penulis kesukaan Anda, bergabung dengan kelompok diskusi buku yang seru, dan daftarkan diri Anda pada acara-acara menarik lainnya dengan fitur **Book Event**.

   - Terkadang, memilih buku bacaan dapat menjadi sebuah tantangan. Itu sebabnya, **Book Review** hadir untuk membantu Anda dengan menghadirkan ulasan dan rekomendasi dari pembaca lain. Bagikan pandangan Anda atau temukan pandangan yang cocok dengan selera Anda. Dalam Booka, dunia buku akan terasa lebih dekat dan terhubung.

   - Di dalam Booka, Anda bukan sekadar seorang pembaca, melainkan pribadi yang menciptakan cerita literasi sendiri. Dengan **Reading Profile**, Anda dapat membangun profil pribadi Anda. Catat buku-buku yang telah Anda baca dan buat daftar buku yang ingin Anda tambahkan ke wishlist. 

Dengan Booka, kami ingin mengubah pengalaman membaca Anda menjadi lebih dari sekadar aktivitas membaca, melainkan pengalaman yang mendalam, berarti, dan terhubung. Selamat datang di Booka, di mana dunia literasi berada di genggaman Anda.

## Module Aplikasi
1. Book Catalogue :
   Menampilkan katalog buku yang tersedia untuk dibeli pengguna.

   Must Have Feature:
      1. Pembelian buku
      2. Browsing katalog buku
   Good to Have Feature:
      1. Admin dapat memodifikasi katalog buku
   
2. Book Event :
   Menampilkan event yang berafiliasi dengan organisasi kita.

   Must Have Feature:
      1. Browsing event buku
      2. Pendaftaran diri ke event
   Good to Have Feature: 
      1. Admin dapat memodifikasi katalog event
   
3. Book Review :   
   Menampilkan ulasan dari berbagai pengguna mengenai suatu buku yang tersedia di katalog kita

   Must Have Feature:
      1. Thread Comment review buku serta rating buku menggunakan bintang
      2. Daftar 10 buku dengan review tertinggi
   Good to Have Feature: 
      1. Admin dapat melakukan moderasi thread comment
   
4. Reading Profile :
   Menampilkan profil pengguna yang terdiri dari data diri pengguna, buku yang telah dibaca, serta wishlist (buku yang ingin dibeli)

   Must Have Feature:
      1. Menampilkan profile user yang terdiri dari nama, foto profil, daftar teman, dan bio singkat
      2. Browsing Profile user lain untuk ditambahkan ke friendlist
   Good to Have Feature: 
      1. Wishlist buku
      2. Reading progress
   
## Dataset
Pada proyek ini, kami menggunakan [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/discussion) yang bersumber dari Kaggle.

## Peran Pengguna 

1. User Biasa:
     Pengguna dapat membeli buku baik cetak maupun digital di aplikasi book catalogue. Pengguna dapat browsing serta mendaftarkan diri pada event yang ada. Pengguna dapat melihat review orang dari suatu buku serta dapat memberikan ulasan sendiri ketika telah membaca buku tersebut. Pengguna dapat menampilkan informasi mengenai dirinya, etc
2. Admin:
       Pengguna menambahkan, menghapus, mengubah kapasitas buku cetak, etc. Pengguna dapat menambahkan event baru di halaman event. Pengguna melakukan moderasi terhadap ulasan User Biasa, yang mana dapat menghapus review User Biasa ketika melanggar community guidelines
