def main():
    s = str(input("Nhap vao 1 chuoi str: "))
    try:
        print(f"Tra ve: {value(s)}")
    except ValueError as e:
        print(f"Error: {e}")

def value(s: str) -> int:
    if s.lower().startswith("hello"):
        return 100 #0
    elif s.lower().startswith("h"):
        return 20
    else:
        return 0 #100

if __name__ == "__main__":
    main()