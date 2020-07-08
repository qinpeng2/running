import matplotlib.pyplot as plt
import pandas

target = 200
period = 31


def read_personal_data():
    daily_data = pandas.read_csv('../resources/data_202007.csv')
    return daily_data['km']


def main():
    week_target = []
    week_actual = []
    # target list
    for i in range(period):
        week_target.append(target - target/period * i)
    # actual list
    personal_data = read_personal_data()

    total_km = 0
    for km in personal_data:
        total_km += km
        week_actual.append(target - total_km)

    plt.figure(facecolor='#A9A9A9')
    plt.axes(facecolor='k')
    plt.axhline(0, 0, 1000, color='w')
    plt.axvline(0, 0, 53, color='w')
    plt.title('200 km Burn Down for June')
    plt.plot(week_target)
    plt.plot(week_actual)
    plt.xlabel('Burn Down by Day')
    plt.ylabel('GOAL for 200km')
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()
