import data_headers as dh
import pandas as pd


def unify_bp_ctcl(primary_df, secondary_df):
    # go through every ballotpedia row
    for p_row in primary_df.index:
        # find the candidate's name in ballotpedia
        search_name = str(primary_df.loc[p_row, 'name_first']) + ' ' + str(primary_df.loc[p_row, 'name_last'])
        # check each ctcl row against the selected ballotpedia row
        for s_row in secondary_df.index:
            curr_name = str(secondary_df.loc[s_row, 'name_first']) + ' ' + str(secondary_df.loc[s_row, 'name_last'])
            # if the candidate matches, we go through each cell in the row and fill it in if it's blank
            if search_name == curr_name:
                for field in dh.mapped_data:
                    if pd.isna(primary_df.loc[p_row, field]) and not pd.isna(secondary_df.loc[s_row, field]):
                        primary_df.loc[p_row, field] = secondary_df.loc[s_row, field]

    return primary_df
