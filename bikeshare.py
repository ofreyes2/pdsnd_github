import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

#****************************************************************************************************
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city = input('Enter a city chicago, new york city, or washington: ').lower()
    while True:
        city = input('Enter a city name chicago, new york city, or washington: ').lower()
        if city in (CITY_DATA.keys()):
           #return city
           break
        else:
            print ('"{}" IS INCORRECT\n *****CHECK YOUR SPELLING OR "{}" IS NOT ON THE LIST******'.format(city,city))
            #break


#**************************************************************************************
# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter a month for {}: january, february,...,june, or all: '.format(city)).lower()
        if month in MONTHS:
            #return month
            break
        else:
            print('"{}" IS INCORRECT\n *****CHECK YOUR SPELING OR "{}" IS NOT ON THE LIST******'.format(month,month))
            #break

#*****************************************************************************************
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of the week for {} data, for the month of {} : sunday, monday,...,saturday, or all: '.format(city, month)).lower()
        if day in DAYS:
            #return day
            break
        else:
            print('"{} IS INCORRECT\n ******CHECK YOUR SPELLING OR {} IS NOT ON THE THE LIST******'.format(day,day))
            #break

#*******************************************************************************************
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel.......\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    most_common_month = MONTHS[most_common_month - 1]
    print("The most common month was: ", most_common_month.upper())

    # TO DO: display the most common day of week
    most_common_day_of_week = df['weekday'].value_counts().idxmax()
    print("The most common day of the week was: ", most_common_day_of_week.upper())

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    if most_common_start_hour >= 13 and most_common_start_hour <= 23:
        most_common_start_hour = most_common_start_hour - 12
        meridiem = 'pm'
    elif most_common_start_hour == 12:
        most_common_start_hour = most_common_start_hour
        meridiem = 'pm'
    elif most_common_start_hour == 24:
        most_common_start_hour = most_common_start_hour - 12
        meridiem = 'am'
    else:
        most_common_start_hour = most_common_start_hour
        meridiem = 'am'


    print("The most common start hour of the day was: ", most_common_start_hour,meridiem)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station : ",most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station: ", most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_start_end_staion = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequently used start and end station trip is : {}, {}".format(most_frequent_combination_start_end_staion[0], most_frequent_combination_start_end_staion[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time, " minutes.")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time : ", mean_travel_time, "minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type_count = df['User Type'].value_counts()
        print("Total:\n",user_type_count.to_string())
    else:
        print("\nNo User type column")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nThe total gender count is:\n",gender_count.to_string())
    else:
        print("\nNo Gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        year_of_birth = df['Birth Year']
        common_year_birth = int(year_of_birth.value_counts().idxmax())
        print("\nThe common year of birth is: ",common_year_birth)
        recent_year_birth = int(year_of_birth.max())
        print("The recent birth year is: ",recent_year_birth)
        earliest_year_birth = int(year_of_birth.min())
        print("The earliest birth year is: ", earliest_year_birth)
    else:
        print("\nNo Birth Year column")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
# PULL 5 ROWS OF RAW DATA AT A TIME FROM USER RESPONSE OF YES OR NO
    n=0
    while True:
        proceed = input("\n\nWould you like to see 5 blocks of raw data: yes or no?:  ").lower()

        if proceed =='yes':
            #rows = df.iloc[n:n+5]
            rows = df.iloc[n:n+5]
            n = n+5
            #row_block = rows + 5
            print("\n", rows,"\n")
        elif proceed == 'no'):
            break
        else:
            print("YOU TYPED INCORRECTLY PLEASE TYPE yes or no")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
