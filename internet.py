import urllib.request
def connect(host='https://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( ‘connected’ if connect() else ‘no internet!’ )
