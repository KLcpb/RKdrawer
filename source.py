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
        
        plt.gcf().set_size_inches(18, 10)
        plt.locator_params(axis='both', nbins=10) 
        plt.ylabel(param_name)
        plt.plot(self.data[param_name])
        plt.savefig(path)
        plt.cla()
        plt.clf()

    def load_params(self,path):
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
        for param in self.params:
            self.data[param] = []
        
    def load_file(self,path):
        with open(path,'r') as file:
            ##add values from file to special variable
            for string in file.readlines():
                vals = string.split(';')
                try:
                    for i in range(len(vals)):
                        self.data[self.params[i]].append(float(vals[i]))
                except IndexError:
                    print("INVALID CONFIG FILE")
                    return
    
    def process_raw(self):
        for param in self.params:
            self.__draw(param,self.output_folder + '/RAW/' + param + '.png')

    def __detect_start(self):
        pass