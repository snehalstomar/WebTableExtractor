# WebTableExtractor
A tool to extract all tables from a webpage and store them as .csv files.

## Requirements:
+ Python 3.5.2 and above
+ pandas(python3 -m pip install pandas)
+ requests(python3 -m pip install requests)
+ progressbar(python3 -m pip install progressbar)

## Steps to use:
1. Clone/Download this repository. 
2. Make sure that the PWD contains "url_table_reader.py".
3. run:
$ python3 url_table_reader.py --url "<<I>The URL from which tables have to be extracted</I>>"

## Output:
+ A directory(having a substring of the input URL as its name), containing the .csv files corresponding to each table on the given webpage(URL).  
