# TrabalhoSistemasWeb
# Descrição
Este script em Python realiza a extração de dados sobre carros usados disponíveis para compra. Ele coleta informações como o nome do carro, motor, preço e quilometragem, e armazena esses dados em um arquivo CSV chamado CarrosCompra.csv.
Após a execução, um arquivo chamado CarrosCompra.csv será criado no mesmo diretório, contendo os dados dos carros extraídos.

# Estrutura do Arquivo CSV
O arquivo CSV gerado terá as seguintes colunas:

## Carro: Nome do carro
## Motor: Especificação do motor
## Preço: Preço do carro
## Km: Quilometragem do carro
Observações
O script verifica se o arquivo CarrosCompra.csv já existe e o remove antes de criar um novo, garantindo que os dados estejam sempre atualizados.
Caso ocorra um erro de conexão, uma mensagem apropriada será exibida.
