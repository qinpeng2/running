import math

import matplotlib.pyplot as plt
import pandas

target = 200
period = 31


def read_personal_data():
    daily_data = pandas.read_csv('../../resources/run/data_2020/data_202007.csv')
    return daily_data['km']


def main():
    week_target = []
    week_actual = []
    # target list
    left = target
    for i in range(period):
        period_target = round(target - target / (period -1) * i, 2)
        week_target.append(period_target if period_target > left else left)
        left = left - period_target
    # actual list
    personal_data = read_personal_data()

    total_km = 0
    for km in personal_data:
        km = str(km).strip()
        if km == '':
            continue
        total_km += round(float(km),2)
        week_actual.append(target - total_km)

    plt.figure(facecolor='#A9A9A9')
    plt.axes(facecolor='k')
    plt.axhline(0, 0, target, color='w')
    plt.axvline(0, 0, period, color='w')
    plt.title('200 km Burn Down for July')
    plt.plot(week_target)
    plt.plot(week_actual)
    plt.xlabel('Burn Down by Day. Now:{}km'.format(round(total_km, 2)))
    plt.ylabel('GOAL for 200km')
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()
