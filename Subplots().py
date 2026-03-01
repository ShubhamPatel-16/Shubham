import matplotlib.pyplot as plt
import numpy as np

# Subplots()

x = np.array([1,2,3,4,5])
figure , axes = plt.subplots(2,2)  #(a,b)= (row,columns)

axes[0,0].plot(x,x*2,color = 'red')  #[0,0] is used to 
axes[0,0].set_title('Plot 1') # Set the title for the first subplot

axes[0,1].bar(x,x**2, color = 'Blue') #[0,1] is used to access the second subplot
axes[0,1].set_title('Plot 2') # Set the title for the second subplot

axes[1,0].scatter(x,x**3, color = 'Green') 
axes[1,0].set_title('Plot 3')

axes[1,1].plot(x,x**4, color = 'orange') 
axes[1,1].set_title('Plot 4')

plt.tight_layout() # Adjust the spacing between subplots to prevent overlap
plt.show()