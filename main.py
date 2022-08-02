import ballotpedia as bp
import ctcl
import openstates
import unify

import urllib.error

if __name__ == '__main__':
    available_states = ['AZ', 'CA', 'GA', 'MA', 'MD', 'MS', 'NY', 'OK']

    # input loop
    while True:

        state = input('Type the postal abbr. of the state you want: ').upper()

        if state in available_states:
            # OUTPUT FILEPATH
            output_filepath = 'data/' + state.upper() + '/' + state.lower() + '_output.csv'

            # BP CONVERSION
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() + '/' \
                     + state.lower() + '_bp_data.csv'
            try:
                bp_data = bp.pd.read_csv(bp_url)
            except urllib.error.HTTPError:
                pass
            else:
                bp_df = bp.pd.DataFrame(bp_data)
                converted_bp = bp.convert_ballotpedia(bp_df)

            # CTCL CONVERSION
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() + '/' \
                       + state.lower() + '_ctcl_data.csv'
            try:
                ctcl_data = bp.pd.read_csv(ctcl_url)
            except urllib.error.HTTPError:
                pass
            else:
                ctcl_df = bp.pd.DataFrame(ctcl_data)
                converted_ctcl = ctcl.convert_ctcl(ctcl_df)

            # OPENSTATES CONVERSION
            openstates_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() \
                             + '/' + state.lower() + '_openstates_data.csv'
            try:
                openstates_data = bp.pd.read_csv(openstates_url)
            except urllib.error.HTTPError:
                pass
            else:
                openstates_df = bp.pd.DataFrame(openstates_data)
                converted_openstates = openstates.convert_openstates(openstates_df)

            # OUTPUT MERGED DATASET
            # check if we have all 3
            try:
                # noinspection PyUnboundLocalVariable
                unified = unify.unify_bp_ctcl(converted_bp, converted_ctcl, third_df=converted_openstates)
            # if we do not
            except NameError:
                unified = unify.unify_bp_ctcl(converted_ctcl, converted_openstates)
                unified.to_csv(output_filepath, index=False, encoding='utf-8')
                break
            # if we do have all 3
            else:
                unified.to_csv(output_filepath, index=False, encoding='utf-8')
                break
        else:
            print("Sorry, we don't have that state available! Maybe we haven't added it, maybe a typo. Try again.")
