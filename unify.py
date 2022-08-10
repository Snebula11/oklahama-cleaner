import data_headers as dh
import pandas as pd
import numpy as np

# global variable to track which secondary+ rows match primary
match = False
do_not_add = []
added_rows = None


def unify_bp_ctcl(primary_df, secondary_df, third_df=None, fourth_df=None):
    global match
    global do_not_add
    global added_rows
    # go through every primary row
    for p_row in primary_df.index:
        # seeing if we find a match
        match = False
        # find the candidate's name in primary
        search_name = str(primary_df.loc[p_row, 'name_first']) + ' ' + str(primary_df.loc[p_row, 'name_last'])
        # check each secondary row against the selected primary row
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
            # if we did find a match...
            if match:
                # we add that row to our no-fly list
                do_not_add.append(s_row)
                break
        if primary_df['status'][p_row] == 'Challenger':
            for field in dh.incumbents_only:
                if not pd.isna(primary_df.loc[p_row, field]):
                    primary_df.loc[p_row, field] = 'n/a'
        elif primary_df['status'][p_row] == 'Incumbent':
            for field in dh.incumbents_only:
                if primary_df.loc[p_row, field] == 'n/a':
                    primary_df.loc[p_row, field] = np.nan

    # add rows from the secondary df that weren't in the primary
    added_rows_df = secondary_df.drop(labels=do_not_add, axis=0, inplace=False)
    added_rows_df.reset_index(inplace=True, drop=True)
    output_df = pd.concat([primary_df, added_rows_df], ignore_index=True)
    output_df = output_df.reset_index(drop=True)

    # reset globals
    match = False
    do_not_add = []
    added_rows = None

    # do the same with our third
    if third_df is not None:
        for p_row in output_df.index:
            # seeing if we find a match
            match = False
            # find the candidate's name in primary
            search_name = str(output_df.loc[p_row, 'name_first']) + ' ' + str(output_df.loc[p_row, 'name_last'])
            # check each secondary row against the selected primary row
            for t_row in third_df.index:
                curr_name = str(third_df.loc[t_row, 'name_first']) + ' ' + str(third_df.loc[t_row, 'name_last'])
                # if the candidate matches, we go through each cell in the row and fill it in if it's blank
                if search_name == curr_name:
                    # we found a match, so...
                    match = True
                    # we go through each column header
                    for field in dh.mapped_data:
                        # if the ballotpedia value is empty, but ctcl has it...
                        if pd.isna(output_df.loc[p_row, field]) or output_df.loc[p_row, field] == 'n/a':
                            if not pd.isna(third_df.loc[t_row, field]):
                                # store the ctcl value!
                                output_df.loc[p_row, field] = third_df.loc[t_row, field]
                # if we did find a match...
                if match:
                    # we add that row to our no-fly list
                    do_not_add.append(t_row)
                    break
        # add rows from the secondary df that weren't in the primary
        added_rows_df = third_df.drop(labels=do_not_add, axis=0, inplace=False)
        added_rows_df.reset_index(inplace=True, drop=True)
        output_df = pd.concat([output_df, added_rows_df], ignore_index=True)
        output_df = output_df.reset_index(drop=True)

    # reset globals
    match = False
    do_not_add = []
    added_rows = None

    # do the same with our fourth
    if fourth_df is not None:
        for p_row in output_df.index:
            # seeing if we find a match
            match = False
            # find the candidate's name in primary
            search_name = str(output_df.loc[p_row, 'name_first']) + ' ' + str(output_df.loc[p_row, 'name_last'])
            # check each secondary row against the selected primary row
            for f_row in fourth_df.index:
                curr_name = str(fourth_df.loc[f_row, 'name_first']) + ' ' + str(fourth_df.loc[f_row, 'name_last'])
                # if the candidate matches, we go through each cell in the row and fill it in if it's blank
                if search_name == curr_name:
                    # we found a match, so...
                    match = True
                    # we go through each column header
                    for field in dh.mapped_data:
                        # if the ballotpedia value is empty, but ctcl has it...
                        if pd.isna(output_df.loc[p_row, field]) or output_df.loc[p_row, field] == 'n/a':
                            if not pd.isna(fourth_df.loc[f_row, field]):
                                # store the ctcl value!
                                output_df.loc[p_row, field] = fourth_df.loc[f_row, field]
                # if we did find a match...
                if match:
                    # we add that row to our no-fly list
                    do_not_add.append(f_row)
                    break
        # add rows from the secondary df that weren't in the primary
        added_rows_df = fourth_df.drop(labels=do_not_add, axis=0, inplace=False)
        added_rows_df.reset_index(inplace=True, drop=True)
        output_df = pd.concat([output_df, added_rows_df], ignore_index=True)
        output_df = output_df.reset_index(drop=True)

    return output_df
