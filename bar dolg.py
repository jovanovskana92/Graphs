import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('C:/Users/User/Desktop/Doc/Труд НБРМ/javen dolg.xlsx',sheet_name='dolg')

colors = ['green', 'blue']
plt.bar(df['Година'], df['Јавен долг како % од бруто - домашен производ'], color=colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()



df1 = df.set_index('Година') # setting "Years" as index
fig,ax = plt.subplots(figsize=(15,6))
df1.plot(kind='bar',ax=ax)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.set_xlabel('година', labelpad=10)
# ax.set_ylabel('% на реален пораст на БДП', labelpad=10)
ax.set_ylabel('', labelpad=10)
ax.legend(frameon=False, loc=(1.05, 0.3))
ax.figure.autofmt_xdate(rotation=45, ha='center')
ax.set_title('Јавен долг како % од БДП 2002-2021', pad=30, fontsize=14)

plt.legend(loc='best')
plt.show()
# wb.save("C:/Users/User/Desktop/javen dolg.xlsx")
