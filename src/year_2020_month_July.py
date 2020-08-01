import pandas

from burndown import Burndown


class Year2020MonthJuly(Burndown):

    def read_personal_data(self):
        daily_data = pandas.read_csv('../resources/data_202007.csv')
        return daily_data['km']


if __name__ == '__main__':
    burn_down = Year2020MonthJuly(target=200, periods=31, title='200 km Burn Down for July', xlabel = 'Burn Down by Day.', ylabel='GOAL for 200km')
    burn_down.chart()
