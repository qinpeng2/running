import matplotlib.pyplot as plt


class Burndown(object):

    def __init__(self, target, periods, title, xlabel, ylabel):
        # target distance
        self.__target = target
        # statistics periods
        self.__periods = periods
        # display text
        self.__title = title
        self.__xlable = xlabel
        self.__ylable = ylabel

    def read_personal_data(self):
        pass

    def chart(self):
        period_targets = []
        period_actual = []

        left = self.__target
        # __target list
        for i in range(self.__periods + 1):
            current_target = round(self.__target - self.__target / (self.__periods) * i, 2)
            period_targets.append(current_target if current_target > left else left)
            left = left - current_target
        # actual list
        personal_data = self.read_personal_data()

        total_km = 0
        period_actual.append(self.__target)
        for km in personal_data:
            km = str(km).strip()
            if km == '':
                continue
            total_km += round(float(km), 2)
            period_actual.append(self.__target - total_km)

        plt.figure(facecolor='#A9A9A9')
        plt.axes(facecolor='k')
        plt.axhline(0, 0, self.__target, color='w')
        plt.axvline(0, 0, self.__periods, color='w')
        plt.title(self.__title)
        plt.plot(period_targets)
        plt.plot(period_actual)
        plt.xlabel(self.__xlable + ' Actually: {}km'.format(round(total_km, 2)))
        plt.ylabel(self.__ylable)
        plt.plot()
        plt.show()
