Roboroboland Python Study Package(v 0.0.0.2)
=================================
> This package is about roboroboland's python study. It includes from basic calculator examples to advanced serial communication multi threading code.

# To start

## Install Library
To Start, Please install following packages

1. pyserial 
2. numpy
3. pandas

# General

## calculator
1. To Start  
Write down this code on the top of your source    
```
from rland_py_study import calculator.Calculator()
``` 

2. class:Calulator  
- variables : 
    - self._result = 0

- functions :
    - result(self):
        - return : self._result
    - add(self, num) : 
        - add 'num' and '_result'  
        - return : self._result  
    - sub(self, num) : 
        - subtract 'num' from '_result'  
        - return : self._result  
    - mul(self, num) : 
        - multiply '_result' by 'num'    
        - return : self._result  
    - div(self, num) : 
        - divide '_result' by 'num'  
        - return : self._result  
    - reset(self):
        - reset '_result' to zero
        - return : None

3. Example code

```Python:calculator_ex.py
from rland_py_study import *

_cal = calculator.Calculator()
while(1):
    _input = str(input("Please insert number and operator\nPresent value : "+str(_cal.result())+"\n(ex. +10 or -10, quit:q, reset:r)\ninput : "))
    if _input[0] == '+':
        print("Add")
        _input=_input[1:]
        _cal.add(float(_input))
    elif _input[0] == '-':
        print("Sub")
        _input=_input[1:]
        _cal.sub(float(_input))
    elif _input[0] == '*':
        print("mul")
        _input=_input[1:]
        _cal.mul(float(_input))
    elif _input[0] == '/':
        print("Div")
        _input=_input[1:]
        if(float(_input)==0):
            print("can't divided by 0")
        else:
            _cal.div(float(_input))
    elif _input[0] == 'r':
        _cal.reset()
        print("Calculator is reset")
    elif _input[0] == 'q':
        exit()
    else:
        print("Wrong input. Please insert right direction.")
```

# Serial
This library is to use Serial communication with external hardware(ex. RS board, Cube, R drone ...)

## basic

1. To Start  
Write Down this code on the top of your source. Package 'pyserial' must be installed to use it.
```
from rland_py_study.serial import *
```
2. class:SerialBasic  
- variables : 
    - self.robot = None
    - self.process = None

- functions :
    - port_search(self):
        - Search COM port of user's computer and prints their names.
        - return : None
    - port_open(self, port):
        - Try to open port to connect device with computer. If openning process succeed, they will be connected. If openning process failed, port will be closed.
        - return : None
    - port_search(self):
        - If there's a connected device, disconnect it from user's computer.
        - return : None

3. Example
```
#(will be updated soon)
```
