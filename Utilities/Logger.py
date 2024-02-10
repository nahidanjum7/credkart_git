import  logging   #built in python



class LogGenerator:
    @staticmethod
    def logg():

                                      #given path & file name
        logfile=logging.FileHandler("E:\\New Files\\Framework\\Framewok(Selenium)\\CT16_Project\\Logs\\CredKart.log")
        # we are giving here formattor
        format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(format)
        logger = logging.getLogger()  # getting log from this method
        logger.addHandler(logfile) #every time log will get add
        logger.setLevel(logging.INFO) #set the level of log
        return logger



#as a tester we always take set level as INFO
#hirarchy of set level
#debug
#info
#warning
#error
#critical



#file ki info dni hogi
#log ka format dena hoga
#har run k tym pr log create ho ye btana hoga


