import webbrowser
import bs4 as bs
import sys, os
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce,'lxml')

#print(sauce)


#print(soup.title.string)

#print(soup.find_all('p'))

#for paragraph in soup.find_all('p'):
 #   print(paragraph.text)

#print(soup.get_text)

#for url in soup.find_all('a'):
 #   print(url.get('href'))
  #  data_links =[ url.get('href')]

#webbrowser.open(data_links)

#Part2

##nav = soup.nav

##for url in nav.find_all('a'):
##    print(url.get('href'))

##body = soup.body
##for paragraph in body.find_all('p'):
##    print(paragraph.text)

#for div in soup.find_all('div', class_='body'):
#    print(div.text)
#
#text = 'Sample Text to save\nNew Line!'
#
#SaveFile = open('exampleFile.txt','w')
#
#SaveFile.write(text)
#SaveFile.close()
#print('done')

data_links = []

for url in soup.find_all('a'):
    data_links.append(url.get('href'))
    print(url.get('href'))


SaveFile = open('data_links.txt','w')
SaveFile.write(str(data_links))
SaveFile.close()

print(data_links)
print('finished')
