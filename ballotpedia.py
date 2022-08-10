import pandas as pd
import data_headers as dh


def convert_ballotpedia(bp_df):
    # makes our new DataFrame, with the fields we want
    new_df = pd.DataFrame(columns=dh.mapped_data)

    # deletes all candidates that either withdrew, lost, or won (we don't need them anymore!)
    rows_to_delete = []
    for i in range(0, len(bp_df.index)):
        if bp_df['Stage'][i] == 'Primary' or bp_df['Stage'][i] == 'Primary Runoff':
            rows_to_delete.append(i)
    bp_df.drop(labels=rows_to_delete, axis=0, inplace=True)
    bp_df.reset_index(inplace=True)

    # START TO CHANGE OVER COLUMNS #

    new_df['state'] = bp_df['State']
    new_df['Ballotpedia Office ID'] = bp_df['Office ID']
    new_df['Office'] = bp_df['Office name']
    new_df['district'] = bp_df['District name']
    new_df['district_ocd_id'] = bp_df['District OCDID']
    new_df['ballotpedia_id'] = bp_df['Person ID']
    new_df['Name'] = bp_df['Name']
    # get the last and middle names
    for i in new_df.index:
        # split the name into a list
        split_name = str(new_df['Name'][i]).split()
        # if it's just a first and last, store them
        if len(split_name) == 2:
            new_df.loc[i, 'name_first'] = split_name[0]
            new_df.loc[i, 'name_last'] = split_name[1]
        elif len(split_name) == 3:
            # if there's a suffix, store that
            if 'Jr.' in split_name or 'Sr.' in split_name or 'M.D.' in split_name or 'Ph.D.' in split_name:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_last'] = split_name[1]
                new_df.loc[i, 'name_suffix'] = split_name[2]
            # if there's not, look for a middle name
            else:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1]
                new_df.loc[i, 'name_last'] = split_name[2]
        elif len(split_name) == 4:
            suffix_present = False
            for suffix in dh.suffixes:
                if suffix in split_name:
                    suffix_present = True
            # if there's a suffix, store that
            if suffix_present:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1]
                new_df.loc[i, 'name_last'] = split_name[2]
                new_df.loc[i, 'name_suffix'] = split_name[3]
            # if there's not, look for a middle name
            else:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1] + ' ' + split_name[2]
                new_df.loc[i, 'name_last'] = split_name[3]
    new_df['Ballotpedia URL'] = bp_df['Ballotpedia URL']
    new_df['gender'] = bp_df['Gender']
    new_df['party'] = bp_df['Party affiliation']
    new_df['email_campaign'] = bp_df['Campaign email']
    new_df['email_other'] = bp_df['Other email']
    new_df['website_campaign'] = bp_df['Campaign website']
    new_df['website_personal'] = bp_df['Personal website']
    new_df['facebook_campaign'] = bp_df['Campaign Facebook']
    new_df['facebook_personal'] = bp_df['Personal Facebook']
    new_df['twitter_campaign'] = bp_df['Campaign Twitter']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_campaign'][row]):
            new_df.loc[row, 'twitter_campaign'] = 'https://www.twitter.com/' + str(new_df.loc[row, 'twitter_campaign'])
    new_df['twitter_personal'] = bp_df['Personal Twitter']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_personal'][row]):
            new_df.loc[row, 'twitter_personal'] = 'https://www.twitter.com/' + str(new_df.loc[row, 'twitter_personal'])
    new_df['instagram_campaign'] = bp_df['Campaign Instagram']
    new_df['instagram_personal'] = bp_df['Personal Instagram']
    new_df['youtube_campaign'] = bp_df['Campaign YouTube']
    new_df['youtube_personal'] = bp_df['Personal YouTube']
    new_df['address_campaign'] = bp_df['Campaign mailing address']
    new_df['phone_campaign'] = bp_df['Campaign phone']
    new_df['linkedin'] = bp_df['LinkedIn']

    for row in new_df.index:
        if bp_df['Incumbent?'][row] == 'No':
            for field in dh.incumbents_only:
                if pd.isna(new_df.loc[row, field]):
                    new_df.loc[row, field] = 'n/a'
            new_df.loc[row, 'status'] = 'Challenger'
        elif bp_df['Incumbent?'][row] == 'Yes':
            new_df.loc[row, 'status'] = 'Incumbent'

    return new_df
