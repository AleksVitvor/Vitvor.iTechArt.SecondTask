rubles={0:'рублей', 1:'рубль', 2:'рубля', 11:'рублей', 12:'рублей', 13:'рублей', 14:'рублей', 5:'рублей'}
penny={0:'копеек', 1:'копейка', 2:'копейки', 5:'копеек', 11:'копеек', 12:'копеек', 13:'копеек', 14:'копеек', 5:'копеек'}
bignumbers={0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',10:'десять',11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'девятнадцать',20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят',60:'шестьдесят',70:'семьдесят',80:'восемьдесят',90:'девяносто',100:'сто',200:'двести',300:'триста',400:'четыреста',500:'пятьсот',600:'шестьсот',700:'семьсот',800:'восемьсот',900:'девятьсот'}
bignumbersFG={0:'ноль',1:'одна',2:'две',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',10:'десять',11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'девятнадцать',20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят',60:'шестьдесят',70:'семьдесят',80:'восемьдесят',90:'девяносто',100:'сто',200:'двести',300:'триста',400:'четыреста',500:'пятьсот',600:'шестьсот',700:'семьсот',800:'восемьсот',900:'девятьсот'}
sum=input("Введите cумму\n")
def getWordRubles(sum):
    if sum>10 and sum<15:
        return rubles.get(sum)
    else:
        if sum%10>1 and sum%10<5:
            return rubles.get(2)
        elif sum%10>5:
            return rubles.get(5)
        else:
            return rubles.get(sum%10)
def getWordPenny(sum):
    if sum>10 and sum<15:
        return penny.get(sum)
    else:
        if sum%10>1 and sum%10<5:
            return penny.get(2)
        elif sum%10>5:
            return penny.get(5)
        else:
            return penny.get(sum%10)
def getWordNumbers(sum):
    strresult=""
    for i in range(2,-1, -1):
        if sum>-1 and sum<20:
            strresult+=bignumbers.get(sum)
            return strresult
        elif sum//10**i==0:
            continue
        else:
            strresult+=bignumbers.get(sum//10**i*10**i)
            strresult+=" "
            sum-=sum//10**i*10**i
    return strresult
def getWordNumbersFG(sum):
    strresult=""
    for i in range(2,-1, -1):
        if sum>-1 and sum<20:
            strresult+=bignumbersFG.get(sum)
            return strresult
        elif sum//10**i==0:
            continue
        else:
            strresult+=bignumbersFG.get(sum//10**i*10**i)
            strresult+=" "
            sum-=sum//10**i*10**i
    return strresult
def getRublesAndPenny(sum):
    strresult=""
    str=sum.split(',')
    rubl=int(str[0])
    pen=int(str[1])
    wordrubles=getWordRubles(rubl)
    wordpenny=getWordPenny(pen)
    wordnumbers=getWordNumbers(rubl)
    wordnumberfg=getWordNumbersFG(pen)
    strresult=wordnumbers+" "+wordrubles+" "+wordnumberfg+" "+wordpenny
    return strresult
print(getRublesAndPenny(sum))