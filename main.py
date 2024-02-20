import sys

FILE_PATH = "books/frankenstein.txt"

def main():
    if not file_exists(FILE_PATH): return 1 # error out if file does not exist
    
    print(read_file(FILE_PATH))

    return 0

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