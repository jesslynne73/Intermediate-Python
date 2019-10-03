def encrypt(message, key):
    # Let's start with a few if statements to ensure that the message is a string, and the key is a non-zero integer
    if type(message) == str:
        if type(key) == int and key > 0:
            # Now, let's create some strings consisting of the whole alphabet. We'll be using these to index later!
            capitalAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
            # I'll also create an empty string that our message will go in.
            encrypted_message = ""
            # This for loop will run through every character in the message.
            for letter in message:
                # If the letter is uppercase, we will use the capital string. We should find the occurrence of the
                # letter in the string, and get its index.
                if letter.isupper():
                    letter_index = int(capitalAlphabet.find(letter))
                    # When using a Caesar cipher, the new index will be our old index plus the key.
                    new_index = (letter_index + key)
                    # We need to have an if statement in case the new_index is longer than our list. We can use the
                    # modulus function built into Python to keep our list within the length.
                    if new_index > 25:
                        new_index = new_index % 26
                        # Our new letter is the character in the string at the new index. Then, we append that letter
                        # to the empty string we created.
                    new_letter = capitalAlphabet[new_index]
                    encrypted_message += new_letter
                # Let's repeat that same process for lowercase letters using our lowercase string.
                elif letter.islower():
                    letter_index = int(lowerAlphabet.find(letter))
                    new_index = (letter_index + key)
                    if new_index > 25:
                        new_index = new_index % 26
                    new_letter = lowerAlphabet[new_index]
                    encrypted_message += new_letter
                # If the character is not a letter, we don't need to encrypt it. We can append it to the string as is.
                else:
                    encrypted_message += letter
                # Don't forget to return our message!
            return encrypted_message
        else:
            return 'error'
    else:
        return 'error'


def decrypt(message, key):
    # Our decryption can start the same way with verifying that the input is correct and creating alphabet strings.
    if type(message) == str:
        if type(key) == int and key > 0:
            capitalAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
            decrypted_message = ""
            for letter in message:
                if letter.isupper():
                    letter_index = int(capitalAlphabet.index(letter))
                    # This is where decrypting gets a little more complicated than encrypting. This is due to the nature
                    # of indexing in Python. Recall that "A" is 0, not 1. Rather than complicating things with negative
                    # numbers, I'll create a rule that resets the letter_index to 25 (the index of Z) whenever it hits
                    # negative one (also the correct index of Z). This will make things easier to understand.
                    for value in range(0, key):
                        letter_index -= 1
                        if letter_index == -1:
                            letter_index = 25
                        value += 1
                    # Now, we can simply find the letter at our new index and append it to the empty string!
                    new_letter = capitalAlphabet[letter_index]
                    decrypted_message += new_letter
                # We will repeat the process for lowercase letters, still using our rule to avoid negative numbers.
                elif letter.islower():
                    letter_index = int(lowerAlphabet.index(letter))
                    for value in range(0, key):
                        letter_index -= 1
                        if letter_index == -1:
                            letter_index = 25
                        value += 1
                    new_letter = lowerAlphabet[letter_index]
                    decrypted_message += new_letter
                # Again, if the character is not a letter, we don't need to decrypt it.
                else:
                    decrypted_message += letter
                # Don't forget to return the message!
            return decrypted_message
        else:
            return 'error'
    else:
        return 'error'
