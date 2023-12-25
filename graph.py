import pandas as pd
import matplotlib.pyplot as plt
#
# # Import Excel spreadsheet data into a pandas DataFrame
# file_path = 'C:/Users/User/Desktop/time.xlsx'
# df_groups = pd.read_excel(file_path, header=[0, 1], index_col=0)
#
# print(df_groups)
#
# # Create figure with single Axes
# fig, ax = plt.subplots(figsize=(7,4))
#
# # Select colors for each group and plot each group by selecting the
# # cross-sections of the DataFrame at the group level
# colors = ['tab:red', 'tab:orange']
# for group, color in zip(df_groups.columns.levels[0], colors):
#     df_groups.plot(y=group, color=color, ax=ax)
#
# # Additional formatting
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.set_xlabel('Година', labelpad=10)
# ax.set_ylabel('% на пораст на БДП', labelpad=10)
# ax.legend(frameon=False, loc=(1.05, 0.3))
# ax.set_title('РАСТ НА БДП', pad=30, fontsize=14)
#
# plt.show()



import numpy as np # numerical python
import pandas as pd # pannel datasets
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('C:/Users/User/Desktop/Doc/Труд НБРМ/time.xlsx',sheet_name='bdp')
print(df.head())

df1 = df.set_index('година') # setting "Years" as index
fig,ax = plt.subplots(figsize=(15,6))
df1.plot(kind='line',ax=ax, marker='o')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('година', labelpad=10)
ax.set_ylabel('% на реален пораст на БДП', labelpad=10)
ax.set_ylabel('', labelpad=10)
ax.legend(frameon=False, loc=(1.05, 0.3))
ax.figure.autofmt_xdate(rotation=45, ha='center')
ax.set_title('Стапкa на реален пораст на БДП и инфлација 2000-2021', pad=30, fontsize=14)

plt.legend(loc='best')
plt.show()