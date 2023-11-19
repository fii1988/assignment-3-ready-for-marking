def removed_letter(sentence, remove_letter):

    #
    count = 0
    for letter in remove_letter:
        sentence = sentence.replace(letter.lower(), '_')
        sentence = sentence.replace(letter.upper(), '_')
        count += sentence.lower().count('_')
    return sentence, count

def main():
    while True:
        user_input = input("Type a phrase (or quit to exit program): ")

        if user_input.lower() == 'quit':
            return

        letter_typed = input("Type a comma-separated list of letters to redact: ")
        result, count = removed_letter(user_input, letter_typed)

        print(f"Number of letters redacted: {count}")
        print(f"Redacted phrase: {result}\n")

if __name__ == "__main__":
    main()