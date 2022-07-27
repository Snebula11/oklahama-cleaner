import ballotpedia as bp
import ctcl

if __name__ == '__main__':
    # input loop
    while True:
        # take user input
        state = input('Type the postal abbr. of the state you want: ').upper()

        if state == 'CA':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data' \
                     '/all_california_candidates.csv '
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # creating filepath
            output_filepath = 'data/' + state.lower() + '_output.csv'
            # output california data
            bp.convert_ballotpedia(bp_df).to_csv(output_filepath, index=False)
            break
        elif state == 'OK':
            data = ctcl.pd.read_csv('/Users/benswedberg/Desktop/oklahama-cleaner/OK_candidates.csv')
            df = ctcl.pd.DataFrame(data)
            ctcl.candidates(df).to_csv('data/out_ctcl.csv', index=False)
            break
        else:
            print("\nSorry, we couldn't find that state. Please try again using a two-letter postal code.\n")
