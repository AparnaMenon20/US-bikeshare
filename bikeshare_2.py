import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""
# To get user input for city (chicago, new york city, washington).
    while True:
        city=input('Would you like to filter data for Chicago, New York City or Washington?  ').lower()

        if city not in ('chicago', 'new york city', 'washington'):
            print('The name of the city is invalid. Please choose from Chicago, New York or Washington.  ')

        else:
            print('You chose : ',city.title())
            break

 # To get user input for month (all, january, february, ... , june)and day filter (monday,tue,wednesday..)
    while True:
        month_filter=input('Please type a month from January, February, March, April,May,June to filter data by month or type "all" for no month filter.  ').lower()

        if month_filter not in('january','february','march','april','may','june','all'):
            print('The month you typed is invalid. Please choose from January, February, March, April,May,June or all.  ')

        else:
            print('You chose: ',month_filter.title())
            break
    while True:
        day_filter=input('Please type day of the week to filter data by day or type "all" for no day filter.  ').lower()

        if day_filter not in('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
           print('The day you typed is invalid. Please choose from Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday,or all.  ')

        else:
           print('You chose: ',day_filter.title())
           break


    print('-'*40)
    return city, month_filter, day_filter
def load_data(city, month_filter, day_filter):
    df = pd.read_csv(CITY_DATA[city])

# To convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# To extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name



# To filter by month if applicable
    if month_filter != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month_filter)+1

# To filter by month to create the new dataframe
        df =df[df['month']==month]

# To filter by day of week if applicable
    if day_filter != 'all':
# To filter by day of week to create the new dataframe


        df = df[df['day_of_week']==day_filter.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# the most common month
    most_common_month = df['month'].mode()[0]
    months=['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month_name=months[most_common_month-1].title()
    month_count=df['month'].value_counts

# to check if data is filtered by month

    if df['month'].value_counts()[most_common_month]==df['month'].count():
        print('\n The most common month: Not applicable as data is filtered by {} \n'.format(most_common_month_name))
    else:
        print ('\n The most common month is :\n', most_common_month_name)



# the most common day of the week

    most_common_day=df['day_of_week'].mode()[0]

# to check if data is filtered by day

    if df['day_of_week'].value_counts()[most_common_day]==df['day_of_week'].count():
        print('\n The most common day of the week: Not applicable as data is filtered by {}  \n'.format(most_common_day))
    else:
        print ('\n The most common day is :\n', most_common_day)


# the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    print ('\n The most common start hour is :\n',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# the most commonly used start station


    print ('\n The most commonly used start station is : \n',df['Start Station'].mode()[0])
# the most commonly used end station

    print ('\n The most commonly used end station is :\n',df['End Station'].mode()[0])


# The most frequent combination of start station and end station trip
    df['trip']=df['Start Station'] +','+df['End Station']

    print ('\nThe most frequent combination of start and end station trip is \n',df['trip'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
# total travel time

    print('\n The total trip duration is {} seconds \n'.format(df['Trip Duration'].sum()))


# the mean travel time

    print('\n The mean trip duration is {} seconds\n'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

#  counts of user types
    user_types = df['User Type'].value_counts()

#   to display the count of user types
    user_type_dict=dict(user_types)

    print('\nThe counts of different user types are: ')
    for key,value in user_type_dict.items():
        print(key,value)

# to check if gender data is available
    if 'Gender' not in df.columns:
        print('\nGender data not available\n')
    else:

 # to display gender count
        gender_count = df['Gender'].value_counts()
        gender_count_dict=dict(gender_count)
        print('\nThe counts of gender are :' )
        for key,value in gender_count_dict.items():
            print(key,value)




   # to check if birth year data is available

    if 'Birth Year' not in df.columns:
        print('\nBirth year data not available\n')

    else:
        # the most recent year of birth

        print('\n The most recent year of birth is : \n', int(df['Birth Year'].max()))

# the most common year of birth
        print('\n The most common year of birth is : \n',int(df['Birth Year'].mode()[0]))


# the earliest year of birth

        print('\n The earliest year of birth is :\n', int(df['Birth Year'].min()))





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_input(df):
    """ Displays raw data when prompted by the user."""
    while True:
        answer= input('\nWould you like to see five lines of raw data? Enter yes or no.\n')
        if answer not in ('yes','no'):
            print ('Please type either yes or no')
        else:
            if answer.lower()== 'yes':
                print(df.head())
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
