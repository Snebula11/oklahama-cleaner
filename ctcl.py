import pandas as pd


def candidates(ctcl_df):
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

    # makes our new DataFrame, with the fields we want
    new_df = pd.DataFrame(columns=gp_header)

    # START TO CHANGE OVER COLUMNS #

    # TODO: ask fernando if these columns are connected properly
    new_df['name'] = ctcl_df['Candidate Name']
    new_df['State'] = ctcl_df['State']

    new_df['Facebook (Official)'] = ctcl_df['Facebook URL (Gov)']
    new_df['Facebook (Personal)'] = ctcl_df['Facebook URL (Personal)']
    new_df['Facebook (Campaign)'] = ctcl_df['Facebook URL (Campaign)']
    new_df['Instagram (Official)'] = ctcl_df['Instagram URL (Gov)']
    new_df['Instagram (Personal)'] = ctcl_df['Instagram URL (Personal)']
    new_df['Instagram (Campaign)'] = ctcl_df['Instagram URL (Campaign)']

    new_df['Twitter (Official)'] = ctcl_df['Twitter Name (Gov)']
    for i in new_df.index:
        if not pd.isna(new_df['Twitter (Official)'][i]):
            new_df['Twitter (Official)'][i] = ' https://www.twitter.com/' + \
                                               str(new_df['Twitter (Official)'][i])

    new_df['Twitter (Personal)'] = ctcl_df['Twitter Name (Personal)']
    for i in new_df.index:
        if not pd.isna(new_df['Twitter (Personal)'][i]):
            new_df['Twitter (Personal)'][i] = ' https://www.twitter.com/' + \
                                              str(new_df['Twitter (Personal)'][i])

    new_df['Twitter (Campaign)'] = ctcl_df['Twitter Name (Campaign)']
    for i in new_df.index:
        if not pd.isna(new_df['Twitter (Campaign)'][i]):
            new_df['Twitter (Campaign)'][i] = ' https://www.twitter.com/' + \
                                              str(new_df['Twitter (Campaign)'][i])

    new_df['images'] = ctcl_df['Photo URL']
    new_df['email'] = ctcl_df['Email']

    new_df['current_party'] = ctcl_df['Candidate Party Registration']

    for i in new_df.index:
        if not pd.isna(ctcl_df['Seat'][i]) and ctcl_df['Seat'][i] != '(unexpired)':
            district = ctcl_df['Seat'][i].split()
            district.pop(0)
            new_df['current_district'][i] = district[0]

    for i in new_df.index:
        if not pd.isna(ctcl_df['Seat'][i]) and ctcl_df['Seat'][i] != '(unexpired)':
            new_df['current_chamber'][i] = str(ctcl_df['Office Name'][i]) + ' ' + str(ctcl_df['Seat'][i]).title()
        else:
            new_df['current_chamber'][i] = ctcl_df['Office Name'][i]

    for i in new_df.index:
        split_name = str(new_df['name'][i]).split()
        if 'Jr.' in split_name:
            split_name.remove('Jr.')
        if len(split_name) > 2:
            split_name.pop(1)
        new_df['given_name'][i] = split_name[0]
        new_df['family_name'][i] = split_name[1]

    new_df['sources'] = ctcl_df['Website (Campaign)']
    for i in new_df.index:
        if pd.isna(new_df['sources'][i]) and not pd.isna(ctcl_df['Website (Personal)'][i]):
            new_df['sources'][i] = ctcl_df['Website (Personal)'][i]

    new_df['youtube'] = ctcl_df['Youtube (Gov)']
    for i in new_df.index:
        if pd.isna(new_df['youtube'][i]):
            if not pd.isna(ctcl_df['Youtube (Campaign)'][i]):
                new_df['youtube'][i] = ctcl_df['Youtube (Campaign)'][i]
            elif not pd.isna(ctcl_df['Youtube (Personal)'][i]):
                new_df['youtube'][i] = ctcl_df['Youtube (Personal)'][i]

    new_df['Campaign mailing address'] = ctcl_df['Mailing Address']
    new_df['Campaign phone'] = ctcl_df['Phone']

    # EITHER N/A OR BP DOESN'T HAVE IT#

    # new_df['Researcher']
    # new_df['official biography']
    # new_df['biography']
    # new_df['birth_date']
    # new_df['gender'] = ctcl_df['Gender']
    # new_df['LinkedIn'] = ctcl_df['LinkedIn']
    # new_df['title']
    # new_df['status'] = 'Candidate'

    new_df['id'] = 'n/a'
    new_df['facebook'] = 'n/a'
    new_df['twitter'] = 'n/a'
    new_df['death_date'] = 'n/a'
    new_df['links'] = 'n/a'
    new_df['capitol_address'] = 'n/a'
    new_df['capitol_fax'] = 'n/a'
    new_df['capitol_voice'] = 'n/a'
    new_df['district_address'] = 'n/a'
    new_df['district_voice'] = 'n/a'
    new_df['district_fax'] = 'n/a'
    new_df['instagram'] = 'n/a'

    return new_df
