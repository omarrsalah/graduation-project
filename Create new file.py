

class my_class:
   _data_fd = None

   def __init__(self,create,filename):
       if(create):
           self._data_fd = open(filename,'w')

   def __del__(self):
       if(self._data_fd != None):
           self._data_fd.close()

   def measureSample(self):
       ##do something here
       outFile = self._data_fd
       outFile.write('{0} || Concentration: {1}'.format(timeStr, Conc3SD))


if __name__ == '__main__':
    timeStr = time.strftime('%m-%d-%Y_%H_%M_%S_%Z') #use unerscore instead of spaces
    filename = "{0}.{1}".format("Data.txt",timeStr)
    imy_class = my_class(1,filename)
    imy_class.measureSample()
    imy_class.measureSample() ##call multiple times the fd remains open for the lifetime of the object
    del imy_class   ### the file closes now and you will have multiple lines of data