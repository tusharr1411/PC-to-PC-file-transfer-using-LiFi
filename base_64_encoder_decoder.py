import os
import base64


# Function to encode file using base64 and store the file type
def to_base64(filename):
    base64_file = os.path.splitext(filename)[0] + ".txt"
    
    # Get the original file extension
    file_extension = os.path.splitext(filename)[1]
    
    with open(filename, "rb") as f:
        content = f.read()
    
    # Perform base64 encoding
    encoded_content = base64.b64encode(content).decode('utf-8')
    
    # Store the file type at the beginning of the encoded content
    encoded_content_with_header = f"File Type: {file_extension}\n\n{encoded_content}"
    
    with open(base64_file, "w") as f:
        f.write(encoded_content_with_header)
    
    print("Encoded file saved as:", base64_file)


# Function to decode base64 encoded file and save it with the original extension and "decoded_" prefix
def from_base64(filename):
    with open(filename, "r") as f:
        content = f.read()
    
    # Extract the file type from the header
    file_type_line = content.split("\n")[0]
    file_extension = file_type_line.replace("File Type: ", "").strip()
    
    # Remove the file type header from the encoded content
    encoded_content = content.split("\n\n", 1)[1]
    
    # Perform base64 decoding
    decoded_content = base64.b64decode(encoded_content)
    
    # Add "decoded_" prefix to the original filename and save the decoded file
    original_file = "decoded_" + os.path.splitext(filename)[0] + file_extension
    with open(original_file, "wb") as f:
        f.write(decoded_content)
    
    print(f"Decoded file saved as: {original_file}")


# Prompt user to encode or decode
user_input = input("Enter 'encode' or 'decode': ")

# Encoder
if user_input == "encode":
    filename = input("Enter the filename you want to encode (with file extension): ")
    extension = os.path.splitext(filename)[1]

    if extension in {".pdf", ".mp4", ".mp3", ".gif", ".jpg", ".jpeg", ".png", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"}:
        to_base64(filename)
    else:
        print("Unsupported file type.")

# Decoder
elif user_input == "decode":
    filename = input("Enter the .txt filename you want to decode (with .txt extension): ")
    extension = os.path.splitext(filename)[1]

    if extension == ".txt":
        from_base64(filename)
    else:
        print("Unsupported file type.")

else:
    print("Invalid input, please enter 'encode' or 'decode'")
