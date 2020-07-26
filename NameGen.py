import random
import string

# Drive Function should have a size
size = 0

def Drive(size) -> int:
    #Test Case for invalid inputs

    if size == 0 or size < 0:
        raise ValueError('Length must be more than 0')

    ranStr = ''
    for _ in range(size):
        #Create Random Int
        ranInt = random.randint(97, 97 + 26 - 1)
        #only in range 0-1, then use ranInt if bit generated is == 1 otherwise use the ranInt
        flip_bit = random.randint(0, 1)
        ranInt = ranInt - 32 if flip_bit == 1 else ranInt
        #return unicode string
        ranStr += (chr(ranInt))
    return(ranStr)

# Prefix for Machine name condition
def addPrefix(prefix) -> string:
    #Cannot be larger than 20
    if len(prefix) > 20:
        print('NaS')
    else:
        return(str(prefix) + '-' + str(Drive(size)))


# Driver Code
if __name__ == "__main__":
    print('In Main: Success')
else:
    print('\nImported: Success')
