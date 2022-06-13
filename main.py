#DEPENDENCIAS
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#CLASSES
class Aluno:
    def __init__(self,ra='',digito='',nome='',cidadeNascimento='',dtNascimento='',ufNascimento=''):
        self.ra=ra
        self.digito=digito
        self.nome=nome
        self.cidadeNascimento=cidadeNascimento
        self.dtNascimento=dtNascimento
        self.ufNascimento=ufNascimento

    def getRaDigito(self):
        self.ra=input('Insíra o RA:\n')
        self.digito=input('Insíra o Dígito do RA:\n')
        


#CONSTANTES

#FUNÇÕES DE ROTINA
def esperar(tempo=1):
    time.sleep(tempo)

def login(login='INSIRA SEU LOGIN',senha='INSIRA SUA SENHA'):

    esperar()
    navegador.find_element(By.ID, 'name').send_keys(login)
    navegador.find_element(By.ID, 'senha').send_keys(senha)
    navegador.find_element(By.ID, 'botaoEntrar').click()
    esperar(3)

def baixarBoletins():
    anos=[2018,2019,2020,2021]
    esperar()
    navegador.find_element(By.ID, 'txtNrRa').send_keys(aluno.ra)
    esperar()
    navegador.find_element(By.ID, 'txtNrDigRa').send_keys(aluno.digito)
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="ddlUfRa"]').send_keys('SP')
    esperar()
    for x in anos:
        navegador.find_element(By.XPATH, '//*[@id="txtNrAnoLetivo"]').send_keys(x)
        esperar()
        navegador.find_element(By.XPATH, '//*[@id="frmBoletim"]/fieldset/div[3]/button').click()
        esperar(2)

def getDadosFromFichaAluno():
        esperar()
        navegador.find_element(By.XPATH, '//*[@id="TipoConsultaFichaAluno"]').send_keys('RA')
        esperar(2)
        navegador.find_element(By.XPATH, '//*[@id="txtRa"]').send_keys(aluno.ra)
        esperar()
        navegador.find_element(By.XPATH, '//*[@id="txtDigRa"]').send_keys(aluno.digito)
        esperar()


#FUNÇÕES DE NAVEGAÇÃO

def navegarBoletim(): #navega até a página Boletim Escolar por Aluno
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[14]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[14]/ul/li[1]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[14]/ul/li[1]/ul/li[2]/a').click()
    esperar()

def navegarFichaDoAluno():#navega até a página Ficha do ALuno
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/ul/li[3]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/ul/li[3]/ul/li[4]/a').click()  
    esperar()  
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/ul/li[3]/ul/li[4]/ul/li[1]/a').click()  
    esperar()  


#MAIN

aluno=Aluno()
navegador=webdriver.Chrome()
navegador.get('https://sed.educacao.sp.gov.br/')
navegador.maximize_window()
login()
navegarFichaDoAluno()
esperar()
navegador.find_element(By.XPATH, '//*[@id="TipoConsultaFichaAluno"]').send_keys('Nome Completo')
esperar()
navegador.find_element(By.XPATH, '//*[@id="txtNomeCompleto"]').send_keys('Eduardo Henrique Silva Nabha')
esperar()
navegador.find_element(By.XPATH, '//*[@id="btnPesquisar"]').click()
esperar()
maeweb= navegador.find_element(By.XPATH, '//*[@id="tabelaDados"]/tbody/tr/td[6]')
esperar()
teste= maeweb.text
print(teste)

#TESTES
