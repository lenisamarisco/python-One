def print_upper_words(words):
    """Print each word in a separate line, uppercased.
    >>>print_upper_words(["PYTHON", "IS", "VERY", "INTERESTING"])
    PYTHON
    IS 
    VERY INTERESTING
    """
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with I or i.
    >>>print_upper_words2([]"illa", "Interesting", "is"])
    ILLA
    IS
    INTERESTING
    """
    for word in words:
        if word.startswith("i") or word.startswith("I"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given
    >>>print_upper_words3 (["Interesting", "is", "Illa", "nope", "faith"],
    ...                     must_start_with=["i", "N"])
    ILLA
    INTERESTING
    IS
    NOPE
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
            