def get_word_count(book_text):
    num_words = len(book_text.split())
    return f"Found {num_words} total words"

def get_character_count(book_text):
    character_dict = {}
    for character in book_text.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def sort_on(character_dict):
    return character_dict["num"]

def sort_dictionary(character_dict):
    sorted_list = []
    for key,value in character_dict.items():
        sorted_list.append({"char":key, "num":value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    
