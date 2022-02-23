from flask import Flask
import Route as route
import os

app = Flask(__name__, instance_relative_config=True)
route.Routes(app)
port_flask = os.getenv('PORT_FLASK')
if port_flask is None:
    port_flask = 5000

app.run(host = '0.0.0.0' , port = int(port_flask))