import matplotlib.pyplot as plt
import numpy as np



def print_estimation():
    # Define the range for n
    n = np.arange(0, 49, 1)  # from 0 to 9

    # Define the function 2^n
    y = (n**2) * np.log2(n)
    
    return n,y 
    '''plt.figure(figsize=(8, 6))
    plt.plot(n, y,  linestyle='-', color='b', label='2^')

    # Add titles and labels
    plt.title('Estimated optimal complexity')
    plt.xlabel('$n$')
    plt.ylabel('$2$')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()'''


