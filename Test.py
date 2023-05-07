import requests
from bs4 import BeautifulSoup

r = requests.get(
    f"https://nytcrosswordanswers.org/nyt-crossword-puzzles/page/65/")
soup = BeautifulSoup(r.content, "html.parser")
page = soup.find('main', id="main")
date = page.findAll('div', class_="entry-content clear")
dateList = []
for el in date:
    dateList.append(el.find('b'))
words = page.findAll('div', class_="nywrap")
ListOfWordLists = []
ListOfPromptLists = []
for word in words:
    tempWords = []
    tempPrompts = []
    for el in word.findAll('span'):
        tempWords.append(el.text)
    for el in word.findAll('a'):
        tempPrompts.append(el.text)
    ListOfWordLists.append(tempWords)
    ListOfPromptLists.append(tempPrompts)
dateList = [date for date in dateList if date is not None]
if (len(dateList) != len(ListOfWordLists)):
    print("ERROR at page " + str(65) + "!")
for i in range(len(dateList)):
    fileName = (str(dateList[i])).replace(
        "<b>", "").replace("</b>", "").replace(" ", "-")
    f = open("Data/" + f"{fileName}.txt", "w+", encoding="utf-8")
    f.write((str(dateList[i])).replace("<b>", "").replace("</b>", "") + "\n")
    for word in ListOfWordLists[i]:
        f.write(word + "\n")
    f.write("\n")
    for prompt in ListOfPromptLists[i]:
        f.write((prompt) + "\n")
