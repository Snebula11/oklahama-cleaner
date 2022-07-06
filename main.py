import ballotpedia as bp
import csv
import pandas as pd

header_row = ['Researcher', 'id', 'name', 'State', 'official biography', 'biography', 'facebook',
              'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'twitter', 'Twitter (Official)',
              'Twitter (Personal)', 'Twitter (Campaign)', 'current_party', 'current_district', 'current_chamber',
              'title', 'status', 'given_name', 'family_name', 'gender', 'email', 'birth_date', 'death_date', 'image',
              'links', 'sources', 'capitol_address', 'capitol_voice', 'capitol_fax', 'district_address',
              'district_voice', 'district_fax', 'youtube', 'instagram', 'Instagram (Official)', 'Instagram (Personal)',
              'Instagram (Campaign)']

data = pd.read_csv(r'metabase_query_results_1766.csv')
df = pd.DataFrame(data)

new_df = pd.DataFrame()


if __name__ == '__main__':
    print(new_df)
