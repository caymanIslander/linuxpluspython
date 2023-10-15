import subprocess
import time
import sys

addr1 = "www.itu.edu.tr"    #Türkiye
addr2 = "www.uni-lj.si"    #Slovenya
addr3 = "www.ut.ee"     #Estonya
addr4 = "www.tcd.ie"    #İrlanda
addr5 = "www.en.ru.is"  #İzlanda
addr6 = "www.uni.gl"    #Grönland
addr7 = "www.ualberta.ca"   #Kanada
addr8 = "www.otago.ac.nz"   #Yeni Zelanda
addr9 = "www.kyoto-u.ac.jp" #Japonya
addr10 = "www.harvard.edu"  #Abd

uni_list = [addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10]
results = {

}

timings = {

}

all_time = 0

def animation():
    animasyon = ". .. ..."
    while True:
        for karakter in animasyon:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(0.5)  
            sys.stdout.write('\b')  
            sys.stdout.flush()



def commands():
    global all_time
    for i in range(len(uni_list)):
        current = uni_list[i]
        command = f"traceroute {current}"
        print(f"Çalıştırılan Komut: {command}")
        start_time = time.time()
        command_result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end_time = time.time()
        total_time = start_time - end_time
        all_time += total_time
        print("\n\n\n\n")
        print(total_time)
        #print(command_result)
        results.update({current: command_result})
        i+=1




commands()
#print(results)
print(all_time)
#result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#if the command is successfully executed
""" if (result.returncode == 0):
    print("Command execution successful.")
    print("Output:\n", result.stdout)
else:
    print("Couldnt execute command")
 """

