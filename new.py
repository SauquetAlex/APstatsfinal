from datetime import timedelta, date
from bs4 import BeautifulSoup

import time
import progressbar

import requests

widgets = [' [',
           progressbar.Timer(format='elapsed time: %(elapsed)s'),
           '] ',
           progressbar.Bar('*'), ' (',
           progressbar.ETA(), ') ',
           ]

bar = progressbar.ProgressBar(max_value=1, widgets=widgets).start()

# make a date for 07-14-21
FirstDate = date(2021, 7, 14)
for num in range(662, 663):
    try:
        d = FirstDate + timedelta(days=num)
        day = (str(d.strftime("%m-%d-%y")))
        r = requests.get(
            f"https://nytcrosswordanswers.org/nyt-crossword-answers-{day}/")
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
            print("ERROR at page " + str(day) + "!")
            break
        for i in range(len(dateList)):
            fileName = (str(dateList[i])).replace(
                "<b>", "").replace("</b>", "").replace(" ", "-").replace("/", "-")
            f = open("dataTemp/" + f"{fileName}.txt", "w+", encoding="utf-8")
            f.write((str(dateList[i])).replace(
                "<b>", "").replace("</b>", "").replace("/", " ") + "\n")
            for word in ListOfWordLists[i]:
                f.write(word + "\n")
            f.write("\n")
            for prompt in ListOfPromptLists[i]:
                f.write((prompt) + "\n")
    except:
        print("ERROR at page " + str(day) + "!")
    time.sleep(0.1)
    bar.update(num)
