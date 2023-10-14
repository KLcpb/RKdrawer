import matplotlib.pyplot as plt
import sys
import os

log_path = "./log.txt"
config_path = "./config.txt"
output_path = "./output"

try:
    log_path = sys.argv[1]
except Exception:
    print("set as an adress to the log file as the first argument") #сделать замену некорректного значения -1 на среднее арифм соседей

template = [0,0,0.3,1,1,1,1,1,1,1,0.1,-0.2,-0.2,-0.1] #template used for finding start loc

if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"[V] created output folder->{output_path}")

f = open(log_path)

data_format = []
data = []
resolution = 0
try:
    conf = open(config_path)
    for i in conf.readlines():
        if i[0] == "#":
            continue
        elif ";" in i:
            data_format = i.split(";")
            data_format[-1] = data_format[-1][:-1]
            for i in range(len(data_format)):
                data.append([])
        elif i[0:10] == "resolution":
            resolution = i[11:-1]
        elif i[0:23] == "acceleration_multiplier":
            acc_mul = float(i[24:]) #acc miultpltr

    print("[V] format grabbed from here -> ",config_path, data_format)
    print(f"[V] got acceleration multiplier -> {acc_mul}")
except:
    print("[V] no config file detected. using default...")#make cfg file
    file = open("config.txt", "w") 
    file.write("# write telemetry format here\nNUMBER;TIME;AX;AY;AZ;GX;GY;GZ\nresolution=high\nacceleration_multiplier=9.8") 
    file.close() 
    

for i in f.readlines():
    string = i.split(";")
    
    for k in range(len(data_format)):
        if k == data_format.index("AZ") or k == data_format.index("AY") or k == data_format.index("AX"):
            try:
                data[k].append(float(string[k]) * acc_mul)
            except Exception:
                print("[!] invalid line detected -> ", i)
                data[k].append(-1)
        else:
            try:
                data[k].append(float(string[k]))
            except Exception:
                print("[!] invalid line detected -> ", i)
                data[k].append(-1)
print() 
print("[V] data collected!")
print()
#----------------finding start moment-----
s = data[data_format.index("AZ")]
result = []

for i in range(len(s)):
    result.append(s[i] * template[i%len(template)])
start_n = result.index(max(result))

print(f"[V] start detected at {data[data_format.index('TIME')][start_n]} ms")

for i in range(len(data_format)):
    data[i] = data[i][start_n - 20:]

#----------------replace -1 values
for i in range(len(data_format)):
    for k in range(len(data[i])):
        left = 0
        right = 0
        it = k
        if data[i][k] == -1:
            left = data[i][k-1]
            while data[i][it] == -1:
                it+=1
            right = data[i][it]
            for j in range(k,it):
                data[i][j] = left + (j-k) * (right- left)/len(range(k,it))
                print(f"[!] replaced {left + (j-k) * (right- left)/len(range(k,it))} in {data[i][0]}")


for i in range(len(data_format)):
    if data_format[i] == "TIME" or data_format[i] == "NUMBER":
        continue

    plt.gcf().set_size_inches(18, 10)

    plt.locator_params(axis='both', nbins=10) 

    plt.ylabel(data_format[i])

    plt.plot(data[1],data[i])

    plt.savefig(f"{output_path}/{data_format[i]}.png",dpi=300)

    plt.cla()
    plt.clf()

    sys.stdout.write(f"\r\r[.] processed -> {i*100/len(data_format)} %")
    sys.stdout.flush()

sys.stdout.write(f"\r\r[V] processed -> 100 %")
sys.stdout.flush()
