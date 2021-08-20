# function
generates waveforms from mathematical functions

## usage
```
./function.sh {function} {a value} {b value}
```

## functions
* weierstrass function  
  `sum,n:sum+pow(a,n)*cos(pow(b,n)*pi*x`
* chaos sine. 
  `sum,n:sum+((a*sin(3/(x+1)))+(b*cos(5/(x+1)))+(a*2*(sin(6/(x+1))))+((b/2)*cos(3/(x+1)))`
