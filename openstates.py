import pandas as pd
import numpy as np
import data_headers as dh
import utilities as util


def convert_openstates(openstates_df, us_df, state):
    long_state = util.statenames(state.upper())
    do_not_add = []

    for row in us_df.index:
        curr_state = us_df['current_district'][row]
        if '-' in curr_state:
            curr_state = curr_state.split('-')
            curr_state = util.statenames(curr_state[0])
        if curr_state != long_state:
            do_not_add.append(row)

    us_df.drop(labels=do_not_add, axis=0, inplace=True)
    us_df.reset_index(inplace=True, drop=True)
    openstates_df = pd.concat([openstates_df, us_df], ignore_index=True)
    openstates_df.reset_index(inplace=True, drop=True)

    # Makes a new DataFrame to store output
    new_df = pd.DataFrame(columns=dh.new_column_headers)

    '''
    The following code converts Open States data into the desired output format
    It either transfers entire columns (the Open States and output DataFrames have the same index)
    Or it goes row by row through a column performing specific operations on data before storing it in output
    '''

    new_df['name'] = openstates_df['name']

    # get the last and middle names
    for i in new_df.index:
        # split the name into a list
        name_to_split = str(new_df['name'][i]).replace(',', '')
        split_name = name_to_split.split()

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

        if str(new_df.loc[i, 'name_middle'])[0] == '"':
            new_df.loc[i, 'nickname'] = new_df.loc[i, 'name_middle']
            new_df.loc[i, 'name_middle'] = np.nan

    new_df['Image'] = openstates_df['image']

    new_df['party'] = openstates_df['current_party']

    for row in new_df.index:
        if openstates_df['sources'][row] != 'https://theunitedstates.io/':
            curr_dist = str(openstates_df['current_district'][row])

            if openstates_df['current_chamber'][row] == 'upper':
                new_df.loc[row, 'title'] = long_state + ' State Senator'
                new_df.loc[row, 'district'] = long_state + ' State Senate District ' + curr_dist
                new_df.loc[row, 'Office'] = long_state + ' State Senate District ' + curr_dist
            elif openstates_df['current_chamber'][row] == 'lower':
                new_df.loc[row, 'title'] = long_state + ' State Representative'
                new_df.loc[row, 'district'] = long_state + ' State House District ' + curr_dist
                new_df.loc[row, 'Office'] = long_state + ' State House District ' + curr_dist

        else:
            if openstates_df['current_chamber'][row] == 'upper':
                new_df.loc[row, 'title'] = 'U.S. Senator'
                new_df.loc[row, 'district'] = long_state + 'Statewide'
                new_df.loc[row, 'Office'] = 'U.S. Senate' + long_state
            elif openstates_df['current_chamber'][row] == 'lower':
                congress_dist = str(openstates_df['current_district'][row].split('-')[1])
                new_df.loc[row, 'title'] = 'U.S. Representative'
                new_df.loc[row, 'district'] = long_state + ' Congressional District ' + congress_dist
                new_df.loc[row, 'Office'] = 'U.S. House ' + long_state + ' District ' + congress_dist

    new_df['state'] = state.upper()

    new_df['status'] = 'Incumbent'

    new_df['gender'] = openstates_df['gender']

    new_df['date_of_birth'] = openstates_df['birth_date']
    new_df['date_of_death'] = openstates_df['death_date']

    new_df['Bio'] = openstates_df['biography']

    new_df['email_official'] = openstates_df['email']

    new_df['twitter_campaign'] = openstates_df['twitter']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_campaign'][row]):
            new_df.loc[row, 'twitter_campaign'] = 'https://www.twitter.com/' + str(new_df.loc[row, 'twitter_campaign'])

    new_df['youtube_campaign'] = openstates_df['youtube']
    for row in new_df.index:
        if not pd.isna(new_df['youtube_campaign'][row]):
            new_df.loc[row, 'youtube_campaign'] = 'https://www.youtube.com/c/' + \
                                                  str(new_df.loc[row, 'youtube_campaign'])

    new_df['instagram_campaign'] = openstates_df['instagram']
    for row in new_df.index:
        if not pd.isna(new_df['instagram_campaign'][row]):
            new_df.loc[row, 'instagram_campaign'] = 'https://www.instagram.com/' + \
                                                    str(new_df.loc[row, 'instagram_campaign'])

    new_df['facebook_campaign'] = openstates_df['facebook']
    for row in new_df.index:
        if not pd.isna(new_df['facebook_campaign'][row]):
            new_df.loc[row, 'facebook_campaign'] = 'https://www.facebook.com/' + \
                                                  str(new_df.loc[row, 'facebook_campaign'])

    new_df['address_capitol'] = openstates_df['capitol_address']
    new_df['address_district'] = openstates_df['district_address']

    new_df['phone_capitol'] = openstates_df['capitol_voice']
    new_df['phone_district'] = openstates_df['district_voice']

    new_df['fax_capitol'] = openstates_df['capitol_fax']
    new_df['fax_district'] = openstates_df['district_fax']

    new_df['openstates_id'] = openstates_df['id']

    return new_df
