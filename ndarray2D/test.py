#!/usr/bin/env python3

import numpy as np
import example

A = np.arange(10).reshape(5,2)
B = example.length(A)

print('A = \n',A)
print('B = \n',B)
