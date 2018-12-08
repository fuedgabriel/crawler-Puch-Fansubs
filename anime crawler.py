import time
import os
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By



options = webdriver.FirefoxOptions()
#options.add_argument('-headless')
driver = webdriver.Firefox(firefox_options=options)
driver.get('https://punchsubs.net/buscar-projeto/anime')
time.sleep(5)



def page(y):    
    pagina = '//*[@id="cards-search"]/section[2]/div/ul[2]/li[' + str(y) + ']/a'
    #print(pagina)
    try:
        driver.find_element(By.XPATH, pagina).click()
    except:
        driver.find_element(By.XPATH, '/html/body/main/section[2]/div/ul[2]/li[5]/a').click()      
        
        
        print("Click erro")
        '''

        print("tentativa e erro")
        pagina2 = '//*[@id="cards-search"]/section[2]/div/ul[2]/li[' + str(z) + ']/a'
        while True:
            try:
                driver.find_element(By.XPATH, pagina2).click()
                break
            except:
                z=z-1
                '''
    #//*[@id="cards-search"]/section[2]/div/ul[2]/li[2]/a

    #<a class="page" href='javascript:function Z(){Z=""}Z()'>6</a>
    '''
//*[@id="cards-search"]/section[2]/div/ul[2]/li[1]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[2]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[3]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[4]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[5]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[6]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[5]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[6]/a
//*[@id="cards-search"]/section[2]/div/ul[2]/li[5]/a
'''
def nomeEP(x):
    nome = 'li.projeto-card:nth-child('+ str(x) +')'
    #print(nome)
    a = driver.find_element(By.CSS_SELECTOR, nome).text
    print(a)

def Iniciar(y):
    images = driver.find_elements_by_tag_name('img')
    #images = driver.find_elements_by_xpath('//*[@id="cards-search"]/section[2]/div/ul[1]/li[1]/a/img')

    x=0
    page(y)
    time.sleep(4)
    for image in images:
        if x == 0:
            print("Link falso")
            x=1   
            print("")
        else:             
            nomeEP(x)
            try:
                #print image.get_attribute('src')
                #print image.find_element_by_tag_name("img")
                print(image.get_attribute('src'))
                print("")
            except :
                print("Foto falhou")
                print("")
                pass
            
            x=x+1
for ado in range(1, 178):
    Iniciar(ado)
driver.close()


#b = driver.find_element(By.CLASS_NAME, 'projeto-card').text
#c = driver.find_element(By.CLASS_NAME, 'projeto-card').text
#d = driver.find_element(By.CLASS_NAME, 'projeto-card').text


