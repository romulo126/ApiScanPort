def verify_from(froms,verify):
    if froms.get(verify):
        return froms.get(verify)
    return False

def isset(array,name):
    try:
        array[name]
        return True
    except:
        return False