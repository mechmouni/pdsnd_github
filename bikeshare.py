import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       try:
        city = input("enter city: ").lower()
        CITY_DATA[city]
        break
       except KeyError:
        print('Enter a valid city')
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("enter month: ").lower()
            months.index(month)
            break
        except ValueError:
            print('Enter month name or "all"')
                  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input ("enter day: ").lower()
            days.index(day)
            break
        except ValueError:
            print('Enter day of week or "all"')
        
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['Start_End_Stations'] = df['Start Station'] + " to " + df ['End Station']
   #df['hour'].value_counts().idxmax() print(df['Start_End_Stations'].head(5))
    
        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
       
        df = df[(df['month'] == months.index(month)+ 1)]
    
    # filter by day of week     
    if day != 'all':   
        df = df[(df.day_of_week == days.index(day))]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    print("{} trips happened in {}".format(df['month'].value_counts().max(), months[df['month'].value_counts().idxmax() - 1]))
    # TO DO: display the most common day of week
    print("{} trips happened on {}".format(df['day_of_week'].value_counts().max(), days[df['day_of_week'].value_counts().idxmax()]))
          
    # TO DO: display the most common start hour
    print("{} trips started between {}:00 and {}:00".format(df['hour'].value_counts().max(), df['hour'].value_counts().idxmax(), df['hour'].value_counts().idxmax() + 1))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common Start Station: {} trips started from {}'.format( df['Start Station'].value_counts().max(), df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('Most Common End Station: {} trips ended at {}'.format( df['End Station'].value_counts().max(), df['End Station'].value_counts().idxmax()))


    # TO DO: display most frequent combination of start station and end station trip
    print('Most Common Trips: {} trips from {}'.format( df['Start_End_Stations'].value_counts().max(), df['Start_End_Stations'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("All Customers travelled a total of {} minutes".format(df['Trip Duration'].sum()/60))

    # TO DO: display mean travel time
    print("All Customers travelled an average of {} minutes".format(df['Trip Duration'].mean()/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    
    # TO DO: Display earliest, most recent, and most common year of birth
        print("\n Oldest Rider Year: {} \n Youngest Rider Year: {} \n Most Common Year of Birth: {}".format(df['Birth Year'].min(),df['Birth Year'].max(), df['Birth Year'].value_counts().idxmax()))

    except KeyError: 
        print('Gender and Birth Year info is not available for Washington')

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print('Fetched data for City:{}, Month: {}, Day:{}'.format(city,month,day))
        raw_count = 5
        while input('Do you want to see the raw data? Enter yes or no: ').lower() == 'yes': 
            print('printing next {} lines'.format(raw_count))
            print(df.head(raw_count))
            raw_count += 5
            

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
