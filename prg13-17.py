Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py ======
Traceback (most recent call last):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py", line 1, in <module>
    import pandas as pd
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\__init__.py", line 58, in <module>
    from pandas.core.api import (
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\api.py", line 27, in <module>
    from pandas.core.arrays import Categorical
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\__init__.py", line 8, in <module>
    from pandas.core.arrays.categorical import Categorical
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\categorical.py", line 3, in <module>
    from csv import QUOTE_NONNUMERIC
  File "C:\Users/G SHIVAPRAKASH/OneDrive/Desktop/python\csv.py", line 3, in <module>
    reader=csv.reader(f)
AttributeError: partially initialized module 'csv' from 'C:\Users/G SHIVAPRAKASH/OneDrive/Desktop/python\csv.py' has no attribute 'reader' (most likely due to a circular import)

======= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py ======
Traceback (most recent call last):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py", line 1, in <module>
    import pandas as pd
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\__init__.py", line 58, in <module>
    from pandas.core.api import (
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\api.py", line 27, in <module>
    from pandas.core.arrays import Categorical
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\__init__.py", line 8, in <module>
    from pandas.core.arrays.categorical import Categorical
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\categorical.py", line 3, in <module>
    from csv import QUOTE_NONNUMERIC
  File "C:\Users/G SHIVAPRAKASH/OneDrive/Desktop/python\csv.py", line 3, in <module>
    reader=csv.reader(f)
AttributeError: partially initialized module 'csv' from 'C:\Users/G SHIVAPRAKASH/OneDrive/Desktop/python\csv.py' has no attribute 'reader' (most likely due to a circular import)

======= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py ======
Traceback (most recent call last):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py", line 1, in <module>
    import pandas as pd
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\__init__.py", line 58, in <module>
    from pandas.core.api import (
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\api.py", line 27, in <module>
    from pandas.core.arrays import Categorical
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\__init__.py", line 8, in <module>
    from pandas.core.arrays.categorical import Categorical
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\categorical.py", line 3, in <module>
    from csv import QUOTE_NONNUMERIC
  File "C:\Users/G SHIVAPRAKASH/OneDrive/Desktop/python\csv.py", line 3, in <module>
    reader=csv.reader(f)
AttributeError: partially initialized module 'csv' from 'C:\Users/G SHIVAPRAKASH/OneDrive/Desktop/python\csv.py' has no attribute 'reader' (most likely due to a circular import)

=========================================================== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg13.py ==========================================================
Employee Details:
   EmployeeID     Name   Department
0         101    Alice           HR
1         102      Bob  Engineering
2         103  Charlie  Engineering
3         104    David           HR
4         105      Eva    Marketing

Employee Salaries:
   EmployeeID  Salary
0         101   50000
1         102   70000
2         103   80000
3         104   55000
4         105   60000

Sales Region 1:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350

Sales Region 2:
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310

Average Salary per Department:
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64

Merged Employee Data:
   EmployeeID     Name   Department  Salary
0         101    Alice           HR   50000
1         102      Bob  Engineering   70000
2         103  Charlie  Engineering   80000
3         104    David           HR   55000
4         105      Eva    Marketing   60000
Stock Prices Data:
            Price
Date             
2024-01-01    150
2024-01-02    155
2024-01-03    152
2024-01-04    158
2024-01-05    160

Market Volume Data:
            Volume
Date              
2024-01-01    1000
2024-01-02    1100
2024-01-03    1050
2024-01-04    1150
2024-01-05    1200

Joined Stock Prices and Market Volume Data:
            Price  Volume
Date                     
2024-01-01    150    1000
2024-01-02    155    1100
2024-01-03    152    1050
2024-01-04    158    1150
2024-01-05    160    1200

Consolidated Sales Data:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310
>>> #prg 14(a)
...   
>>> 
========================================================= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg14(a).py =========================================================

Warning (from warnings module):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg14(a).py", line 13
    sns.distplot(df["salary"])
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

>>> #prg 14(b)
...   
>>> 
========================================================= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 14(b).py ========================================================
