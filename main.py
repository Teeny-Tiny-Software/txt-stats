import os

def count_words_in_file(filename):
    if not filename.endswith('.txt'):
        print("Error: Please provide a .txt file.")
        return

    if not os.path.isfile(filename):
        print("Error: File does not exist.")
        return

    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        character_count = len(text)
        sentences = text.split('.')
        sentence_count = len(sentences) - 1
        print(f"Word count: {word_count}")
        print(f"Character count: {character_count}")
        print(f"Sentence count: {sentence_count}")

def main():
    filename = input("Enter the filename: ")
    count_words_in_file(filename)

if __name__ == "__main__":
    main()
