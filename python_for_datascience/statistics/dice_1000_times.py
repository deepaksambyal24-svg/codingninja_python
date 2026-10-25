import numpy as np
import matplotlib.pyplot as plt
def roll_dice():
    rolls=np.random.randint(1,7,size=1000)
    # plot the distribution using the histogram
    plt.hist(rolls,bins=np.arange(.5,7.5,1),edgecolor='black')
    plt.title('Distribution of Rolls')
    plt.xlabel('Dice outcomes')
    plt.ylabel('Frequency')
    plt.xticks(range(1,7))
    plt.show()
roll_dice()