import hashlib, time
def create_md5():
    m = hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()