# Function to group states into regions
def categorize_state(row):
    gulf_states = ['AL', 'FL', 'LA', 'MS', 'TX']
    east_coast_states = ['DC', 'ME', 'NH', 'MA', 'RI', 'CT', 'PA',
                         'NY', 'NJ', 'DE', 'MD', 'VA', 'NC', 'SC', 'GA']
    west_coast_states = ['WA', 'OR', 'CA', 'AK', 'HI']
    island = ['HI', 'Guam', 'PR', 'Virgin Islands', 'American Samoa',
              'Marshall Islands', 'Bermuda', 'Pacific Ocean']

    if row['State'] in gulf_states:
        return 'Gulf Coast'
    elif row['State'] in east_coast_states:
        return 'East Coast'
    elif row['State'] in west_coast_states:
        return 'West Coast'
    elif row['State'] in island:
        return 'Island'
    else:
        return 'Other'


def add_region_column(dataframe):
    dataframe['Region'] = dataframe.apply(categorize_state, axis=1)
    return dataframe
