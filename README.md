# Welcome to the *bookbot* project

This program reads in a book from a text file (e.g., [Frankenstein](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt)) and returns a report summarizing: 
- the word count
- the count of the letters in the text, sorted most frequent to least

To run the program, update the `file_path` variable to point to a text file on your local computer. 

To take advantage of the `.gitignore` settings, you can create a `books` folder inside the root directory and add your book file(s) there. 

```
├── books <-- create this on your local
│   ├── frankenstein.txt <-- put your book file here
├── main.py <-- update file_path here
├── README.md <-- you are currently reading this
└── .gitignore
```

The `file_path` would therefore look something like `books/frankenstein.txt` (as can be seen in the current value used in `main.py`).