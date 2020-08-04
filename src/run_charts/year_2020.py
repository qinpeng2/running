import pandas

from component.burndown import Burndown


class Year2019(Burndown):
    def read_personal_data(self):
        week_data = pandas.read_csv('../../resources/run/annual/data_2020.csv')
        return week_data['km']


if __name__ == '__main__':
    year2019 = Year2019(target=2020, periods=53, title='2020 Running Distance Burn Down Chart', xlabel = 'Burn Down by Week', ylabel='GOAL for 2020km')
    year2019.chart()
