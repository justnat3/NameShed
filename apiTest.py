import requests
from pyassert import assert_that

import api

# Is Thread Alive
def threadAlive():
    resp = requests.get('http://127.0.0.1:5001')
    print('\nThread Alive test')
    if resp.ok == True: print('PASS')
    else: print('FAIL')
    assert_that(resp.ok).is_true()

# Is Gen Endpoint Alive
def GenAlive():
    resp = requests.get('http://127.0.0.1:5001/namegen')
    print('\nGen Alive test')
    if resp.ok == True: print('PASS')
    else: print('FAIL')
    assert_that(resp.ok).is_true()
    
# Driver Code
if __name__ == "__main__":
    threadAlive()
    GenAlive()
    print('\n')