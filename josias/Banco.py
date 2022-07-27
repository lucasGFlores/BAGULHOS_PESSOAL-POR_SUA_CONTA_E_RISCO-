from ast import Try
from cmath import pi
from logging import warning
from operator import truediv
import random
from select import select
from statistics import quantiles
import string
from tokenize import String
from warnings import catch_warnings
from webbrowser import get
import psycopg2
import psycopg2.extras
def getConection():
    return psycopg2.connect(dbname='postgres',user='postgres',password='152535',host='localhost')
#-----------------------------------------------------------
def criarMoldeDeStatus(nomeDaFicha,atri):
    con= getConection()
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        atri_db = ""
        for i in atri:
            if i == atri[-1]:
                atri_db +=i+" DECIMAL(3,1)"
            else:    
                atri_db +=i+" DECIMAL(3,1),"
        cod = (f"Create Table ficha{nomeDaFicha}(id_do_personagem int references personagem(id),{atri_db})")
        cur.execute(cod)
        con.commit()
        print("Deu certo caraio")
        cur.close()
        con.close()
    except:
        print("Deu merda")
def criarPersonagem1_id():
    #vida,nome,rpg
    #__declaração____
    id = random.randint(1,9999)
    while(verificaIdDoPersonagem(id)):
        id = random.randint(1,9999)
    return id 
    #__funcionamento do id__
def criarPersonagem2(id_do_usuario,id,nome,vida,rpg):
    con= getConection()
    cur = con.cursor()
    try:
        cur.execute(f"Insert into personagem (id,nome,rpg,id_do_usuario,vida,vidamax) values ({id},'{nome}','{rpg}',{id_do_usuario},{vida},{vida})")
        con.commit()
    except:
        print("Deu ruim, talvez a tabela não exista. Tenta tudo minusculo")

    try:
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name ='ficha{rpg}'")
        values = ""
        for i in cur.fetchall():
            values +=i[0]+","
        value = tuple(values)
        return value
    except:
        print("Deu ruim, talvez a tabela não exista. Tenta tudo minusculo")
        #------------
        #values = ''.join(value[0:-1])
        #status = input(f"{''.join(value[17:-1])}\n coloque os status em ordem como está em cima e separado em virgula\n")
        #rpg,values,id,status
def criarPersonagem3(rpg,id,values,status):
    con= getConection()
    cur = con.cursor()
    try:
        babi = (f"insert into ficha{rpg} ({values}) Values ({id},{status})")
        cur.execute(babi) #cur.execute
    
    #__enfiando coisas na ficha__
    except:
        print("Não seja gay")
    con.commit()
    cur.close()
    con.close()
def registrarMagia(idPersonagem,nome,dado,dano,descricao):
    con = getConection()
    cur =con.cursor()
    #-----------------------------------------------------
    id = random.randint(1,9999)
    while verificaIdDasMagia(id):
       id = random.randint(1,9999)
    cur.execute(f"Insert into habilidade (id,nome,dado,dano,descricao) values ({id},'{nome}','{dado}','{dano}','{descricao}')")
    con.commit()
    cur.execute(f"Insert into usa (id_da_habilidade,id_do_personagem) values ({id},{idPersonagem})")
    con.commit()
    #-----------------------------------------------------
    cur.close()
    con.close()
def verificaIdDoPersonagem(id):
    con = getConection()
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select id from personagem")
    for i in cur.fetchone():
        if i ==id:
            return True
    cur.close()
    con.close()
    return False
def verificaIdDasMagia(id):
    con = getConection()
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select id from habilidade")
    for i in cur.fetchone():
        if i == id:
            return True
    cur.close()
    con.close()
    return False
def listarPersonagem(idUser):
    con = getConection()
    cur = con.cursor()
    cur.execute(f"Select id,nome,rpg from personagem where id_do_usuario ={idUser}")
    resp ="id_____nome_____RPG\n"
    for i in cur.fetchall():
        resp +=f"{i[0]}   {i[1]}   {i[2]}\n"
    print(resp)
    cur.close()
    con.close()
def listarMagiasDoPersonagem(idPersonagem):
    con = getConection()
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #-----------------------------------------------------------------
    value = "_id________nome_\n"
    cur.execute(f"select usa.id_da_habilidade, habilidade.nome, personagem.id from usa inner join habilidade ON habilidade.id = usa.id_da_habilidade inner join personagem ON personagem.id = usa.id_do_personagem where personagem.id = {idPersonagem}")
    for i in cur.fetchall():
        value +=f"{i[0]}    {i[1]}\n"
    print(value)
    #-----------------------------------------------------------------
    cur.close()
    con.close()
