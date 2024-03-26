state_map = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Californie": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    "Pensacola": "FL",
    "Gulf Coast": "Gulf Coast",
    "East Coast": "East Coast",
    "West Coast": "West Coast",
}

# invert the dictionary
abbrev_to_us_state = dict(map(reversed, state_map.items()))
# Function to group states into regions


def categorize_state(row):
    gulf_states = ['AL', 'FL', 'LA', 'MS', 'TX', 'Gulf Coast']
    east_coast_states = ['DC', 'ME', 'NH', 'MA', 'RI', 'CT', 'PA',
                         'NY', 'NJ', 'DE', 'MD', 'VA', 'NC', 'SC', 'GA', 'East Coast']
    west_coast_states = ['WA', 'OR', 'CA', 'AK', 'West Coast']
    island = ['HI', 'Guam', 'PR', 'Virgin Islands', 'American Samoa',
              'Marshall', 'Bermuda', 'Pacific Ocean']

 # Normalize the state to its abbreviation
    states = [state_map.get(state.strip(), state.strip())
              for state in row['State'].split(',')]

 # Split the state entry by commas and strip whitespace, to handle multiple states
 #   states = [state.strip() for state in row['State'].split(',')]

    # Check each state in the list
    for state in states:
        if state in gulf_states:
            return 'Gulf Coast'
    # If none of the states are in the Gulf Coast, categorize based on the first state in the list
    first_state = states[0]  # Consider the first state if multiple
    if first_state in east_coast_states:
        return 'East Coast'
    elif first_state in west_coast_states:
        return 'West Coast'
    elif first_state in island:
        return 'Island'
    else:
        return 'Other'


def add_region_column(dataframe):
    dataframe['Region'] = dataframe.apply(categorize_state, axis=1)
    return dataframe
