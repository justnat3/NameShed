import random
import string

# Drive Function should have a size
size = 0

# Function to write random string
def Drive(size):
    if size == 0:
        raise ValueError('N/A')
    ranStr = ''
    for _ in range(size):
        ranInt = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        ranInt = ranInt - 32 if flip_bit == 1 else ranInt
        ranStr += (chr(ranInt))
    return(ranStr)

# Prefix for Machine name condition
def addPrefix(prefix):
    if len(prefix) > 10:
        print('NaS')
    else:
        return(str(prefix) + '-' + str(Drive(size)))


# Driver Code
if __name__ == "__main__":
    print('In Main: Success')
else:
    print('Imported: Success')
