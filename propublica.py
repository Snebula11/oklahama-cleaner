import utilities
import pandas as pd
import data_headers as dh


def convert_propublica(state):
    p_df = utilities.pull_propublica_api()
    p_df = p_df[p_df['state'] == state]
    p_df = p_df.reset_index()

    long_state = utilities.statenames(state.upper())

    new_df = pd.DataFrame(columns=dh.new_column_headers)

    new_df['name_first'] = p_df['first_name']
    new_df['name_middle'] = p_df['middle_name']
    new_df['name_last'] = p_df['last_name']
    new_df['name_suffix'] = p_df['suffix']

    for row in p_df.index:
        if pd.isna(p_df['middle_name'][row]):
            new_df['name'][row] = p_df['first_name'][row] + ' ' + p_df['last_name'][row]
        else:
            new_df['name'][row] = p_df['first_name'][row] + ' ' \
                                  + p_df['middle_name'][row] + ' ' \
                                  + p_df['last_name'][row]
        if not pd.isna(p_df['suffix'][row]):
            new_df['name'][row] = new_df['name'][row] + ', ' + p_df['suffix'][row]

    for row in new_df.index:
        if p_df['party'][row] == 'D':
            new_df['party'][row] = 'Democratic Party'
        elif p_df['party'][row] == 'R':
            new_df['party'][row] = 'Republican Party'
        elif p_df['party'][row] == 'ID':
            new_df['party'][row] = 'Independent'

    for row in new_df.index:
        if pd.isna(p_df['district'][row]):
            new_df.loc[row, 'district'] = long_state + ' Statewide'
            new_df.loc[row, 'office'] = 'U.S. Senate ' + long_state
            new_df.loc[row, 'title'] = 'U.S. Senator'

        else:
            new_df.loc[row, 'title'] = 'U.S. Representative'

            if p_df['district'][row] == 'At-Large':
                new_df.loc[row, 'district'] = long_state + ' At-Large Congressional District'
                new_df.loc[row, 'office'] = 'U.S. House ' + long_state + ' At-Large District'

            else:
                curr_dist = str(p_df['district'][row])
                new_df.loc[row, 'district'] = long_state + ' Congressional District ' + curr_dist
                new_df.loc[row, 'office'] = 'U.S. House ' + long_state + ' District ' + curr_dist

    new_df['state'] = p_df['state']

    for row in new_df.index:
        if p_df['in_office'][row]:
            new_df['status'][row] = 'Incumbent'

        elif not p_df['in_office'][row]:
            new_df['status'][row] = 'Out of Office'

    for row in new_df.index:
        if p_df['gender'][row] == 'M':
            new_df['gender'][row] = 'Male'

        elif p_df['gender'][row] == 'F':
            new_df['gender'][row] = 'Female'

    new_df['date_of_birth'] = p_df['date_of_birth']

    new_df['website_official'] = p_df['url']

    new_df['twitter_official'] = p_df['twitter_account']
    for row in new_df.index:
        if not pd.isna(new_df['twitter_official'][row]):
            new_df.loc[row, 'twitter_official'] = 'https://www.twitter.com/' + \
                                                  str(new_df.loc[row, 'twitter_official'])

    new_df['youtube_official'] = p_df['youtube_account']
    for row in new_df.index:
        if not pd.isna(new_df['youtube_official'][row]):
            new_df.loc[row, 'youtube_official'] = 'https://www.youtube.com/c/' + \
                                                  str(new_df.loc[row, 'youtube_official'])

    new_df['facebook_official'] = p_df['facebook_account']
    for row in new_df.index:
        if not pd.isna(new_df['facebook_official'][row]):
            new_df.loc[row, 'facebook_official'] = 'https://www.facebook.com/' + \
                                                   str(new_df.loc[row, 'facebook_official'])

    new_df['rss'] = p_df['rss_url']

    new_df['address_capitol'] = p_df['office']

    new_df['phone_capitol'] = p_df['phone']

    new_df['fax_capitol'] = p_df['fax']

    new_df['contact_form_url'] = p_df['contact_form']

    new_df['lis_id'] = p_df['lis_id']
    new_df['cspan_id'] = p_df['cspan_id']
    new_df['govtrack_id'] = p_df['govtrack_id']
    new_df['votesmart_id'] = p_df['votesmart_id']
    new_df['icpsr_id'] = p_df['icpsr_id']
    new_df['google_entity_id'] = p_df['google_entity_id']

    new_df['propublica URL'] = p_df['api_uri']

    new_df['fec_id'] = p_df['fec_candidate_id']

    new_df['district_ocd_id'] = p_df['ocd_id']

    return new_df
