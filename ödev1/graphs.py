import matplotlib.pyplot as plt
import numpy as np

# Data
locations = ["www.itu.edu.tr", "www.uni-lj.si", "www.ut.ee", "www.tcd.ie", "www.en.ru.is",
             "www.uni.gl", "www.ualberta.ca", "www.otago.ac.nz", "www.kyoto-u.ac.jp", "www.harvard.edu"]

min_delays = [25.07295298576355, 22.29454755783081, 1.5320186614990234, 21.16260814666748, 0.038948774337768555,
             16.720227479934692, 20.75685715675354, 15.936838150024414, 27.56974482536316, 25.124084949493408]

avg_delays = [25.07295298576355, 22.29454755783081, 1.5320186614990234, 21.16260814666748, 0.038948774337768555,
             16.720227479934692, 20.75685715675354, 15.936838150024414, 27.56974482536316, 25.124084949493408]

max_delays = [25.07295298576355, 22.29454755783081, 1.5320186614990234, 21.16260814666748, 0.038948774337768555,
             16.720227479934692, 20.75685715675354, 15.936838150024414, 27.56974482536316, 25.124084949493408]

# Create a plot for each location
bar_width = 0.2
index = np.arange(len(locations))

for i, location in enumerate(locations):
    plt.figure(figsize=(10, 6))
    
    # Combine the delay values for Min, Average, and Max
    combined_delays = [min_delays[i], avg_delays[i], max_delays[i]]
    
    plt.bar(index, combined_delays, bar_width, label="Delay Type")
    plt.title(f"Traceroute Results for {location}")
    plt.xlabel("Location")
    plt.ylabel("Delay (ms")
    
    plt.xticks(index, ["Min Delay", "Average Delay", "Max Delay"])
    
    # Set y-axis limits to zoom in
    plt.ylim(0, 30)  # Adjust the values as needed
    
    plt.grid()
    plt.legend()
    
    # Save the plot to an image file (e.g., PNG)
    plt.savefig(f"{location.replace('.', '_')}_traceroute_bar.png")
    
    # Close the plot to prevent it from being displayed
    plt.close()
