import configparser

config=configparser.RawConfigParser() ##configparser.RawConfigParser() this method is used to read the data from config.ini file
                                      #config.ini file we have created to save the common data

config.read("E:\\New Files\\Framework\\Framewok(Selenium)\\CT16_Project\\Configuration\\config.ini") #copied path of ini file to read config file

class Readconfig:

    @staticmethod
    def getUserEmail():
        UserEmail=config.get('Login Data','UserEmail') #'section','field' this is going to fetch data from common data section
        return UserEmail

    @staticmethod
    def getUserPassword():
        UserPassword=config.get('Login Data','Password') #'sectionname should be same as confile file','field'
        return UserPassword

##for Registration
    @staticmethod
    def getUserName():
        UserName = config.get('Registration Data','Username')  # 'section','field' this is going to fetch data from common data section
        return UserName

    @staticmethod
    def getUserPwd():
        UserPwd = config.get('Registration Data', 'UserPwd')  # 'sectionname should be same as confile file','field'
        return UserPwd

    @staticmethod
    def getUserCnfPwd():
        UserCnfPwd = config.get('Registration Data', 'UserCnfPwd')  # 'sectionname should be same as confile file','field'
        return UserCnfPwd
