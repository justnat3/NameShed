import api
import requests
from pyassert import assert_that

# Is Thread Alive
def threadAlive():
    resp = requests.get('http://127.0.0.1:5001')
    if resp.ok == True: print('PASS')
    else: print('FAIL')
    assert_that(resp.ok).is_true()
    
# Driver Code
if __name__ == "__main__":
    threadAlive()
