import time


class Time():
    def __init__(self):
        print("The current time is:", time.strftime("%H:%M:%S"))
        self.setTime()

    def get_hour(self):
        return self.__hours

    def get_minute(self):
        return self.__minutes

    def get_second(self):
        return self.__seconds

    def get_days(self):
        return self.__days

    def setTime(self):
        elsapsedTime = eval(input("Enter the elasped time: "))
        self.__days = elsapsedTime // 86400
        self.__hours = (elsapsedTime % 86400) // 3600
        self.__minutes = ((elsapsedTime % 86400) % 3600) // 60
        self.__seconds = (((elsapsedTime % 86400) % 3600) % 60) % 60

        print("The hour:minute:second for the elapsed time "
              + F"{self.__hours}:{self.__minutes}:{self.__seconds}"
              )


test = Time()
