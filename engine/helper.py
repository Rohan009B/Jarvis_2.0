# ✅ Extract YouTube search term from command
import re


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    #define Words List like ABC, BCD , XYZ
    words = input_string.split()

    filrered_words = [word for word in words if word.lower() not in words_to_remove]

    result_string = ' '.join(filrered_words)
    return result_string

# #For Example Run This Code
# input_string = "make a phone call to rohit"
# words_to_remove = ['make','a','to','phone','call','send','message','whatsapp','']
# result = remove_words(input_string, words_to_remove)
# print(result)

