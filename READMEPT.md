## Docker Scan de Porta em Python
#
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/romulo-henrique-364976133)
#
[ README - ENG](README.md)
#
### SOBRE:
- O script irá realizar uma análise de porta em um determinado servidor.
- O sistema e uma API aonde possui Duas Rotas:
    - /scan
    - /finished
- A rota /scan irá realizar a análise de porta.
- A rota /finished irá retornar o status da análise de porta para verificar se ja foi finalizado.
- O sistema irá criar um arquivo TXT com o resultado da análise de porta.

### Requerimento:

- [Docker](https://www.docker.com/)
- [Postman](https://www.getpostman.com/) ou outro cliente de HTTP

### COMO USAR:
- Configure o .env: 
    - password do Redis. 
    - Porta do Flask.
    - Porta do Redis.
    - Porta do Docker.

- Execute o docker usando o comando: ` docker-compose up -d --build `

- Abra o Postman e acesse o endereço desejado. 

### /scan Rota:
- Metodo: ` POST `
- Endereço: ` http://localhost:5000/scan ` ou ` http://ip_do_docker:5000/scan `
- Parametros:
    - `ports`: Porta que deseja realizar a análise.
    - `ip`: IP ou HOST que deseja realizar a análise.
    - `processors`: Quantidade de processadores que deseja utilizar.

- Exemplo de parametros ports:
    - `ports=80-100`
    - `ports=80`
    - `ports=Fast`
    - `ports=Full`
### Resultado:
- Retorna um json com o status da requisição.
- exemple:
    -  `{
            "status": true,
            "msg": "Scan iniciado com sucesso"
        }`
    -  `{
            "status": false,
            "msg": "motivo do erro"
        }`

### /finished Rota:
- Metodo: ` POST `
- Endereço: ` http://localhost:5000/finished ` ou ` http://ip_do_servidor:5000/finished `
- Parametros:
    - `ip`: IP ou HOST que deseja verificar a análise.

### Resultado:
- Retorna um JSON com o status da análise.
- Exemplo:
    - `{"msg":["PASTA/DATA_HORA.txt = Scanning"],"status":true}
    `
`
