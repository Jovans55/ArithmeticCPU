# ArithmeticCPU

Just wanted to make a cpu LOL.

You need to input the instructions as if it's assembly this read me will explain how!

# Commands

if theres an s at the end that means the result will be stored in the memory you choose

Examples will be what follows after --

Descriptions are what's in between \*\* \*\*

To start the app do python app.py, that's it.

## Syntax

### Arithmetic commands

```

** to add 2 numbers **
add {store address} {store address} -- add 1 2

adds {store address} {store address} {address to store in} -- adds 1 2 5

** to subtract 2 numbers **
sub {store address} {store address} -- sub 1 2

subs {store address} {store address} {address to store in} -- subs 1 2 5

** to divide 2 numbers **
div {store address} {store address} -- div 1 2

divs {store address} {store address} {address to store in} -- divs 1 2 5

** to multiple 2 numbers **
mul {store address} {store address} -- mul 1 2

muls {store address} {store address} {address to store in} -- muls 1 2 5
```

### Memory mangment commands

```
** to store a number to an address**
store {value} {store address} -- store 10 1

** to retrieve a number from an address**
retrieve {store address} -- store 1

** to delete a number from an address**
del {store address} -- del 1
```

### One line commands

```
** to show the memory of the cpu/fake computer**
showMem

** to show the cache of the cpu**
showCache
```

#### Note

I feel like I've added error handling for everything that can go wrong but I'm sure there's a 100 ones I missed. I did get the most common ones I believe, if you run into errors open an issue LOL
