import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y1 = [20, 30, 5, 7, 11]
# y2 = [10, 15, 25, 30, 35]
# y3 = [5, 10, 15, 20, 25]

# line_style = dict(marker =".",
#         markersize =20,
#         markerfacecolor = "yellow", 
#         markeredgecolor = "black",
#          linestyle ="solid" ,
#          linewidth = 3)
# plt.plot(x, y1, marker =".",
#         markersize =20,
#         markerfacecolor = "yellow", 
#         markeredgecolor = "black",
#          linestyle ="dotted" ,
#          linewidth = 3)

# plt.title("Line Plot", fontsize = 26, color = "blue")  # Set the title of the plot with a specific font size and color
# plt.xlabel("X-axis/Year", color = "red")  # Set the label for the x-axis with a specific font size and color
# plt.ylabel("Y-axis/Student")
# plt.plot(x,y1,color = 'red', **line_style)
# plt.plot(x,y2,color = 'blue', **line_style)   # **line_style  is used to unpack the dictionary and pass the values as keyword arguments to the plot function. This allows us to reuse the same style for multiple plots without having to repeat the same code.
# plt.plot(x,y3,color = 'green', **line_style)
 
# plt.plot(x, y2, marker =".",
#         markersize =20,
#         markerfacecolor = "yellow", 
#         markeredgecolor = "black",
#          linestyle ="dotted" ,
#          linewidth = 3)

# plt.xticks(x) # Set the x-ticks to be the same as the x values  
# plt.yticks(range(0, 40, 5)) # Set the y-ticks to be from 0 to 40 with a step of 5
 
# plt.show()





#Grid()

x = [1, 2, 3, 4, 5]
y1 = [5,10,15,20,25]


# plt.grid()  # Add a grid to the plot
plt.grid(axis = 'y',
    linewidth = 0.5,
    linestyle = 'dashed',
    color = 'blue')  # Add a grid to the y-axis with specific line width, style, and color
plt.plot(x,y1)
plt.show()