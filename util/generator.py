import random
import string


# Drive Function should have a size
def Drive(size) -> string:

    if size == 0 or size < 0:
        return('Length must be more than 0')

    ranStr = ''
    for _ in range(size):
        ranInt = random.randint(97, 97 + 26 - 1)
        # only in range 0-1, substract 32 ranInt if bit generated is == 1
        # otherwise return the ranInt
        flip_bit = random.randint(0, 1)
        ranInt = ranInt - 32 if flip_bit == 1 else ranInt
        ranStr += (chr(ranInt))
    print(size)
    return(ranStr)

# Prefix for Machine name condition
def addPrefix(prefix, size) -> string:
    return(str(prefix) + str(Drive(size)))


# Driver Code
if __name__ == "__main__":
    Drive(2)
    print('In Main: Success')
else:
    print('\nImported: Success')
