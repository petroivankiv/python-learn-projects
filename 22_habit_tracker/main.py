import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit


def main():
    # Звички, від яких хочу відмовитись на деякий час
    # щоб вістежити витрати часу та грошей
    habits: list[Habit] = [
        track_habit('Кава', datetime(2023, 9, 3), cost=80, minutes_used=5),
        track_habit('Алкоголь', datetime(2023, 9, 5, 22), cost=150, minutes_used=15),
        track_habit('Цукор', datetime(2023, 8, 16, 19), cost=25, minutes_used=3),
        track_habit('Цигарки', datetime(2023, 7, 16, 19), cost=70, minutes_used=3),
    ]

    # Creates a Dataframe
    df = pd.DataFrame(habits)

    # Create a nice table
    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main()
