import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\Users\admin\skill craft internship\gender_data.txt")


df = pd.DataFrame(data)

plt.figure(figsize=(12,5))
bar_width = 0.3


plt.bar(df['Year'] - bar_width/2, df['Men'], width=bar_width, 
        color='blue', label='Men', alpha = 1)

plt.bar(df['Year'] + bar_width/2, df['Women'], width=bar_width, 
        color="#cc2473", label='Women', alpha=1)



plt.title('Population Comparison: Men vs Women (2000-2023)')
plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.grid(axis='y', linestyle='--', alpha =1)
plt.xticks(df['Year'])

plt.tight_layout()
plt.show()

