import pandas as pd

df = pd.read_csv("C:/Users/cash/Downloads/motor_insure.csv/motor_data11-14lats.csv")
print(df.head(10))

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.ylabel('EFFECTIVE YEAR')
plt.xlabel('CARRYING CAPACITY')
plt.title('Effective Year vs Carrying Capacity')
plt.show()