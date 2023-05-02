
import time
from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service

services=Service(ChromeDriverManager().install())

navegador=webdriver.Chrome(service=services)

navegador.get("http://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
navegador.find_element('xpath','/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Joedson")
navegador.find_element('xpath','/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("joedson.seguranca@gmail.com")
navegador.find_element('xpath','/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("(83)988526923")
navegador.find_element('xpath','/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/button').click()
input('')









#instalação da atualização do firefox
#selenium
'''navegador do firefox=geckodrive   e chrome= chromedrive'''