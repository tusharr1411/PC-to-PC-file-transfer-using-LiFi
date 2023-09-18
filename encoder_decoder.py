import os


#function to encode file
def to_binary(filename):
    binary_file = os.path.splitext(filename)[0] + ".txt"
    with open(filename, "rb") as f:
        content = f.read()
    with open(binary_file, "w") as f:
        f.write(''.join(format(byte, '08b') for byte in content))
    print("Encoded file saved as:", binary_file)


#function to decode file
def from_binary(filename):
    original_file = os.path.splitext(filename)[0] + os.path.splitext(filename)[1][1:]
    with open(filename, "r") as f:
        content = f.read().replace(' ', '')
    with open(original_file, "wb") as f:
        f.write(bytes(int(content[i:i+8], 2) for i in range(0, len(content), 8)))
    print("Decoded file saved as:", original_file)



#prompt user to encode or decode
user_input = input("Enter 'encode' or 'decode': ")


#encoder
if user_input == "encode":

    filename = input("Enter the filename you want to encode(with file extension): ")
    extension = os.path.splitext(filename)[1]

    if extension in {".pdf", ".mp4", ".mp3", ".gif", ".jpg", ".jpeg", ".png",".doc", ".docx", ".ppt", ".pptx",".xls", ".xlsx"}:
        to_binary(filename)
    else:
        print("Unsupported file type.")


#decoder
elif user_input == "decode":

    filename = input("Enter the .txt filename you want to decode(with .txt extension): ")
    extension = os.path.splitext(filename)[1]

    if extension == ".txt":
        from_binary(filename)
    else:
        print("Unsupported file type.")



else:
    print("Invalid input, please enter 'encode' or 'decode'")
