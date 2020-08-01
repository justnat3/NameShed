import requests
from pyassert import assert_that

import api

# Is Thread Alive
def threadAlive():
    resp = requests.get('http://127.0.0.1:5000')
    print('\nThread Alive test')
    if resp.ok == True:
        print('PASS')
    else:
        print('FAIL')
    assert_that(resp.ok).is_true()

# Is Gen Endpoint Aliv
def GenAlive():
    resp = requests.get('http://127.0.0.1:5000/namegen')
    print('\nGen Alive test')
    if resp.ok == True:
        print('PASS')
    else:
        print('FAIL')
    assert_that(resp.ok).is_true()

# POST Create Testing -> First: can we hit the endpoint | Second: Can we create a new object from that post in the URL
def PrefixAlive():
    try:
        print('\nPrefixAlive Test')
        resp = requests.get(
            'http://127.0.0.1:5000/prefixGen?prefix=Test&size=1')
        if resp.ok == True:
            print('PASS')
        else:
            print('FAIL')
    except ConnectionError:
        print('sorry')


# Driver Code
if __name__ == "__main__":
    threadAlive()
    GenAlive()
    PrefixAlive()
    print('\n')
