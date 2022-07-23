from logging import warning
import random
from statistics import quantiles
from warnings import catch_warnings
import psycopg2
import psycopg2.extras
def getConection():
    return psycopg2.connect(dbname='postgres',user='postgres',password='152535',host='localhost')
#-----------------------------------------------------------
def criarMoldeDeStatus(nomeDaFicha,atri):
    con= getConection()
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    atri_db = ""
    for i in atri:
        if i == atri[-1]:
            atri_db +=i+" DECIMAL(3,1)"
        else:    
            atri_db +=i+" DECIMAL(3,1),"
    cod = (f"Create Table {nomeDaFicha}({atri_db})")
    cur.execute(cod)
    con.commit()
    cur.close()
    con.close()
    #@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@
def criarPersonagem(id_do_usuario):
    con= getConection()
    cur = con.cursor()
    id = random.randint(1,9999)
    #método verificar o id do 
    #try:
    nome = input("nome do personagem\n")
    rpg = input("Molde dos status do rpg no qual esse personagem faz parte\n")
    #cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name ="+"'"+rpg+"'")
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name ='fichateste'")
    values = ""
    for i in cur.fetchall():
        values +=i[0]+","
    value = tuple(values)
    values = ''.join(value[0:-1])
    status = input(values+"\n coloque os status em ordem como está em cima e separado em virgula")
    cur.execute("Insert into personagem (id,nome,rpg,id_do_usuario) values ("+id+","+rpg+","+id_do_usuario+")")
    cur.execute("insert into "+rpg+" ("+values+") Values (")
    #except:
    #    print("Deu ruim, talvez a tabela não exista. Tenta tudo minusculo")
    con.commit()
    cur.close()
    con.close()
#cur.execute("INSERT into teste (nome,senha) values (%s,%s)",("diox","123"))
#cur.execute("select*from teste")
#for linha in cur.fetchall():
#    print(linha['nome'])
#----------------------------------------------
