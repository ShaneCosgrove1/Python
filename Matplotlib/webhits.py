#import Matplotlib

import matplotlib.pyplot as plt


#create a webhits list
webHits = [743, 832, 655, 800, 937, 1016, 871, 995, 1252, 1879, 1456, 1695, 1659, 1820, 1746, 1425, 1573,
1131, 1072, 958, 870, 1012, 1063, 834]

#creating the axis and figures
fig,ax=plt.subplots()

#Set the title
ax.set_title("Web Hits Per Day")

#Set the x axis
ax.set_xlabel("Time")

#Set the y axi
ax.set_ylabel("Number of Hits")

#plot the values
ax.plot(webHits)

#show the figure
plt.show()

#save the figure
fig.savefig("WebHits",bbox="tight")