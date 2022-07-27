import ballotpedia as bp
import ctcl

if __name__ == '__main__':
    # input loop
    while True:
        # take user input
        state = input('Type the postal abbr. of the state you want: ').upper()

        if state == 'CA':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/ca_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/ca_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # creating filepath
            output_filepath = 'data/' + state.lower() + '_output.csv'
            # output california data
            ctcl.convert_ctcl(ctcl_df).to_csv(output_filepath, index=False)
            # bp.convert_ballotpedia(bp_df).to_csv(output_filepath, index=False)
            break
        elif state == 'OK':
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/ok_ctcl_data.csv'
            ctcl_data = ctcl.pd.read_csv(ctcl_url)
            ctcl_df = ctcl.pd.DataFrame(ctcl_data)
            # creating filepath
            output_filepath = 'data/' + state.lower() + '_output.csv'
            # output oklahoma data
            ctcl.convert_ctcl(ctcl_df).to_csv(output_filepath, index=False)
            break
        else:
            print("\nSorry, we couldn't find that state. Please try again using a two-letter postal code.\n")
