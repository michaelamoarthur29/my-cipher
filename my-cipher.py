import sys

# Check if the shift amount is provided
if len(sys.argv) < 2:
    print("Usage: python3 mycipher.py <shift>")
    sys.exit(1)

# Read the shift amount from the command line argument
shift = int(sys.argv[1])

# Read input from the standard input (keyboard) until EOF (Ctrl+D)
message = ""
for line in sys.stdin:
    message += line

# Remove non-alphabetic characters and convert to uppercase
message = ''.join(filter(str.isalpha, message)).upper()

# Create the Caesar cipher
cipher_message = ""
for char in message:
    cipher_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    cipher_message += cipher_char

# Format the output into blocks of five characters with ten blocks per line
output = ""
for x in range(len(cipher_message)):
    if (x % 5) == 0 and x != 0:
        output += " "
    if (x % 50) == 0 and x != 0:
        print(output.strip())
        output = ""
    output += cipher_message[x]

# Print the last line if it's not a multiple of 50
if len(cipher_message) % 50 != 0:
    print(output.strip())
