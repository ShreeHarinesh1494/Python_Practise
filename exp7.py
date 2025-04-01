# #Qn 1 
# import random
# import string
# rc = "{0:06x}".format(random.randint(0,0xFFFFFF))
# rs = "".join(random.choices(string.ascii_letters,k=5))
# rv = random.randint(10,50)
# rv1 = random.randint(0,10)*7

# print(rc)
# print(rs)
# print(rv)
# print(rv1)

# #Qn 2 
# import random
# import string
# rc = random.choice(string.ascii_letters)
# rs = "".join(random.choice(string.ascii_letters) for _ in range(random.randint(3,8)))
# rs1 = "".join(random.choices(string.ascii_letters,k=5))
# print(rc)
# print(rs)
# print(rs1)

# #Qn 3 
# import types
# def uer_fucntion():
#     print("Hello World")

# lambda_fucn = lambda x: x * 2

# print(isinstance(uer_fucntion,types.FunctionType))
# print(isinstance(lambda_fucn,types.LambdaType))

# #Qn 4 
# from decimal import Decimal,ROUND_UP,ROUND_DOWN

# num = Decimal("12.345")

# roundup = num.quantize(Decimal("1.00"),rounding=ROUND_UP)
# rounddown = num.quantize(Decimal("1.00"),rounding=ROUND_DOWN)
# print(num)
# print(roundup)
# print(rounddown)


# #Qn 5 
# import copy
# lst = [1,2,3,4,5]
# shlst = copy.copy(lst)
# print(lst)
# print(shlst)

# #Qn 5
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import pearsonr

# # Step 1: Generate random x and y values
# np.random.seed(42)  # For consistent results
# x = np.random.randint(1, 100, 50)  # 50 random x values
# y = x * 0.5 + np.random.normal(0, 5, 50)  # y is slightly dependent on x with noise

# # Step 2: Convert to Pandas DataFrame
# df = pd.DataFrame({'X Values': x, 'Y Values': y})

# # Step 3: Calculate correlation using SciPy
# correlation, _ = pearsonr(df['X Values'], df['Y Values'])
# print(f"Correlation between X and Y: {correlation:.2f}")

# # Step 4: Plot scatter plot using Matplotlib
# plt.scatter(df['X Values'], df['Y Values'], color='blue', alpha=0.6, label='Data Points')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('Scatter Plot of Random Data')
# plt.legend()
# plt.grid(True)
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

np.random.seed(42)
x = np.random.randint(0,100,50)
y = x*0.5+np.random.normal(0,5,50)

df = pd.DataFrame({"Xvalues":x,"YValues":y})
corre,_ = pearsonr(df['Xvalues'],df['YValues'])
print("Correlation btw x and y is {corre:2f}")

plt.scatter(df['Xvalues'],df['YValues'],color="blue",alpha=0.6,label="Data Pts")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Data pts")
plt.grid(True)
plt.legend()
plt.show()




