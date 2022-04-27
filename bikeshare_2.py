import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

        city= input('To explore more data please enter city name chicago, new york city or washington:  ').lower().strip()
        # cities = ['chicago' , 'new york city' , 'washington']
        # use if condition to handle the user input for required cities 
        if city in CITY_DATA :
                print('Pereparing,,, \n \n Data Is Loading For your city {}'.format(city))
                break 
        else:
        
             print('Not Available  ,  Data For chicago, new york city or washington only')
       # use while loop with condition true to loop no matter th inputs  and if condition to handle the user inputs for months
    while True:
        month = input('Kindly Choose From The Available Months\n \n" january:june "or "all":  ').lower().strip()
        months = ['january', 'february', 'march','april','may','june','all']
       
        if month in months :
            print('Pereparing,,, \n \n Data Availble for the month {} you entered '.format(month))
            break    # use break to break the loop when the input is correct
         
        else:
            print('Please Enter The Correct Month')

      

    while True:
        day = input('Kindly Choose Day To Explore Your Data Or All: ').lower().strip()
        days = [ 'monday','tuesday','wensday','thursday','friday','saturday','sunday','all']

        if day in days:
            print('Pereparing,,,,, \n \n Data Availble for the day {} you entered '.format(day))
            break
        
        else:
            print('Please Enter The Correct Day')


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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

    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    # change start time column into date time 
    df['Start Time'] =  pd.to_datetime(df['Start Time'])

    # create new columns for day and month from start time columns 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() # use new .day_name() method

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month =  df['month'].mode()[0] # use mode() method to extract common month with indixing [0]
    print('common months : {}'.format(popular_month))
    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0] # use mode() method to extract common month with indixing [0]
    print('common days : {}'.format(popular_day))


    # display the most common start hour

    # create hour column to get the most common hour by mode() method and indixing [0]
    df['hour'] = df['Start Time'].dt.hour
    popular_hour =  df['hour'].mode()[0]
    print('common hours : {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0] # use mode()method and indixing from [0]
    print('Common Start Station : {}'.format(popular_start_station))

    # display most commonly used end station

    popular_end_station = df['End Station'].mode()[0] 
    print('Common End Station:{}'.format(popular_end_station))


    # display most frequent combination of start station and end station trip

    start_end_combination = 'from' + ' ' + popular_start_station + ':' + popular_end_station
    print('Most frequent combination of start station and end station trip : {} '.format(start_end_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print(f'The Total Time Of Trip Duration is: {total_travel_time}')

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print(f' Average Travel Time for trips : {average_travel_time}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    types_for_users = df['User Type'].value_counts()
    print(f'User Types of Trips: {types_for_users}')


    # Display counts of gender
    # washington csv file has no gender column so i will use if condtion to not have errors during run time 
    if 'Gender' in df :
        trips_gender = df['Gender'].value_counts()
        print(f'Displaying Gender Counts For You \n\n: {trips_gender}')
    else:
        print('\n \n Gender Counts Not Available For Washington City')
        
    # washington csv file has no birth year column so, i will use ( if condtion )to not have errors during run time 
    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        earliest_birthyear = df['Birth Year'].min()
        print('\n \n Earliest Birth Year For Trips: ', int(earliest_birthyear))

        recent_birthyear =  df['Birth Year'].max()
        print('\n \n Reacent Birth Year For Trips : ', int(recent_birthyear))

        popular_birthyear =  df['Birth Year'].mode()[0]
        print('\n \n Common Birth Year For Trips: ', int(popular_birthyear))

    else :
        print('\n \n Birth Year of Customers Not Available For Washington City')


        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# raw data function to display + 5 rows for the user according to user input by yes or no that takes df as an argument.
def rawdata(df):
    
    index  = 0
    while True :
        user_response = input('Would You Like To Display More Data"yes" or "no" : ').lower().strip()
        if user_response == 'yes':
            index +=5
            print(df[index:index + 5])
        elif user_response == 'no':
            print('\n \n Thank For Your Time, Exit Now ')
            break
        else :
            print('Please Try To Choose The Right Answer yes or no ')





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
