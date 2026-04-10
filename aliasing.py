# Demonstrasi fenomena aliasing pada list
a = [1, 2, 3, 4]
b = a  #b mereferensikan objek yang sama dengan a

print("Sebelum perubahan:")
print(f"List A: {a}")
print(f"List B: {b}")

# Mengubah elemen pada a
a.append(5)

print("\nSetelah perubahan pada List B:")
print(f"List A: {a}")
print(f"List B: {b}")