import ballotpedia as bp
import ctcl
import openstates
import propublica
import unify
import utilities as util
import urllib.error

converted_bp = converted_ctcl = converted_openstates = converted_propublica = None


def merge_data(state):
    global converted_bp, converted_ctcl, converted_openstates, converted_propublica

    # OUTPUT FILEPATH
    output_filepath = 'data/' + state.upper() + '/' + state.lower() + '_output.csv'

    # BP CONVERSION
    bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' + state.upper() + '/' \
             + state.lower() + '_bp_data.csv'
    try:
        bp_data = bp.pd.read_csv(bp_url)
    except urllib.error.HTTPError:
        print('\nNo BP data available.')
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
        print('\nNo CTCL data available.')
        pass
    else:
        ctcl_df = bp.pd.DataFrame(ctcl_data)
        converted_ctcl = ctcl.convert_ctcl(ctcl_df)

    # OPENSTATES CONVERSION
    openstates_url = 'https://data.openstates.org/people/current/' + state.lower() + '.csv'
    openstates_data = bp.pd.read_csv(openstates_url)
    openstates_df = bp.pd.DataFrame(openstates_data)
    converted_openstates = openstates.convert_openstates(openstates_df)

    # PROPUBLICA
    converted_propublica = propublica.convert_propublica(state)

    # OUTPUT MERGED DATASET
    # check if we have all 3
    if converted_bp is not None:
        print(f'Unifying 4 datasets for {state}!')
        unified = unify.unify_bp_ctcl(converted_bp,
                                      converted_ctcl,
                                      third_df=converted_openstates,
                                      fourth_df=converted_propublica)
        unified.to_csv(output_filepath, index=False, encoding='utf-8')
        converted_bp = converted_ctcl = converted_openstates = converted_propublica = None
    # if we do not
    elif converted_bp is None:
        print(f'Unifying 3 datasets for {state}!')
        unified = unify.unify_bp_ctcl(converted_ctcl,
                                      converted_openstates,
                                      third_df=converted_propublica)
        unified.to_csv(output_filepath, index=False, encoding='utf-8')
        converted_bp = converted_ctcl = converted_openstates = converted_propublica = None


if __name__ == '__main__':
    while True:
        all_or_one = input("\nType 'all' to generate data for every state; type 'one' to select a state: ").lower()
        if all_or_one != 'all' and all_or_one != 'one':
            print("\nFor now, just type 'all' or 'one', then you can enter different input!")
        else:
            break

    if all_or_one == 'all':
        for entry in util.states.keys():
            merge_data(entry)

    elif all_or_one == 'one':
        while True:
            chosen_state = input('\nType the postal abbr. of the state you want: ').upper()
            if chosen_state not in util.states.keys():
                print('\nOops, maybe you mistyped. Try a different two-letter state code!')
            else:
                break
        merge_data(chosen_state)
