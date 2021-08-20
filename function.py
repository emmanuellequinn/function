import wave, struct, sys
from math import pow, cos, pi

# command line arguments
# TODO: better way to parse/organise these
func = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])

# control variables
# TODO: make these optional command line arguments
samples = 100000
terms = 50
normalizer = 32768/1.5

def function(func, a, b, x): 
    if func == 'weierstrass':
         return reduce(lambda sum,n:sum+pow(a,n)*cos(pow(b,n)*pi*x), range(terms), 0)
    else:
        print('invalid function')
	sys.exit()

def funcToWave(func, a, b):
    
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

if __name__ == "__main__":
    funcToWave(func, a, b)

