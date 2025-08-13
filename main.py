import sys
from stats import counter, charcount, ssort

def get_book_text(filepath):
    with open(filepath) as f:
     return f.read()


def main():
    if len(sys.argv) != 2:
        print("You need to give two arguments. Second arg will be directroy to your book")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    count = counter(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"{count} words found in the document")
    print("--------- Character Count -------")
    countchar = charcount(text)
    ssort(countchar)
    print("============= END ===============")

if __name__ == "__main__":
    main()

