# -*- coding: utf-8 -*-
import re
import codecs

# import os

# os.remove('alldata.db') if os.path.exists('alldata.db') else None

# pattern = '[A-Z]\.[\s,~]+\w+'
pattern = '^([ABC\d\.]+)\s(.+)\s(\d+)'
prog = re.compile(pattern)

new_file = codecs.open('formated_bookmark.txt', 'w+', encoding='utf8')
new_file.close()

front_page_num = 46

with codecs.open("bookmarks.txt", "r", encoding='utf8') as file:
    for line in file:
        # for eachline in file:
        each_bookmark = prog.match(line)
        chapt_num = each_bookmark.group(1)
        chapt_name = each_bookmark.group(2)
        chapt_page_num = each_bookmark.group(3)
        chapt_page_num = str(int(chapt_page_num) + front_page_num)
        print(chapt_num, chapt_name, chapt_page_num)
        tmp_file = codecs.open('formated_bookmark.txt', 'a', encoding='utf8')
        plus_sign =  u'+' * (chapt_num.count(u'.')+1)
        tmp_file.write('%s"%s %s"|%s\n' \
        % (plus_sign, chapt_num, chapt_name, chapt_page_num))
        tmp_file.close()

print('Success!')


