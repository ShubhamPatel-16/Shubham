import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [20, 30, 5, 7, 11]
y2 = [10, 15, 25, 30, 35]

line_style = dict(marker =".",
        markersize =20,
        markerfacecolor = "yellow", 
        markeredgecolor = "black",
         linestyle ="dotted" ,
         linewidth = 3)
# plt.plot(x, y1, marker =".",
#         markersize =20,
#         markerfacecolor = "yellow", 
#         markeredgecolor = "black",
#          linestyle ="dotted" ,
#          linewidth = 3)
plt.plot(x,y1, **line_style)
plt.plot(x,y2, **line_style)
# plt.plot(x, y2, marker =".",
#         markersize =20,
#         markerfacecolor = "yellow", 
#         markeredgecolor = "black",
#          linestyle ="dotted" ,
#          linewidth = 3)

plt.show()

