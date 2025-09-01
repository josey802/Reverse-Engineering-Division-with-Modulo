alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 'u', 
 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
# text = input("Type your message: \n").lower()
# shift = int(input("Type your shift number: \n"))

def encrypt(original_text, shift_amount):
  cipher_text = ""
  for letter in original_text:
    if letter not in alphabet:
      cipher_text += letter
    else:
      shifted_position = alphabet.index(letter) + shift_amount

      shifted_position %= len(alphabet) #0-25
      cipher_text += alphabet[shifted_position]
  print(f"Here is the encoded text result: {cipher_text}")

# encrypt(original_text= text, shift_amount= shift)

def decrypt(original_text, shift_amount):
  decrypted_text = ""
  for letter in original_text:
    if letter not in alphabet:
      decrypted_text += letter
    else:
      shifted_position = alphabet.index(letter) - shift_amount
      shifted_position %= len(alphabet)
      decrypted_text += alphabet[shifted_position]
  print(f"Here is the decoded text result : {decrypted_text}")

# decrypt(original_text=text, shift_amount= shift)          

def caesar():
  while True:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
      if direction not in ("encode", "decode"):
        print("You typed in the wrong input, try again \n")
        continue

      text = input("Type your message: \n").lower()
 
      while True:
        try:
          shift = int(input("Type your shift number: \n"))
          break
        except ValueError:
          print("Your input must be a number. Try again \n")

      if direction == "encode":
        encrypt(original_text= text, shift_amount= shift)

      elif direction == "decode":
        decrypt(original_text=text, shift_amount= shift)   

      again = input("\n Type 'yes' to go again, or anything else to quit: \n").lower()
      if again != "yes":
        print("Goodbye")
        break  

caesar()