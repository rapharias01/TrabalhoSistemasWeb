import requests
import bs4
import os

url = "https://www.mobiauto.com.br/comprar/carros-usados/es-vitoria"

def getCarros():
    response = requests.get(url)

    if response.status_code == 200:

        if os.path.exists("CarrosCompra.csv"):
            os.remove("CarrosCompra.csv")

        print("OK! Processando dados...")

        write = "Carro;Motor;Preço;Km"

        soup = bs4.BeautifulSoup(response.text, 'html.parser')
            
        divs = soup.find_all('div', class_='css-1qtpr08')
            
        for div in divs:
            Carro_div = div.find('h2', class_='css-19o6tnu')
            carro = Carro_div.text.strip() if Carro_div else "Título não encontrado"

            Motor_div = div.find('h3', class_='css-bdiaeq')
            motor = Motor_div.text.strip() if Motor_div else "Descrição não encontrada"

            preco_div = div.find('p', class_='css-13y9uqe')
            preco = preco_div.text.strip() if preco_div else "Preço não encontrado"

            Km_div = div.find('div', class_='css-h65h5j')
            km = Km_div.text.strip() if Km_div else "Km não encontrada"

            write += "\n"+carro+";"+motor+";"+preco+";"+km+";"

            print(f"Carro: {carro}")
            print(f"Motor: {motor}")
            print(f"Preço: {preco}")
            print(f"Km: {km}")
            print('-' * 40)


        f = open("CarrosCompra.csv", "a")
        f.write(write)
        f.close()    
    else:
        print("Erro de conexão\n")
getCarros()