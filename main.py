from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from classes import *



#FUNÇÕES
def esperar(tempo=0.5):
    time.sleep(tempo)

def login(login,senha):  
    navegador.get('https://sed.educacao.sp.gov.br/')
    navegador.maximize_window()
    esperar()
    navegador.find_element(By.ID, 'name').send_keys(login)
    navegador.find_element(By.ID, 'senha').send_keys(senha)
    navegador.find_element(By.ID, 'botaoEntrar').click()
    esperar()
    

def navegarFichaDoAluno(ra='',digito='X',ano='2022'):
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/ul/li[3]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/ul/li[3]/ul/li[4]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="decorAsidePopup"]/li[10]/ul/li[3]/ul/li[4]/ul/li[1]/a').click()
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="AnoLetivo"]').send_keys(ano)
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="TipoConsultaFichaAluno"]').send_keys('RA')
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="txtRa"]').send_keys(ra)
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="txtDigRa"]').send_keys(digito)
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="txtUfRa"]').send_keys('SP')
    esperar()
    navegador.find_element(By.XPATH, '//*[@id="btnPesquisar"]').click()
    esperar()


aluno=Aluno()
aluno.getRaDigito()

navegador=webdriver.Chrome()
login('INSIRA AQUI SEU LOGIN DA SED','INSIRA AQUI SUA SENHA DA SED')
navegarFichaDoAluno(aluno.ra,aluno.digito)


