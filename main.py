import ballotpedia as bp
import ctcl
import unify

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
            print('got raw bp data')
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/ca_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            print('got raw ctcl data')

            # creating filepath
            output_filepath = 'data/' + state.lower() + '_output.csv'
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            print('converted both datasets')

            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            print(f'output the unified set to a csv at {output_filepath}')

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