def perfilPersonagem(idUser,idPersonagem):
    con = getConection()
    cur= con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #--------------------------------
    lista = ""
    cur.execute(f"select * from personagem where id ={idPersonagem} and id_do_usuario = {idUser}")
    for i in cur.fetchall():
        value =f"{i['nome']}   {i['rpg']}\nVida:{i['vida']}/{i['vidamax']}"
    print(value)
    #----------------------------------
    cur.close()
    con.close()
def setVida(idUser,idPersonagem,novaVida):
    con = getConection()
    cur = con.cursor()
    #-----------------------------------------
    cur.execute(f"Update personagem set vida = {novaVida} where id ={idPersonagem} and id_do_usuario={idUser}")
    con.commit()
    #-----------------------------------------
    cur.close()
    con.close()
def converterAtriParaMod(idUser,idP,idM):
    con = getConection()
    cur = con.cursor()
    if isString(idP):
        try:
            cur.execute(f"select id from personagem where nome = '{idP}' and id_do_usuario = {idUser}")
            idP = int(cur.fetchone()[0])
        except:
                print("ou não existe ou tem personagem duplicado")
    if isString(idM):
        try:
            cur.execute(f"select habilidade.id from usa inner join personagem ON personagem.id = usa.id_do_personagem inner join habilidade ON habilidade.id = usa.id_da_habilidade where habilidade.nome = '{idM}' and personagem.id = {idP}")
            idM = int(cur.fetchone()[0])
            
        except:
            print("tem poder com nome duplicado")
        #---------------------------------------------------------------------#
    if isInt(idP) and isInt(idM):
        cur.execute(f"select dado from habilidade where id = {idM}")
        dado = cur.fetchone()[0]
        print(dado)
        



        x = False
        atri = ''
        for i in list(dado):
            if i == "-" or i == "+":
                x =True
            if x:
                atri+=i
        print("Atributo: "+atri)
        #||| Método insano que separa as variáveis |||#
        print(separadorDeMod(atri))
        teste = separadorDeMod(atri)
        #------------------ pegar o tipo da ficha do personagem ---------------#
        cur.execute(f"select rpg from personagem where id = {idP}")
        rpg = cur.fetchone()[0]
        print(f"RPG: {rpg}")
        
        #------------------------saber qual é o atributo no dado -----------#
        coluna = ''
        lista = ''
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = 'ficha{rpg}'")
        for i in cur.fetchall():
        # aqui tem q meter os atributos do método separadorDeMod(atri)
            for l in separadorDeMod(atri):
                print(f"{l} e +{i[0]} são iguais? {l == i[0]}")
                if l == "+"+i[0]:
                    lista +=f",{i[0]}"
                lista = ''.join(list(lista))
            


            print(f"i: {i[0]}")
            if atri == "+"+i[0] or atri == "-"+i[0]:
                coluna = i[0]
        print(f"coluna: {coluna}")
        lista = lista[1:] # a variável
        print(f"lista: {lista}")
        #------------------------pegar atributo da ficha   -----------------#
        mod = 0
        
        cur.execute(f"select {coluna} from ficha{rpg} where id_do_personagem ={idP}")
        print(f"select {coluna} from ficha{rpg} where id_do_personagem ={idP}")
        # usar o len em atri
        for i in range (len(teste)):
            if "-" in teste:
                mod +=(cur.fetchone()[i])*(-1)
            else:
               mod +=(cur.fetchone()[i])  
        return mod
        cur.close()
        con.close() 
def dadoMassa(idUser,idP,idM):
    con = getConection()
    cur = con.cursor()    
    if isString(idP):
        try:
            cur.execute(f"select id from personagem where nome = '{idP}' and id_do_usuario = {idUser}")
            idP = int(cur.fetchone()[0])
        except:
                print("ou não existe ou tem personagem duplicado")
    if isString(idM):
        try:
            cur.execute(f"select habilidade.id from usa inner join personagem ON personagem.id = usa.id_do_personagem inner join habilidade ON habilidade.id = usa.id_da_habilidade where habilidade.nome = '{idM}' and personagem.id = {idP}")
            idM = int(cur.fetchone()[0])
            
        except:
            print("tem poder com nome duplicado")
    #---------------------------------------------------------------------#
    if (isInt(idP) and isInt(idM)):
        print(f"select dado from habilidade where id = {idM}")
        cur.execute(f"select dado from habilidade where id = {idM}")
        dado = cur.fetchone()[0]
        x = True
        atri = ''
        for i in list(dado):
            if i == "-" or i == "+":
                x =False
            if x:
                atri+=i
        return atri   
