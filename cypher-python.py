""" 
Steps in building the Caesar Cipher program:

1. Encryption function:
   a. Define a function that takes a plaintext string and a key (parameter).
   b. Initialize an empty string to store the ciphertext.
   c. Use a 'for' loop to iterate through each character of the plaintext:
      - If the character is uppercase (A–Z, ASCII 65–90), convert it with ord(), apply the formula, and return the new character with chr().
      - If the character is lowercase (a–z, ASCII 97–122), do the same using the lowercase ASCII range.
      - Otherwise, leave non-alphabet characters unchanged.
      - Apply the encryption formula: C = (P + K) % 26, where C = Ciphertext, P = Plaintext, and K = Key.
   d. Return or print the final ciphertext.

2. User interface:
   - Display a heading: "CONTACT FORM".
   - Collect user input: subject, message text, and email address.
   - Format inputs for clarity and readability.

3. Error handling:
   - Wrap the user input section in a try–except block to handle user interruptions gracefully.

4. Application purpose:
   - The program acts as a simple contact form with encrypted fields. While basic, it serves well as a demonstration of ciphers. """

def cipher(plaintext):
    
	cipher_str = ''		# A variable to hold the latter ciphertext.

	for i in plaintext:
		if i.isupper():
			# Below is conversion of uppercase letters with a key equal to 15.
			cipher_upper = 65 + ((ord(i) - 65 + 15) % 26)
			# The undermentioned statement returns encrypted uppercase letter.
			cipher_str = cipher_str + chr(cipher_upper)
		elif i.islower():
			# Below is conversion of lowercase letters with a key equal to 15.
			cipher_lower = 97 + ((ord(i) - 97 + 15) % 26)
			# The undermentioned statement returns encrypted lowercase letter.
			cipher_str = cipher_str + chr(cipher_lower)
		else:
			# Below is the statement that handles non-alphabet characters.
			cipher_str = cipher_str + i
	
	# Whatever text input by the user is printed out as a ciphertext using the appropriate variable
	print(f"{'[Encrypted]':<22}" + cipher_str + "\n")

print("\n______________________________________________________________________\n")
print(f"{'':<28}CONTACT FORM\n")

try:	# <-- Just in case of interrupting the program by the user.

	plaintext = input(f"{'Subject:':<22}")
	cipher(plaintext)
	plaintext = input(f"{'Your message:':<22}")		# Well formatted.
	cipher(plaintext)
	plaintext = input(f"{'Your e-mail address:':<22}")
	cipher(plaintext)

	print("Thanks for submitting our [safe!] form. We'll get back to you shortly.")
	print("\n______________________________________________________________________")

except KeyboardInterrupt:
	print("\n\n\t****** APPLICATION INTERRUPTED ******\n")
