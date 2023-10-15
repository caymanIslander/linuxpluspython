import subprocess
import time
import sys
import matplotlib.pyplot as plt


class Destination:
    def __init__(self, name, min, max, avg):
        self.name = name
        self.min = min
        self.max = max
        self.avg = avg


dest1 = Destination("www.itu.edu.tr", 0, 0, 0)  # Türkiye
dest2 = Destination("www.uni-lj.si", 0, 0, 0)  # Norveç
dest3 = Destination("www.ut.ee" , 0, 0, 0)  # Almanya
dest4 = Destination("www.tcd.ie", 0, 0, 0)  # Fransa
dest5 = Destination("www.en.ru.is", 0, 0, 0)  # İspanya
dest6 = Destination("www.uni.gl", 0, 0, 0)  # İngiltere
dest7 = Destination("www.ualberta.ca" , 0, 0, 0)  # Kanada
dest8 = Destination("www.otago.ac.nz", 0, 0, 0)  # Amerika
dest9 = Destination("www.kyoto-u.ac.jp", 0, 0, 0)  # Avusturya
dest10 = Destination("www.harvard.edu", 0, 0, 0)  # Japonya

uni_list = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8, dest9, dest10]

all_time = 0

num_traceroutes = list(range(1, 1001, 100))
min_values = [[] for _ in uni_list]
max_values = [[] for _ in uni_list]
avg_values = [[] for _ in uni_list]

def commands(repeat):
    global all_time
    for uni in uni_list:
        min = 0
        max = 0
        avg = 0
        for j in range(repeat):
            command = f"traceroute -d {uni.name}"
            #print(f"Çalıştırılan Komut: {command}")
            start_time = time.time()
            command_result = subprocess.call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                             text=True)
            
            end_time = time.time()
            total_time = end_time - start_time
            all_time += total_time

            #print(total_time)

            avg += total_time
            if (j == 0):
                min = total_time
                max = total_time
                continue

            if(total_time > max):
                max = total_time
            if(total_time < min):
                min = total_time

        uni.min = min
        uni.max = max
        uni.avg = avg/repeat
    print(f"Test finished in {all_time} ms")

for num_traceroute in num_traceroutes:
    commands(num_traceroute)

# Create line graphs for min, max, and avg values for each destination
for index, uni in enumerate(uni_list):
    plt.figure(figsize=(10, 6))
    plt.plot(num_traceroutes, min_values[index], label='Min Delay')
    plt.plot(num_traceroutes, max_values[index], label='Max Delay')
    plt.plot(num_traceroutes, avg_values[index], label='Average Delay')
    plt.title(f"Traceroute Results for {uni.name}")
    plt.xlabel("Number of Traceroutes")
    plt.ylabel("Delay (ms)")
    plt.legend()
    plt.grid()
    plt.show()


commands(10)

#print(all_time)


for uni in uni_list:
    print(f"Location : {uni.name} | min delay = {uni.min} | avg delay = {uni.avg} | max delay = {uni.max}")