def nomeDaMagia(idUser,idP,idM):
    con = getConection()
    cur = con.cursor()
    if isString(idP):
        try:
            cur.execute(f"select id from personagem where nome = '{idP}' and id_do_usuario = {idUser}")
            idP = int(cur.fetchone()[0])
        except:
                print("ou não existe ou tem personagem duplicado")
    if isString(idM):
        try:
            cur.execute(f"select habilidade.id from usa inner join personagem ON personagem.id = usa.id_do_personagem inner join habilidade ON habilidade.id = usa.id_da_habilidade where habilidade.nome = '{idM}' and personagem.id = {idP}")
            idM = int(cur.fetchone()[0])
            
        except:
            print("tem poder com nome duplicado")
    
    cur.execute(f"select habilidade.nome from usa inner join habilidade on habilidade.id = usa.id_da_habilidade inner join personagem on personagem.id = usa.id_do_personagem where personagem.id = {idP} and habilidade.id = {idM}")
    return cur.fetchone()[0]
    con.close
    cur.close()
def separadorDeMod(atri):
        #atri = "-inteligencia-batata+xampson+cu-poter" #demonstração
        atris = []
        v = atri
        i = (atri.replace("+","-").split("-")) #atributos
        i.pop(0)
        for l in i:
            v =''.join(v.split(l))
        o = list(v) #sinais para mods
        for x in range(len((atri.replace("+","-").split("-")))-1):
            atris.append(f"{o[x]}{i[x]}")
        return atris
def deletarPersonagem(idUser,idPersonagem):
    con = getConection()
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f"select * from personagem where personagem.id_do_usuario = {idUser} and  personagem.id = {idPersonagem}")
    rpg = cur.fetchone()['rpg']
    if cur.fetchone() == '':
        return "Esse id não é do personagem\n     Ou     \nO personagem não é teu"
    else:
        d = []    
        cur.execute(f"delete from ficha{rpg} where id_do_personagem = {idPersonagem};")
    #-------------------------------------------------------------------------------------#
        cur.execute(f"select usa.id_da_habilidade from usa where usa.id_do_personagem ={idPersonagem}")
        for i in cur.fetchall():
            d.append(i)
        print(d)
        cur.execute(f"delete from usa where id_do_personagem = {idPersonagem}")
        for i in d:
            if i[0] == None:
                print('sogers?')
            else:
                cur.execute(f"delete from habilidade where id = {i[0]}")
        cur.execute(f"delete from personagem where id = {idPersonagem}")
        
        con.commit()
    cur.close()
    con.close()
def isInt(value):
    #print(f"{value}")
    #print(type(value) == type(777))
    return (type(value) == type(777))
def isString(value):
    return (type(value) == type("boger"))
def teste(idUser,idP,idM):

    con = getConection()
    cur = con.cursor()
    try:
        cur.execute(f"select id from personagem where nome = '{idP}' and id_do_usuario = {idUser}")
        idP = int(cur.fetchone()[0])
        print(idP)
    except:
        print("ou não existe ou tem personagem duplicado")
    try:
        cur.execute(f"select id from habilidade where nome ='{idM}' ")
        idM = int(cur.fetchone()[0])
        print(idM)
    except:
        print("tem poder com nome duplicado")
        #---------------------------------------------------------------------#
    if isInt(idP) and isInt(idM):
        cur.execute(f"select dado from habilidade where id = {idM}")
        dado = cur.fetchone()[0]
        x = False
        atri = ''
        for i in list(dado):
            if i == "-" or i == "+":
                x =True
            if x:
                atri+=i
        print("Atributo: "+atri)
        #------------------ pegar o tipo da ficha do personagem ---------------#
        cur.execute(f"select rpg from personagem where id = {idP}")
        rpg = cur.fetchone()[0]
        print(rpg)
        
        #------------------------saber qual é o atributo no dado -----------#
        coluna = ''
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = 'ficha{rpg}'")
        for i in cur.fetchall():
            if atri == "+"+i[0] or atri == "-"+i[0]:
                coluna = i[0]
        print(coluna)
        #------------------------pegar atributo da ficha   -----------------#
        mod = 0
        cur.execute(f"select {coluna} from ficha{rpg} where id_do_personagem ={idP}")
        mod = int(cur.fetchone()[0])
        print(mod)
        cur.close()
        con.close()    

#cur.execute("INSERT into teste (nome,senha) values (%s,%s)",("diox","123"))
#cur.execute("select*from teste")
#for linha in cur.fetchall():
#    print(linha['nome'])
#----------------------------------------------
