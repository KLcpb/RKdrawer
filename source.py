import matplotlib.pyplot as plt

class drawer():
    def __init__(self,output_path):
        self.data={}
        self.settings = {}
        self.params = []
        self.output_folder = output_path

    def __draw(self,param_name,path):
        if param_name == "TIME" or param_name == "NUMBER":
            return
        data_to_plot = self.data[param_name]
        param_to_plot_name = param_name
        if param_name == "ALTITUDE":
            try:
                data_to_plot = self.__process_altitude_from_pressure(self.data["PRESS"])
            except KeyError:
                raise NameError(f'Invalid params, if ALTITUDE is drawed its necessary to have PRESS in params')
            param_to_plot_name = "ALTITUDE WITH BIAS"

        
        plt.gcf().set_size_inches(18, 10)
        plt.locator_params(axis='both', nbins=10)
        plt.ylabel(param_to_plot_name)
        plt.plot(data_to_plot)
        plt.savefig(path)
        plt.cla()
        plt.clf()
    def __process_altitude_from_pressure(self,press):
        ALT_BIAS = 150
        print(f'! altitude bias set to {ALT_BIAS}')
        
        return list(map(lambda x: float(44330*(1-(x/101300)**0.1903) - ALT_BIAS),press))

    def load_params(self,path='./config.txt'):
        with open(path,'r') as file:
            #get params from config file
            for string in file.readlines():
                print(string)
                if ';' in string:
                    self.__set_params(string)
                if '=' in string:
                    stngs = string.split('=')
                    self.settings[stngs[0]] = stngs[1]
        return stngs

    def __set_params(self,string):
        self.params = string.split(';')
        self.params[-1]=self.params[-1][:-1]
        for param in self.params:
            self.data[param] = []

    def load_file(self):
        path = self.settings["logpath"][1:-2]
        with open(path,'r') as file:
            ##add values from file to special variable
            cnt=0
            for string in file.readlines():
                cnt+=1
                vals = string.split(';')
                try:
                    for i in range(len(vals)):
                        self.data[self.params[i]].append(float(vals[i]))
                except IndexError:
                    print("INVALID CONFIG FILE")
                    return -1
            return cnt
            
    def process_raw(self):
        for param in self.params:
            self.__draw(param, "./" + self.output_folder+"/" + param + '.png')
       
    def __detect_start(self):
        pass
