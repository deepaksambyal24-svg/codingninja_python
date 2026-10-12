import pandas as pd
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series = pd.Series(data)
print(series['b':'e'])
print(series[2:4])

import numpy as np
arr= np.array(range(1,11))
print(arr)

# Write your code here
import numpy as np
import pandas as pd
roll_nu=np.array(range(23070,23081))
Student_info=pd.Series("Delhi",index=roll_nu)
print(Student_info)


import pandas as pd

import pandas as pd

data = {'Delhi': 31.0, 'Mumbai': 20.0, 'Chennai': 10.5, 'Kolkata': 14.0}
series = pd.Series(data)

# Write your code from here
ind=series.index
print(ind)




