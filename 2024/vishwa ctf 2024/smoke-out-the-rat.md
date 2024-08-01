# Smoke out the rat - Digital Forensics

## Description

There was a major heist at the local bank. Initial findings suggest that an intruder from within the bank, specifically someone from the bank's database maintenance team, aided in the robbery. This traitor granted access to an outsider, who orchestrated the generation of fake transactions and the depletion of our valuable customers' accounts. We have the phone number, '789-012-3456', from which the login was detected, which manipulated the bank's employee data. Additionally, it's noteworthy that this intruder attempted to add gibberish to the binlog and ultimately dropped the entire database at the end of the heist.

Your task is to identify the first name of the traitor, the last name of the outsider, and the time at which the outsider was added to the database.

Flag format : VishwaCTF{TraitorFirstName_OutsiderLastName_HH:MM:SS}

Author : Saksham Saipatwar

FLAG FORMAT:
VishwaCTF{}

## Solution

Download the file and start doing analysis on it

```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ file DBlog-bin.000007 
DBlog-bin.000007: MySQL replication log, server id 1 MySQL V5+, server version 8.0.36
```

We can use `mysqlbinlog` to read the file

```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ mysqlbinlog DBlog-bin.000007 
/*!50530 SET @@SESSION.PSEUDO_SLAVE_MODE=1*/;
/*!40019 SET @@session.max_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
DELIMITER /*!*/;
# at 4
#240217  4:15:13 server id 1  end_log_pos 126 CRC32 0x32e61563  Start: binlog v 4, server v 8.0.36 created 240217  4:15:13 at startup
# Warning: this binlog is either in use or was not closed properly.
ROLLBACK/*!*/;
BINLOG '
IXnQZQ8BAAAAegAAAH4AAAABAAQAOC4wLjM2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAhedBlEwANAAgAAAAABAAEAAAAYgAEGggAAAAICAgCAAAACgoKKioAEjQA
CigAAWMV5jI=
'/*!*/;
# at 126
#240217  4:15:13 server id 1  end_log_pos 157 CRC32 0xea8569cb  Ignorable
# Ignorable event type 35 (MySQL Previous_gtids)
# at 157
#240218 11:24:55 server id 1  end_log_pos 236 CRC32 0x92d92a42  Ignorable
# Ignorable event type 34 (MySQL Anonymous_Gtid)
# at 236
mysqlbinlog: Character set '#255' is not a compiled character set and is not specified in the '/usr/share/mysql/charsets/Index.xml' file
zsh: segmentation fault  mysqlbinlog DBlog-bin.000007
```


```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ xxd DBlog-bin.000007 | grep 789-012-3456
00001a10: 6f6d 0c37 3839 2d30 3132 2d33 3435 3616  om.789-012-3456.
   

┌──(kali㉿kali)-[~/Desktop]
└─$ xxd -s 0x000019bf DBlog-bin.000007 | head
000019bf: 1600 4461 7461 6261 7365 2041 646d 696e  ..Database Admin
000019cf: 6973 7472 6174 6f72 0344 4241 80a0 0080  istrator.DBA....
000019df: c000 0000 0700 0000 074d 6174 7468 6577  .........Matthew
000019ef: 064d 696c 6c65 721a 006d 6174 7468 6577  .Miller..matthew
000019ff: 2e6d 696c 6c65 7240 6578 616d 706c 652e  .miller@example.
00001a0f: 636f 6d0c 3738 392d 3031 322d 3334 3536  com.789-012-3456
00001a1f: 1600 4461 7461 6261 7365 2041 646d 696e  ..Database Admin
00001a2f: 6973 7472 6174 6f72 0344 4241 80c0 0080  istrator.DBA....
00001a3f: e000 0000 0800 0000 074a 6573 7369 6361  .........Jessica
00001a4f: 0544 6176 6973 1900 6a65 7373 6963 612e  .Davis..jessica.
```