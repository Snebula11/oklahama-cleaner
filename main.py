import ballotpedia as bp
import ctcl
import openstates
import propublica
import unify
import utilities as util
import urllib.error

if __name__ == '__main__':
    available_states = ['AZ', 'CA', 'GA', 'MA', 'IL', 'MD', 'MS', 'NY', 'OK']
    go = False

    # input loop
    # for state in util.states.keys():
    while True:

        state = input('Type the postal abbr. of the state you want: ').upper()

        # OUTPUT FILEPATH
        output_filepath = 'data/' + state.upper() + '/' + state.lower() + '_output.csv'

        # BP CONVERSION
        bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() + '/' \
                 + state.lower() + '_bp_data.csv'
        try:
            bp_data = bp.pd.read_csv(bp_url)
        except urllib.error.HTTPError:
            print('No BP data available')
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
            print('No CTCL data available')
            pass
        else:
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)

        # OPENSTATES CONVERSION
        openstates_url = 'https://data.openstates.org/people/current/' + state.lower() + '.csv'
        try:
            openstates_data = bp.pd.read_csv(openstates_url)
        except urllib.error.HTTPError:
            print('No Open States data available')
            break
        else:
            openstates_df = bp.pd.DataFrame(openstates_data)
            converted_openstates = openstates.convert_openstates(openstates_df)

        # PROPUBLICA
        converted_propublica = propublica.convert_propublica(state)

        # OUTPUT MERGED DATASET
        # check if we have all 3
        try:
            unified = unify.unify_bp_ctcl(converted_bp,
                                          converted_ctcl,
                                          third_df=converted_openstates,
                                          fourth_df=converted_propublica)
        # if we do not
        except NameError:
            print(f'unifying datasets for {state}')
            unified = unify.unify_bp_ctcl(converted_ctcl, converted_openstates, third_df=converted_propublica)
            unified.to_csv(output_filepath, index=False, encoding='utf-8')
            # pass
            # break
        # if we do have all 3
        else:
            print(f'unifying datasets for {state}')
            unified.to_csv(output_filepath, index=False, encoding='utf-8')
            # break
