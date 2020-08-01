import pandas

from burndown import Burndown


class Year2019(Burndown):
    def read_personal_data(self):
        week_data = pandas.read_csv('../resources/run/annual/data_2019.csv')
        return week_data['km']


if __name__ == '__main__':
    year2019 = Year2019(target=1000, periods=53, title='2019 Running Distance Burn Down Chart', xlabel = 'Burn Down by Week', ylabel='GOAL for 1000km')
    year2019.chart()
