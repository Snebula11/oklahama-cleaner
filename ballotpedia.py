import pandas as pd


def challengers(bp_df):
    # columns for our current data model
    gp_header = ['Researcher', 'id', 'name', 'State', 'official biography', 'biography', 'facebook',
                 'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'twitter', 'Twitter (Official)',
                 'Twitter (Personal)', 'Twitter (Campaign)', 'current_party', 'current_district', 'current_chamber',
                 'title', 'status', 'given_name', 'family_name', 'gender', 'email', 'birth_date', 'death_date', 'image',
                 'links', 'sources', 'capitol_address', 'capitol_voice', 'capitol_fax', 'district_address',
                 'district_voice', 'district_fax', 'youtube', 'instagram', 'Instagram (Official)',
                 'Instagram (Personal)', 'Instagram (Campaign)', 'Campaign mailing address', 'Campaign phone',
                 'LinkedIn']

    # TODO: figure out which statuses we need

    # deletes all candidates that either withdrew, lost, or won (we don't need them anymore!)
    row_num = len(bp_df.index)
    bad_status = ['Withdrew', 'Lost', 'Won']
    rows_to_delete = []
    for i in range(0, row_num):
        if bp_df['Candidate status'][i] in bad_status:
            rows_to_delete.append(i)
    bp_df.drop(labels=rows_to_delete, axis=0, inplace=True)
    bp_df.reset_index(inplace=True)

    # makes our new DataFrame, with the fields we want
    new_df = pd.DataFrame(columns=gp_header)

    # START TO CHANGE OVER COLUMNS #

    # TODO: ask fernando if these columns are connected properly
    new_df['name'] = bp_df['Name']
    new_df['State'] = bp_df['State']
    new_df['Facebook (Personal)'] = bp_df['Personal Facebook']
    new_df['Facebook (Campaign)'] = bp_df['Campaign Facebook']
    new_df['Twitter (Personal)'] = bp_df['Personal Twitter']
    for i in new_df.index:
        if not pd.isna(new_df['Twitter (Personal)'][i]):
            new_df['Twitter (Personal)'][i] = ' https://www.twitter.com/' + \
                                              str(new_df['Twitter (Personal)'][i])

    new_df['Twitter (Campaign)'] = bp_df['Campaign Twitter']
    for i in new_df.index:
        if not pd.isna(new_df['Twitter (Campaign)'][i]):
            new_df['Twitter (Campaign)'][i] = ' https://www.twitter.com/' + \
                                              str(new_df['Twitter (Campaign)'][i])

    new_df['current_party'] = bp_df['Party affiliation']
    new_df['current_district'] = bp_df['Office name']
    new_df['current_chamber'] = bp_df['Office name']
    new_df['status'] = 'Candidate'
    new_df['given_name'] = bp_df['First name']
    new_df['family_name'] = bp_df['Last name']
    new_df['gender'] = bp_df['Gender']
    new_df['email'] = bp_df['Campaign email']

    new_df['sources'] = bp_df['Campaign website']
    for i in new_df.index:
        if pd.isna(new_df['sources'][i]) and not pd.isna(bp_df['Personal website'][i]):
            new_df['sources'][i] = bp_df['Personal website'][i]

    new_df['youtube'] = bp_df['Campaign YouTube']
    for i in new_df.index:
        if pd.isna(new_df['youtube'][i]) and not pd.isna(bp_df['Personal YouTube'][i]):
            new_df['youtube'][i] = bp_df['Personal YouTube'][i]

    new_df['Instagram (Personal)'] = bp_df['Personal Instagram']
    new_df['Instagram (Campaign)'] = bp_df['Campaign Instagram']
    new_df['Campaign mailing address'] = bp_df['Campaign mailing address']
    new_df['Campaign phone'] = bp_df['Campaign phone']
    new_df['LinkedIn'] = bp_df['LinkedIn']

    # EITHER N/A OR BP DOESN'T HAVE IT#

    # new_df['Researcher']
    # new_df['official biography']
    # new_df['biography']
    # new_df['birth_date']
    # new_df['images']

    new_df['id'] = 'n/a'
    new_df['facebook'] = 'n/a'
    new_df['Facebook (Official)'] = 'n/a'
    new_df['twitter'] = 'n/a'
    new_df['Twitter (Official)'] = 'n/a'
    new_df['death_date'] = 'n/a'
    new_df['links'] = 'n/a'
    new_df['capitol_address'] = 'n/a'
    new_df['capitol_fax'] = 'n/a'
    new_df['capitol_voice'] = 'n/a'
    new_df['district_address'] = 'n/a'
    new_df['district_voice'] = 'n/a'
    new_df['district_fax'] = 'n/a'
    new_df['instagram'] = 'n/a'
    new_df['Instagram (Official)'] = 'n/a'

    return new_df
