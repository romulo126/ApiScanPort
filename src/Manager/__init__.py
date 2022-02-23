import Scan as scan
import os
import datetime
from multiprocessing import Pool    
import Redis as redis

def scanear(ip, typeScan, processors_count, dir = 'Datas/'):
    path = createDir(ip, dir)
    scanProcessors(ip, typeScan, path,processors_count)
    
def get_value_redis(key):
    try:
        valuer = redis.get_value(key)
        newarray = []
        for value in valuer:
            newarray.append(value.decode('utf-8'))
        return newarray
    except Exception as e:
        return 'erro '+str(e)


def scanProcessors(ip, typeScan, path,processors_count):
    try:
        nameIpRedisScanning = str(path)+' = Scanning'
        
        redis.set_value(ip, nameIpRedisScanning)

        pool = Pool(processes=processors_count)
        ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        if typeScan == 'Fast':
            for port in ports:
                pool.apply_async(scan.scan, args=(path, ip, port,))
        elif typeScan == 'Full':
            for port in range(1,65536):
                pool.apply_async(scan.scan, args=(path, ip, port,))
        else:
            if "-" in typeScan:
                ports = typeScan.split("-")
                for port in range(int(ports[0]), int(ports[1])+1):
                    pool.apply_async(scan.scan, args=(path, ip, port,))
                    
        
            else:
                pool.apply_async(scan.scan, args=(path, ip, int(typeScan),))
        pool.close()
        pool.join()

        redis.remove_value(ip, nameIpRedisScanning)
        
        nameIpRedisfinished = str(path)+' = finished'
        redis.set_value(ip, nameIpRedisfinished)
        



    except Exception as e:
        print("Error, something is wrong",e)
        


def writeTXT(name, text):
    f = open(name, 'a')
    f.write('\n'+str(text))
    f.close()
    

def createTXT(ip, dir = 'Datas/'):
    name = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    if not os. path.isfile(dir+str(ip)+'/'+str(name)+'.txt'):
        f = open(dir+str(ip)+'/'+str(name)+'.txt','w')
        f.close()
    return dir+str(ip)+'/'+str(name)+'.txt'

def createDir(ip, dir = 'Datas/'):
    if not os. path. isdir(dir+str(ip)):
        os.makedirs(dir+str(ip))
    return createTXT(ip, dir)