import sys

def main():
    file_path = "books/frankenstein.txt"
    
    if not file_exists(file_path): return 1 # error out if file does not exist
    
    text = read_file(file_path) # read the file and store it in a variable
    
    report = prepare_report(text, file_path) # prepare the report

    print(report)

    return 0

def prepare_report(text, file_name):
    word_count = count_words(text)
    letters_count = count_letters(text)

    report = ""
    report += f"--- Begin report of {file_name} ---\n"
    report += f"{word_count} words found in the document.\n"
    report += "\n" # add a new line to separate the word count from the letter count

    for letter in letters_count:
        report += f"The {letter['letter']} character was founds {letter['count']} times.\n"    
    
    report += "--- End report ---"

    return report

def count_words(text):
    return len(text.split())

def count_letters(text):
    letters_count = {}

    for char in text.lower():
        if not char.isalpha(): continue # skip non-alphabetic characters    
        if char in letters_count:
            letters_count[char] += 1
        else:
            letters_count[char] = 1
    
    letters_list = [{"letter": k, "count": v} for k, v in letters_count.items()]
    letters_list.sort(reverse=True, key=sort_on_count)
    
    return letters_list

def sort_on_count(dict):
    return dict["count"]

def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()

def file_exists(file_name):
    try:
        with open(file_name, "r") as f:
            return True
    except FileNotFoundError:
        return False 

if __name__ == "__main__":
    sys.exit(main()) 