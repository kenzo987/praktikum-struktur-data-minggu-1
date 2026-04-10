import sys

# Menampilkan tipe data dan ukuran memori untuk berbagai tipe data

# Tipe data integer sederhana
int_sederhana = 80
size_int = sys.getsizeof(int_sederhana)

# Tipe data list dengan integer
list_int = [3]
size_list = sys.getsizeof(list_int)

# Tipe data string
str = "Hello, World!"
size_str = sys.getsizeof(str)

#Perbandingan dengan tipe data list dengan integer sederhana

print(f"Tipe data: {type(int_sederhana)}, Ukuran memori: {size_int} bytes")
print(f"Tipe data: {type(list_int)}, Ukuran memori: {size_list} bytes")
print(f"Tipe data: {type(str)}, ukuran meori: {size_str} bytes")


