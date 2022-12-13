import matplotlib.pyplot as plt
sub=['FDS','WT','TCS','CN']
marks=[77,89,80,92]
#plt.bar(sub,marks,color="g",width=0.5,align="center",bottom=10,edgecolor="b",linewidth=2,tick_label=sub)
explode=[0.2,0.1,0.5,0.3]
plt.pie(marks,labels=sub,autopct="%1.1f%%")
plt.show()
