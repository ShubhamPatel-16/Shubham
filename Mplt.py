import matplotlib.pyplot as plt
import numpy as np 


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
# # plt.plot(x, y1, marker =".",
# #         markersize =20,
# #         markerfacecolor = "yellow", 
# #         markeredgecolor = "black",
# #          linestyle ="dotted" ,
# #          linewidth = 3)

# plt.title("Line Plot", fontsize = 26, color = "blue")  # Set the title of the plot with a specific font size and color
# plt.xlabel("X-axis/Year", color = "red")  # Set the label for the x-axis with a specific font size and color
# plt.ylabel("Y-axis/Student")
# plt.plot(x,y1,color = 'red', **line_style)
# plt.plot(x,y2,color = 'blue', **line_style)   # **line_style  is used to unpack the dictionary and pass the values as keyword arguments to the plot function. This allows us to reuse the same style for multiple plots without having to repeat the same code.
# plt.plot(x,y3,color = 'green', **line_style)
 
# # plt.plot(x, y2, marker =".",
# #         markersize =20,
# #         markerfacecolor = "yellow", 
# #         markeredgecolor = "black",
# #          linestyle ="dotted" ,
# #          linewidth = 3)

# plt.xticks(x) # Set the x-ticks to be the same as the x values  
# plt.yticks(range(0, 40, 5)) # Set the y-ticks to be from 0 to 40 with a step of 5
 
# plt.show()





#Grid()

# x = [1, 2, 3, 4, 5]
# y1 = [5,10,15,20,25]


# # plt.grid()  # Add a grid to the plot
# plt.grid(axis = 'y',
#     linewidth = 0.5,
#     linestyle = 'dashed',
#     color = 'blue')  # Add a grid to the y-axis with specific line width, style, and color
# plt.plot(x,y1)
# plt.show()


# Bar chart()

# categories = ['protiens', 'carbohydrates', 'fats','fruits', 'Veges']
# values = np.array([20, 5, 10, 30, 25])

# plt.bar(categories , values)
# # plt.barh(categories , values)


# plt.title('Bar Chart', 
#           fontsize = 25,
#           color ='Blue')
# plt.xlabel('Foods')
# plt.show()


# Pie Chart()

# categories = ['protiens', 'carbohydrates', 'fats','fruits', 'Veges']
# values = np.array([20, 5, 10, 30, 25])

# plt.pie( values, 
#         labels = categories ,
#         autopct = '%1.1f%%', # autopct is used to display the percentage value on the pie chart. The format string '%1.1f%%' specifies that the percentage should be displayed with one decimal place and a percent sign.
#         explode = [0,0,0,0.9,0.1],
#         shadow = True,
#         startangle = 90) 


 

# plt.title('Pie Chart', 
#           fontsize = 25,
#           color ='Blue')
# plt.xlabel('Foods')
# plt.show()


# scatter Graph()


x1 = np.array([1, 2, 3, 4, 5]) # study hour
y1 = np.array([50,60,65,70,85]) # marks obtained

x2 = np.array([1, 3, 6, 8, 9]) # study hour
y2 = np.array([54,64,68,74,95]) # marks obtained

plt.scatter(x1,y1,
            color = 'red',
            alpha = 0.4,          # alpha use for transparency
            label = 'Student 1')  

plt.scatter(x2,y2,
            color = 'purple',
            alpha = 1,
            label = 'Student 2') 

plt.title('Test Score',
          fontsize = 22,
          color = 'Orange')
plt.xlabel('Study Hour',
           fontsize = 20,
           color = 'red')
plt.ylabel('Marks Obtained',
           fontsize = 20,
           color = 'Blue')


plt.legend()   # legend is used to display the labels for the different data series in the plot. It helps to identify which data points belong to which series based on the color and label specified in the scatter function.
plt.show()