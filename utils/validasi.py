# Fungsi utilitas
def input_angka(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Input harus antara {min_value} dan {max_value}." if min_value and max_value else f"Input minimal {min_value}." if min_value else f"Input maksimal {max_value}.")
            else:
                return value
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")