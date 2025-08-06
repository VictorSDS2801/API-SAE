from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def pegar_atividades(usuario, senha):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    
    driver.get("https://ava.sae.digital/login")
    WebDriverWait(driver, 10)



    driver.find_element(By.ID, "usuario").send_keys(usuario)
    driver.find_element(By.ID, "senha").send_keys(senha)
    driver.find_element(By.ID, "btnEntrar").click()
    WebDriverWait(driver, 10)

    atividades = driver.find_elements(By.XPATH, "//*[contains(text(), 'pendente') or contains(text(), 'Atividade')]")

    if atividades:
        print("Atividades pendentes encontradas!")
        atividadess = []
        for atividade in atividades:
            atividadess.append({"atividade": atividade.text})
            
    else:
        atividadess = [
                {"atividade": "Nenhuma atividade pendente."}
        ]
        
    driver.quit()
    return atividadess
    
pegar_atividades('20230245@ccpa.com.br', '20230245@')