import data_headers as dh
import pandas as pd

match = False
do_not_add = []


def unify_bp_ctcl(primary_df, secondary_df):
    global match
    global do_not_add
    # go through every ballotpedia row
    for p_row in primary_df.index:
        # seeing if we find a match
        match = False
        # find the candidate's name in ballotpedia
        search_name = str(primary_df.loc[p_row, 'name_first']) + ' ' + str(primary_df.loc[p_row, 'name_last'])
        # check each ctcl row against the selected ballotpedia row
        for s_row in secondary_df.index:
            curr_name = str(secondary_df.loc[s_row, 'name_first']) + ' ' + str(secondary_df.loc[s_row, 'name_last'])
            # if the candidate matches, we go through each cell in the row and fill it in if it's blank
            if search_name == curr_name:
                # we found a match, so...
                match = True
                # we go through each column header
                for field in dh.mapped_data:
                    # if the ballotpedia value is empty, but ctcl has it...
                    if pd.isna(primary_df.loc[p_row, field]) and not pd.isna(secondary_df.loc[s_row, field]):
                        # store the ctcl value!
                        primary_df.loc[p_row, field] = secondary_df.loc[s_row, field]
            if match:
                do_not_add.append(s_row)
                break
        if primary_df['status'][p_row] == 'Challenger':
            for field in dh.incumbents_only:
                if not pd.isna(primary_df.loc[p_row, field]):
                    primary_df.loc[p_row, field] = 'n/a'
        elif primary_df['status'][p_row] == 'Incumbent':
            for field in dh.incumbents_only:
                if primary_df.loc[p_row, field] == 'n/a':
                    primary_df.loc[p_row, field] = pd.NA

    # sdi = len(secondary_df.index)
    # for s_row in secondary_df.index:
    #     match_found = False
    #     search_name = str(secondary_df.loc[s_row, 'name_first']) + ' ' + str(secondary_df.loc[s_row, 'name_last'])
    #     for p_row in primary_df.index:
    #         curr_name = str(primary_df.loc[p_row, 'name_first']) + ' ' + str(primary_df.loc[p_row, 'name_last'])
    #         if search_name == curr_name:
    #             match_found = True
    #             break
    #     if not match_found:
    #         primary_df = primary_df.append(secondary_df.loc[[s_row]])
    #     print(f'working {s_row}/{sdi}')
    added_rows_df = secondary_df.drop(labels=do_not_add, axis=0, inplace=False)
    added_rows_df.reset_index(inplace=True, drop=True)

    output_df = pd.concat([primary_df, added_rows_df], ignore_index=True)
    output_df.reset_index()

    return output_df
