import pandas as pd
import data_headers as dh
import utilities as util


def convert_ballotpedia(bp_df, state):
    # Stores full state name
    long_state = util.statenames(state.upper())

    # Takes the rows for the requested states
    bp_df = bp_df[bp_df['State'] == state]
    bp_df = bp_df.reset_index()

    # Makes a new DataFrame to store output
    new_df = pd.DataFrame(columns=dh.new_column_headers)

    # Takes only relevant candidates (excludes disqualified and primary losers) from the BP DataFrame
    rows_to_delete = []
    for i in range(0, len(bp_df.index)):
        row_stage = bp_df['Stage'][i]
        row_race_type = bp_df['Race type'][i]
        if row_stage == 'Primary' or row_stage == 'Primary Runoff':
            rows_to_delete.append(i)
        elif (row_race_type == 'Special' or row_race_type == 'Recall') and row_stage == 'General':
            rows_to_delete.append(i)
    bp_df.drop(labels=rows_to_delete, axis=0, inplace=True)
    bp_df.reset_index(inplace=True)

    '''
    The following code converts Ballotpedia data into the desired output format
    It either transfers entire columns (the BP and output DataFrames have the same index)
    Or it goes row by row through a column performing specific operations on data before storing it in output
    '''

    # Parses the name to get first, middle, last, suffix, and nickname
    new_df['name'] = bp_df['Name']

    for i in new_df.index:
        # split the name into a list
        split_name = str(new_df['name'][i]).split()

        # find a suffix
        suffix_present = False
        for suffix in dh.suffixes:
            if suffix in split_name:
                suffix_present = True

        # if it's just a first and last, store them
        if len(split_name) == 2:
            new_df.loc[i, 'name_first'] = split_name[0]
            new_df.loc[i, 'name_last'] = split_name[1]

        elif len(split_name) == 3:
            # if there's a suffix, store that
            if suffix_present:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_last'] = split_name[1]
                new_df.loc[i, 'name_suffix'] = split_name[2]
            elif split_name[1] == 'Van':
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_last'] = split_name[1] + ' ' + split_name[2]
            # if there's not, look for a middle name
            else:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1]
                new_df.loc[i, 'name_last'] = split_name[2]

        elif len(split_name) == 4:
            # if there's a suffix, store that
            if suffix_present:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1]
                new_df.loc[i, 'name_last'] = split_name[2]
                new_df.loc[i, 'name_suffix'] = split_name[3]
            elif split_name[2] == 'Van':
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1]
                new_df.loc[i, 'name_last'] = split_name[2] + ' ' + split_name[3]
            # if there's not, look for a middle name
            else:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1] + ' ' + split_name[2]
                new_df.loc[i, 'name_last'] = split_name[3]

    new_df['party'] = bp_df['Party affiliation']

    # Gives office, district and title
    for row in new_df.index:
        split_office = bp_df['Office name'][row].split(' ')

        if bp_df['District type'][row] == 'Congress':
            new_df.loc[row, 'office'] = bp_df['Office name'][row]
            if split_office[1] == 'House':
                new_df.loc[row, 'district'] = long_state + ' Congressional District ' + split_office[-1]
                new_df.loc[row, 'title'] = 'U.S. Representative'
            elif split_office[1] == 'Senate':
                new_df.loc[row, 'district'] = long_state + ' Statewide'
                new_df[row, 'title'] = 'U.S. Senator'

        elif bp_df['District type'][row] == 'State Legislative (Lower)':
            new_df.loc[row, 'office'] = long_state + ' State House District ' + split_office[-1]
            new_df.loc[row, 'district'] = long_state + ' State House District ' + split_office[-1]
            new_df.loc[row, 'title'] = long_state + ' State Representative'

        elif bp_df['District type'][row] == 'State Legislative (Upper)':
            new_df.loc[row, 'office'] = long_state + ' State Senate District ' + split_office[-1]
            new_df.loc[row, 'district'] = long_state + ' State Senate District ' + split_office[-1]
            new_df.loc[row, 'title'] = long_state + ' State Senator'

        elif bp_df['District type'][row] == 'State':
            new_df.loc[row, 'office'] = bp_df['Office name'][row]
            new_df.loc[row, 'district'] = long_state + ' Statewide'
            # No title due to high variation in office type

        # In AZ, this accounts for school districts only (spot check other states)
        else:
            new_df.loc[row, 'office'] = bp_df['Office name'][row]
            new_df.loc[row, 'district'] = bp_df['District name'][row]
            # No title due to high variation in office type

    new_df['state'] = state.upper()

    for row in new_df.index:
        if bp_df['Incumbent?'][row] == 'No':
            # for field in dh.incumbents_only:
            #     if pd.isna(new_df.loc[row, field]):
            #         new_df.loc[row, field] = 'n/a'
            new_df.loc[row, 'status'] = 'Challenger'
        elif bp_df['Incumbent?'][row] == 'Yes':
            new_df.loc[row, 'status'] = 'Incumbent'

    new_df['gender'] = bp_df['Gender']

    new_df['ballotpedia_id'] = bp_df['Person ID']
    new_df['Ballotpedia URL'] = bp_df['Ballotpedia URL']
    new_df['ballotpedia Office ID'] = bp_df['Office ID']

    new_df['district_ocd_id'] = bp_df['District OCDID']

    return new_df
