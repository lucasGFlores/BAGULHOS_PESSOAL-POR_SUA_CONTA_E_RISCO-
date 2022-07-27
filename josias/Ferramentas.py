import random

def dado(comando1, text):
    #----------------------converter comando para variaveis-------------#
    comando1 = list(comando1)
    #1d20+3 sogers?
    if "d" in comando1:
        qtg = comando1[0:comando1.count("d")]
        if "+" in comando1:
            x = True
            lad = ""
            lados = comando1[comando1.count("d")+1:]
            while x:
                for i in lados:
                    if i == "+" or i == "-":
                        x =False
                        break
                    else:
                        lad+=i[0]
            bonus = comando1[comando1.count('d')+1:]
            y = False
            bon = ''
            for i in bonus:
                if i == '-' or i == '+':
                    y = True
                if y:
                    bon +=i[0]
            lados = lad
            bonus = int(bon)
        else:
            lados = comando1[comando1.count("d")+1:]
            print(lados)
            lados = int(''.join(lados))
            bonus=0
      #-----------------------------------------------------------------#  
    qtg = (int(qtg[0]))
    print(type(type(qtg)))
    print(lados)
    print(bonus)
    #qtg,lados,bonus = 0,text=''
    resultado = ""
    qtp = qtg
    while qtp >0:
        num = random.randint(1,int(lados))
        if num == lados and bonus == 0:
            resultado+=f"{text} ` {num+bonus} ` <--[**{num}**]{qtg}D{lados}"
        elif num == lados and bonus >0:
            resultado+=f"{text} ` {num+bonus} ` <--[**{num}**]{qtg}D{lados}+{bonus}"
        elif num == lados and bonus <0:
            resultado+=f"{text} ` {num+bonus} ` <--[**{num}**]{qtg}D{lados}{bonus}"
        elif num == 1 and bonus == 0:
            resultado+=f"{text} ` {1+bonus} ` <--[**{1}**]{qtg}D{lados}"
        elif num == 1 and bonus >0:
            resultado+=f"{text} ` {1+bonus} ` <--[**{1}**]{qtg}D{lados}+{bonus}"
        elif num == 1 and bonus <0:
            resultado+=f"{text} ` {1+bonus} ` <--[**{1}**]{qtg}D{lados}{bonus}"
        elif bonus ==0:
            resultado+=f"{text} ` {num+bonus} ` <--[{num}]{qtg}D{lados}"
        elif bonus >0 :
           resultado+=f"{text} ` {num+bonus} ` <--[{num}]{qtg}D{lados}+{bonus}"
        elif bonus<0:
            resultado+=f"{text} ` {num+bonus} ` <--[{num}]{qtg}D{lados}{bonus}"
        resultado+="\n"
        qtp = qtp-1
    print(resultado)

