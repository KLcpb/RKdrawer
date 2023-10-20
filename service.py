import matplotlib.pyplot as plt
def get_altitude(data,data_format):
    alt = 0
    v = 0
    prev_alt = 0 
    for i in range(1,len(data[data_format.index('AZ')])):
        dt = data[1][i] - data[1][i-1]
        v = v + dt * (data[data_format.index('AZ')][i] - 9.81)
        prev_alt = alt
        alt = alt + v * dt 
        if alt - prev_alt <= 0:
            break
    return alt
        
def save_plot(data,data_format,param,resolution,output_path):
    plt.gcf().set_size_inches(18, 10)

    plt.locator_params(axis='both', nbins=10) 

    plt.ylabel(data_format.index(param))

    plt.plot(data[1],data[data_format.index(param)])

    plt.savefig(f"{output_path}/{param}.png",dpi=300)

    plt.cla()
    plt.clf()

def save_plot_value(data,values,name,output_path):
    plt.gcf().set_size_inches(18, 10)

    plt.locator_params(axis='both', nbins=10) 

    plt.ylabel(name)

    plt.plot(data[1],values)

    plt.savefig(f"{output_path}/{name}.png",dpi=300)

    plt.cla()
    plt.clf()

def plot(a):

    plt.plot(a)
    plt.show()