import Utils as hp
import Manager as manager
from flask import jsonify,request
import threading

def Routes(app):
    @app.route('/finished', methods=["POST"])
    def finished():
        ip = hp.verify_from(request.values,'ip')
        if not ip:
            return jsonify({"status":False,"msg":"IP OR HOST is required"}),200
        return jsonify({"status":True,"msg":manager.get_value_redis(ip)}),200

    @app.route('/scan', methods=["POST"])
    def scan():
        ip = hp.verify_from(request.values,'ip')
        Ports = hp.verify_from(request.values,'ports')
        processors_count = hp.verify_from(request.values,'processors_count')

        if not ip:
            return jsonify({"status":False,"msg":"IP OR HOST is required"}),200
    
        if not Ports:
            return jsonify({"status":False,"msg":"Ports is required", "types":['Full','Fast','80-100', '80']}),200

        if not processors_count:
            processors_count = 1

        try:
            threading.Thread(target= manager.scanear, args=(ip, Ports, processors_count,)).start()
            return jsonify({"status":True,"msg":"Scan started successfully"}),200
        except Exception as e:
            return jsonify({"status":False,"msg":str(e)}),200

