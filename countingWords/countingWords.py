import re
from timeit import default_timer as timer
from datetime import timedelta


def counting(pathToDic, pathToTest):
    f = open(pathToDic, 'r')
    temp = f.read()
    f.close()
    dictionary = {}
    newLineRegex = re.compile(r"\n")
    temp = newLineRegex.split(temp)
    for i in temp:
        dictionary[i] = True
    # print(tudien)
    # get full dict as object

    f = open(pathToTest, 'r')
    content = f.read()
    f.close()
    spCharRegexStr = r"[\s\.\n\,\?\(\)\"\:]"
    spCharRegex = re.compile(spCharRegexStr)
    temp = filter(lambda x: x != '', spCharRegex.split(content))
    article = []
    for i in temp:
        article.append(i.upper());
    # print(article)
    article = list(set(article))
    wordCounts = 0
    wordNotExists = 0

    for i in article:
        try:
            if dictionary[i]:
                wordCounts += 1
                # dictionary[i] = False
        except:
            wordNotExists += 1
            pass
    return {'counting': wordCounts, "except": wordNotExists}


def calPercent(wordOfArticle, wordsOfDic):
    return (wordOfArticle / wordsOfDic) * 100


aricle = ['article(400words-0.5A4).txt', 'article(2700words-3A4).txt', 'article(31000words-40A4).txt',
          'article(63000words-80A4).txt']
sysllabels = 'syllables.txt'

for i in aricle:
    start = timer()
    answer = counting(sysllabels, i)
    calPercent(answer['counting'], 7700)
    print(answer)
    end = timer()
    print('The file: '+i+' run in: ', timedelta(seconds=end - start))
