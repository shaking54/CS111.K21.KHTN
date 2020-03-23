import re


def counting(pathToDic , pathToTest):
    f = open(pathToDic, 'r')
    temp = f.read()
    f.close()

    myreg = r"\n"
    tudien = {}
    reg = re.compile(myreg)
    temp = reg.split(temp)
    for i in temp:
        tudien[i]=True
    # print(tudien)
    # get full dict as object

    f = open(pathToTest, 'r')
    content = f.read()
    f.close()
    myreg = r"[\s\.\n\,\?\(\)\"\:]"
    reg = re.compile(myreg)
    temp = filter(lambda x: x != '', reg.split(content))
    baibao = []
    for i in temp:
        baibao.append(i.upper());
    # print(baibao)
    exist = 0
    nonExist = 0

    for i in baibao:
        try:
            if tudien[i]:
                exist +=1
                tudien[i]= False
        except:
            nonExist+=1
            pass
    return {'counting':exist,"except":nonExist}



def calPercent(wordOfArticle,wordsOfDic):
    return (wordOfArticle/wordsOfDic)*100

answer = counting('syllables.txt','demo.txt')
print(answer)
print(calPercent(answer['counting'] , 7700))