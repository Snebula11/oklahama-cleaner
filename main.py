import ballotpedia as bp
import ctcl
import openstates
import unify

import urllib.error

if __name__ == '__main__':
    available_states = ['AZ', 'CA', 'GA', 'MA', 'MD', 'MS', 'NY', 'OK']

    # input loop
    while True:
        # take user input
        bp_present = False
        ctcl_present = False
        openstates_present = False

        state = input('Type the postal abbr. of the state you want: ').upper()

        if state in available_states:
            # our output filepath
            output_filepath = 'data/' + state.upper() + '/' + state.lower() + '_output.csv'

            # our bp input
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() + '/' \
                     + state.lower() + '_bp_data.csv'
            try:
                bp_data = bp.pd.read_csv(bp_url)
            except urllib.error.HTTPError:
                break
            else:
                bp_df = bp.pd.DataFrame(bp_data)
                converted_bp = bp.convert_ballotpedia(bp_df)
                bp_present = True

            # our ctcl input
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() + '/' \
                       + state.lower() + '_ctcl_data.csv'
            try:
                ctcl_data = bp.pd.read_csv(ctcl_url)
            except urllib.error.HTTPError:
                break
            else:
                ctcl_df = bp.pd.DataFrame(ctcl_data)
                converted_ctcl = ctcl.convert_ctcl(ctcl_df)
                ctcl_present = True

            # our openstates input
            openstates_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() \
                             + '/' + state.lower() + '_openstates_data.csv'
            try:
                openstates_data = bp.pd.read_csv(openstates_url)
            except urllib.error.HTTPError:
                break
            else:
                openstates_df = bp.pd.DataFrame(openstates_data)
                converted_openstates = openstates.convert_openstates(openstates_df)
                openstates_present = True

            # output unified set
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            print(f'BP is {bp_present}; CTCL is {ctcl_present}; OS is {openstates_present}')

            break

        else:
            print("Sorry, we don't have that state available! Maybe we haven't added it, maybe a typo. Try again.")
