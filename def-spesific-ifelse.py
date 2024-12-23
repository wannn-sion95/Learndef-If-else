def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Masukkan angka yang valid.")

def compare_numbers(x, y):
    print("---------------------------------")
    if x < y:
        print("Nilai x kurang dari Nilai y")
    elif x > y:
        print("Nilai x lebih besar dari Nilai y")
    else:
        print("Nilai x sama dengan Nilai y")

def perform_operations(x, y):
    print("---------------------------------")
    print(f"Penjumlahan: {x} + {y} = {x + y}")
    print(f"Pengurangan: {x} - {y} = {x - y}")
    print(f"Perkalian: {x} * {y} = {x * y}")
    if y != 0:
        print(f"Pembagian: {x} / {y} = {x / y}")
    else:
        print("Pembagian: Tidak dapat membagi dengan nol")
    print("---------------------------------")

def main():
    print("---------------------------------")
    angkaPertama = get_input("Masukkan nilai huruf x: ")
    angkaKedua = get_input("Masukkan nilai huruf y: ")

    compare_numbers(angkaPertama, angkaKedua)
    perform_operations(angkaPertama, angkaKedua)

if __name__ == "__main__":
    main()
