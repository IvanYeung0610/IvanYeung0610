# Team Success: Daniel Yentin, Ivan Yeung
# SoftDev
# skeleton/stub :: SQLITE3 BASICS
# Oct 2022

## Observations
1. SQL files are not readable as plaintext.
2. Shell commands are in the same style as regular code.
3. Every line must end with a semicolon ';'. If it doesn't end with semicolon it will move to a new line to continue the command until it reaches a semicolon or the squlite3 is terminated.
4. Can access list of commands in squlite3 by typing in .help command

## Prerequisite
1. Machine needs to have squlite3 on it
2. Open up a terminal
3. Enter the command ```$ sqlite3 ex1```
4. Steps 1-3 can be skipped in Windows machines by double clicking on the sqlite3.exe icon
5. Terminate the process with ctrl + d

## Tables
- Syntax for creating a new table: create table <table_name>(column1 datatype, column2 datatype, . . .)
 - Ex: ``` sqlite> create table tbl1(one text, two int); ```
- Syntax for adding elements to the table: insert into <table_name> values(column1, column2, . . .)
 - Ex: ```sqlite> insert into tbl1 values('hello!',10);```
- Syntax for viewing table: select * from <table_name>;
 - Ex: ```select * from tbl1;```
 - Ex Output:
 ```
 hello!|10
 goodbye|20
 bye bye|30
 ```
- Syntax for viewing table in different format: .mode <modetype> (choose from one of the 14 available)
  - Ex:
    ```
    sqlite> .mode table
    sqlite> select * from tbl1;
    ```
  - Ex Output:
    ```
    +---------+-----+
    |   one   | two |
    +---------+-----+
    | hello!  | 10  |
    | goodbye | 20  |
    | bye bye | 30  |
    +---------+-----+
    ```
  - Modes in squlite3:
  1. ascii
  2. box
  3. csv
  4. column
  5. html
  6. insert
  7. json
  8. line
  9. list
  10. markdown
  11. quote
  12. table
  13. tabs
  14. tcl

## Reading from a file
- 



## Resource
- https://www.sqlite.org/cli.html
