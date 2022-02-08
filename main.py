from bs4 import BeautifulSoup
import os
import sys

#get current path
print(sys.path[0])

#read index file from current directory
with open(os.path.join(sys.path[0], "index.html"),'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tag = soup.find('p')
    print(tag)
    tags = soup.findAll('p')
    print(tags)
    print(tag.text)