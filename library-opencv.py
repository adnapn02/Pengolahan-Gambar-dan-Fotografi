# memanggil library opencv
# baca gambar dengan pendekatan pola warna RGB
import cv2

# memanggil fungsi google collab untuk memperbaiki syntak menampilkan dilayar
from google.colab.patches import cv2_imshow
# membuat variabel untuk memuat nilai gambar yang ada di folder kerja
img= cv2.imread("oem_oem_full01.jpeg")
# menampilkan dilayar dengan memanggil variabel img yang sudah berisi nilai gambar
cv2_imshow(img)
# melihat tipe data dari variabel img disimpan sebagai apa
print(type(img))