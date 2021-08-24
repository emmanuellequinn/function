import wave, struct, sys
from math import pow, cos, sin, pi

# command line arguments
# TODO: better way to parse/organise these
# * add samples, terms, normalizer as optional arguments
func = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])

# control variables
# TODO: make these optional command line arguments
samples = 100000
terms = 50
normalizer = 32768/1.5

# valid functions
# TODO: is there a better way to organise/define these?
# * add samples, terms and normalizer as options
def function(func, a, b, x): 
    if func == 'weierstrass':
        return reduce(lambda sum,n:sum+pow(a,n)*cos(pow(b,n)*pi*x), range(terms), 0)
    
    if func == 'chaossine':
        # f(x) = (2*sin(3/x))+(3*cos(5/x))+(4*sin(6/x))+(1*cos(3/x))
        # from https://computing.dcu.ie/~humphrys/Notes/Neural/chaos.html 
        return reduce(lambda sum,n:sum+((a*sin(3/(x+1)))+(b*cos(5/(x+1)))+(a*2*(sin(6/(x+1))))+((b/2)*cos(3/(x+1)))), range(terms), 0)
    
    else:
        print('invalid function')
	sys.exit()

# function to wave generator
# TODO: more customisation:
# * change length?
# * loops?
# * if samples/terms/normalizer can be added to the command, can they be optionally added to the output file name?
def funcToWave(func, a, b):
    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)

    output = wave.open("{}-{}-{}.wav".format(func, a, b), 'w')
    output.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))
    
    print('progress (%):'),
    for i in range(samples):
        x = float(1000*i)/samples
        value = normalizer * function(func, a, b, x)    

        if i%5000==0: print(int(100*float(i)/samples)),; sys.stdout.flush()
    
        packed_value = struct.pack('l', int(value))
        output.writeframes(packed_value)

    output.close()

###

if __name__ == "__main__":
    funcToWave(func, a, b)

