## Docker Scan Port in Python
#
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/romulo-henrique-364976133)
#
[ README - PT-BR](READMEPT.md)

### ABOUT:
- The script will perform a port analysis on a given server.
- The system is an API where it has Two Routes:
    - /scan
    - /finished
- The /scan Route will perform the port analysis.
- The /finished Route will return the status of the port analysis to verify if it has been completed.
- The system will create a file with the result of the port analysis.

### REQUIREMENTS:
- [Docker](https://www.docker.com/)
- [Postman](https://www.getpostman.com/) or another HTTP client

### HOW TO USE:
- Configure the .env: 
    - password of Redis. 
    - Port of Flask.
    - Port of Redis.
    - Port of Docker.

- Execute the docker using the command: ` docker-compose up -d --build `

- Open the Postman and access the desired address.

### /scan Route:
- Method: ` POST `
- Address: ` http://localhost:5000/scan ` or ` http://ip_of_docker:5000/scan `
- Parameters:
    - `ports`: Port that you want to perform the analysis.
    - `ip`: IP or HOST that you want to perform the analysis.
    - `processors`: Number of processors that you want to use.
- Example of parameters ports:
    - `ports=80-100`
    - `ports=80`
    - `ports=Fast`
    - `ports=Full`
### Result:
- Returns a json with the status of the request.
- Example:
    -  `{
            "status": true,
            "msg": "Scan started successfully"
        }`
    -  `{
            "status": false,
            "msg": "reason of error"
        }`

### /finished Route:
- Method: ` POST `
- Address: ` http://localhost:5000/finished ` or ` http://ip_of_docker:5000/finished `
- Parameters:
- `ip`: IP or HOST you want to check the parsing status.

### Result:
- Returns a json with the status of the request.
- Example:
    -  `{
            "msg":["DIR/DATE_HORS.txt = Scanning"],"status":true
        }`
