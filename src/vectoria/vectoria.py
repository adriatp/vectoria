# temperature_converter.py

def main():
    celsius = float(input("Introduïu la temperatura en graus Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} graus Celsius equivalen a {fahrenheit} graus Fahrenheit.")

if __name__ == "__main__":
    main()