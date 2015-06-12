#!/usr/bin/python
import re
re_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
with open("input.txt") as fh_in:
    
    with open("mailout.txt","a+") as fh_out:
        for line in fh_in:
            match_list = re_pattern.findall(line)
            if match_list:
                fh_out.write(match_list[0]+"\r\n")   
