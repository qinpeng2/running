import pandas

from component.burndown import Burndown


class Year2020July(Burndown):

    def read_personal_data(self):
        daily_data = pandas.read_csv('../../resources/run/data_month_2020/data_202007.csv')
        return daily_data['km']


if __name__ == '__main__':
    burn_down = Year2020July(target=200, periods=31, title='200 km Burn Down for July', xlabel = 'Burn Down by Day.', ylabel='GOAL for 200km')
    burn_down.chart()
