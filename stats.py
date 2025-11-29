def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_word_list(file_path):
    content = get_book_text(file_path)
    return content.split()

def get_word_count(file_path):
    return len(get_word_list(file_path))

def get_character_count(file_path):
    characters = {}
    word_list = get_word_list(file_path)

    for word in word_list:
        word = word.lower()
        for char in word:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    return characters

def sort_num(dict):
    return dict["num"]

def get_sorted_list(file_path):
    char_num_list = []
    characters = get_character_count(file_path)

    for char, num in characters.items():
        char_dict = {"char": char, "num": num}
        char_num_list.append(char_dict)
    
    char_num_list.sort(reverse=True, key=sort_num)

    return char_num_list


            