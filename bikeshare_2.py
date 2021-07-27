import time
import pandas as pd
import numpy as np

city_data = {'chicago': 'chicago.csv',
             'ch': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'ny': 'new_york_city.csv',
             'washington': 'washington.csv',
             'wa': 'washington.csv'
              }

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
    
    city = input('Would you like to see the data for Chicago (CH), New York (NY) or Washington (WA)?\n')
    city = city.lower()
    print()
    
    while True:
        if city == 'ch' or city == 'chicago':
            print('Yay!! We will explore data for {0} today: '.format(str(city_data[city]).upper().split('.')[0]))
            break
        elif city == 'ny' or city == 'new york':
            print('Yay!! We will explore data for {0} today: '.format(str(city_data[city]).upper().split('.')[0]))
            break
        elif city == 'wa' or city == 'washington':
            print('Yay!! We will explore data for {0} today: '.format(str(city_data[city]).upper().split('.')[0]))
            break
        
        print()
        print('Please choose the city names from these values \n Chicago (CH) or New York (NY) or Washington (WA))')
        city = input('Would you like to see the data for Chicago (CH), New York (NY) or Washington (WA)?\n')
        city = city.lower()
        
    month = None
    day = None       
    inp = input('Would you like to filter the data by month, day, both or not at all? Type none for no filter\n')
    
    if (inp == 'none'):
        print('No Filters to be Applied, proceed with the next steps: ')
        month = None
        day = None
        
    elif (inp == 'both'):
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Which month? all, january, february, march, april, may or june?\n')
        month = month.lower()
        
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day of the week? Please enter your response as integer (e.g. 1=sunday or all)\n')
       
    elif (inp == 'month'):
        month = input('Which month? all, january, february, march, april, may or june?\n')
        month = month.lower()

    elif (inp == 'day'):
        day = input('Which day of the week? Please enter your response as integer (e.g. 1=sunday and 7=saturday or all)\n')


    if ((inp == 'both') or (inp == 'month')):
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        while True:
            if month in months:
                print('Using the Month filter where MONTH = {0} \n'.format(month))
                break
        
            print()
            month = input('Enter the correct month value \nWhich month? all, january, february, march, april, may or june? \n')
            month = month.lower()
        
    if ((inp == 'both') or (inp == 'day')): 
        days = ['all', '1', '2', '3', '4', '5', '6', '7']
        while True:
            if day in days:
                print('Filter the data for DAY OF WEEK = {0} \n'.format(day))
                break
            
            print()
            day = input('Enter the corect value \nWhich day of the week? Please enter your response as integer (e.g. 1=sunday and 7=saturday or all) \n')


    print('-'*40)
    return city, month, day


def load_data(city, month_fil, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    city_file = city_data[city.lower()]
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['day_of_week_ind'] = df['Start Time'].dt.strftime("%w")
    df['hour'] = df['Start Time'].dt.strftime("%H")
    
    if ((month_fil != 'all') and (month_fil is not None)):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_ind = months.index(month_fil) + 1
    
    #days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    #print('Completed')
    #day_ind = days.index(day) + 1
    
    if(month_fil != 'all' or day != 'all'):
        if((month_fil != 'all') and (day != 'all') and (month_fil is not None) and (day is not None)):
            df = df[(df['month'] == month_ind) & (df['day_of_week_ind'] == day)]
        elif((month_fil != 'all') and (month_fil is not None)):
            df = df[df['month'] == month_ind]
        elif((day != 'all') and (day is not None)):
            df = df[df['day_of_week_ind'] == day]
        else:
            df = df.copy()
    else:
        print('No Filters Applied, proceeding with the steps \n')
          
    print('Viewing the Dataframe Columns & Values \n')
    print(df.columns)
    print()
    print(df.head())
      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # most_common_month = df['month'].mode()[0]
    most_common_month = df['month'].value_counts().idxmax()
    most_common_months_list = df['month'].value_counts()
    print('Most common month is {0} with value {1} '.format(most_common_month, most_common_months_list[most_common_month]))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    most_common_day_list = df['day_of_week'].value_counts()
    print('Most common day is {0} with value {1} '.format(most_common_day, most_common_day_list[most_common_day]))
    
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    most_common_hour_list = df['hour'].value_counts()
    print('Most common day is {0} with value {1} '.format(most_common_hour, most_common_hour_list[most_common_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_ss = df['Start Station'].value_counts().idxmax()
    most_common_ss_list = df['Start Station'].value_counts()
    print('Most common start station is {0} with value {1} '.format(most_common_ss, most_common_ss_list[most_common_ss]))
    
    # TO DO: display most commonly used end station
    most_common_es = df['End Station'].value_counts().idxmax()
    most_common_es_list = df['End Station'].value_counts()
    print('Most common end station is {0} with value {1} '.format(most_common_es, most_common_es_list[most_common_es]))
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_sses = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name='count').max()
    print("Most common start station, end station combination is {0}".format(most_common_sses.values))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = np.sum(df['Travel Time'])
    total_num_days = str(total_travel_time).split()[0]
    print('Total Time Travelled is {} days'.format(total_num_days))

    # TO DO: display mean travel time
    average_travel_time = np.mean(df['Travel Time'])
    avg_num_days = str(average_travel_time).split()[0]
    print('Average Time Travelled is {} days'.format(avg_num_days))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_cnt = df[['User Type']].groupby('User Type', axis = 0).size().sort_values(ascending=False).reset_index(name='count')
    print('User Types Count: \n')
    print(user_types_cnt)
    print()
    
    print('View the Dataframe Columns & Values \n')
    print(df.columns)
    print()
    print(df.head())
    print()
    
    # TO DO: Display counts of gender
    try:
        gender_cnt = df[['Gender']].groupby('Gender').size().sort_values(ascending=False).reset_index(name='count')
        print('Gender Counts: \n')
        print(gender_cnt)
        print()
    except:
        print('Gender data is missing from the file')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = np.min(df['Birth Year'])
        print('Earliest Birth Year: {0}'.format(earliest_birth_year))
        
        most_recent_birth_year = np.max(df['Birth Year'])
        print('Most Recent Birth Year: {0}'.format(most_recent_birth_year))
        
        #most_common_birth_year = df[['Birth Year']].groupby(['Birth Year']).size().sort_values(ascending=False).reset_index(name='count').max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: {0}'.format(most_common_birth_year))
    except:
        print('Birth Year related data missing from the file')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        j = 5
        while True:
            print_data = input('\nWould you like to print 5 rows of data? Enter yes or no\n')
            if print_data.lower() == 'yes':
                print(df.iloc[[i,j]])
                i += 5
                j += 5
                continue
            else:
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
