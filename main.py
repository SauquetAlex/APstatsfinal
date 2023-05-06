import requests
from bs4 import BeautifulSoup
for j in range(34, 128):
    r = requests.get(f"https://nytcrosswordanswers.org/nyt-crossword-puzzles/page/{j}/")
    soup = BeautifulSoup(r.content, "html.parser")

    page = soup.find('main', id="main")
    date = page.findAll('h2', class_="entry-title")
    dateList = []
    for el in date:
        dateList.append(el.find('a').text)

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

    for i in range(len(dateList)):
        fileName = (dateList[i]).split()[3].replace("/","-")
        f = open(f"{fileName}.txt", "w+")
        f.write(dateList[i] + "\n")
        for word in ListOfWordLists[i]:
            f.write(word + "\n")
        f.write("\n")
        for prompt in ListOfPromptLists[i]:
            f.write(prompt + "\n")
    print(j)