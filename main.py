from stats import get_sorted_list
from stats import get_word_count

def main():
    book_directory = "books/frankenstein.txt" 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_directory}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_directory)} total words")
    print("--------- Character Count -------")
    
    char_list = get_sorted_list(book_directory)

    for char in char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()

