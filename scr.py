def decode_array(array):
    try:
        decoded_text = bytearray(array).decode('utf-8')
        print(f"Decoded text: {decoded_text}")
    except UnicodeDecodeError:
        print("Unable to decode array to UTF-8.")

def main():
    with open('decompiled.txt', 'r') as file:
        lines = file.readlines()

    result = []
    for i in range(len(lines)):
        line = lines[i]
        if 'sbi' in line and '5' in line:
            if i+2 < len(lines) and 'sbi' in lines[i+1] and '6' in lines[i+1] and 'cbi' in lines[i+2] and '6' in lines[i+2]:
                result.append(1)
        elif 'cbi' in line and '5' in line:
            if i+2 < len(lines) and 'sbi' in lines[i+1] and '6' in lines[i+1] and 'cbi' in lines[i+2] and '6' in lines[i+2]:
                result.append(0)

    print("Result array:", result)
    decode_array(result)

if __name__ == "__main__":
    main()
