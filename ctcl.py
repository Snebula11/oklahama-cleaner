import pandas as pd
import data_headers as dh


def candidates(ctcl_df):
    # makes our new DataFrame, with the fields we want
    new_df = pd.DataFrame(columns=dh.mapped_data)

    # START TO CHANGE OVER COLUMNS #
    new_df['state'] = ctcl_df['State']
    for row in new_df.index:
        if not pd.isna(ctcl_df['Seat'][row]):
            new_df['Office'][row] = str(ctcl_df['Office Name'][row]) + ' ' + str(ctcl_df['Seat'][row]).title()
        else:
            new_df['Office'][row] = ctcl_df['Office Name'][row]
    new_df['Name'] = ctcl_df['Candidate Name']
    # get the last and middle names
    for i in new_df.index:
        # split the name into a list
        split_name = str(new_df['Candidate Name'][i]).split()
        # if it's just a first and last, store them
        if len(split_name) == 2:
            new_df.loc[i, 'name_first'] = split_name[0]
            new_df.loc[i, 'name_last'] = split_name[1]
        elif len(split_name) == 3:
            # if there's a suffix, store that
            if 'Jr.' in split_name or 'Sr.' in split_name:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_last'] = split_name[1]
                new_df.loc[i, 'name_suffix'] = split_name[2]
            # if there's not, look for a middle name
            else:
                new_df.loc[i, 'name_first'] = split_name[0]
                new_df.loc[i, 'name_middle'] = split_name[1]
                new_df.loc[i, 'name_last'] = split_name[2]
    new_df['party'] = ctcl_df['Candidate Party Registration']
    # TODO: should ctcl's 'phone', 'mailing address', 'email' be campaign or official
    new_df['phone_campaign'] = ctcl_df['Phone']
    new_df['address_campaign'] = ctcl_df['Mailing Address']
    new_df['website_campaign'] = ctcl_df['Website (Campaign)']
    new_df['website_personal'] = ctcl_df['Website (Personal)']
    new_df['email_campaign'] = ctcl_df['Email']
    new_df['Image'] = ctcl_df['Photo URL']
    new_df['facebook_official'] = ctcl_df['Facebook URL (Gov)']
    new_df['facebook_personal'] = ctcl_df['Facebook URL (Personal)']
    new_df['facebook_campaign'] = ctcl_df['Facebook URL (Campaign)']
    new_df['twitter_official'] = ctcl_df['Twitter Name (Gov)']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_official'][row]):
            new_df.loc[row, 'twitter_official'] = ' https://www.twitter.com/' + str(new_df.loc[row, 'twitter_official'])
    new_df['twitter_personal'] = ctcl_df['Twitter Name (Personal)']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_personal'][row]):
            new_df.loc[row, 'twitter_personal'] = ' https://www.twitter.com/' + str(new_df.loc[row, 'twitter_personal'])
    new_df['twitter_campaign'] = ctcl_df['Twitter Name (Campaign)']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_campaign'][row]):
            new_df.loc[row, 'twitter_campaign'] = ' https://www.twitter.com/' + str(new_df.loc[row, 'twitter_campaign'])
    new_df['instagram_official'] = ctcl_df['Instagram URL (Gov)']
    new_df['instagram_personal'] = ctcl_df['Instagram URL (Personal)']
    new_df['instagram_campaign'] = ctcl_df['Instagram URL (Campaign)']

    return new_df
