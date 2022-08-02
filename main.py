import ballotpedia as bp
import ctcl
import unify


if __name__ == '__main__':
    # input loop
    while True:
        # take user input
        state = input('Type the postal abbr. of the state you want: ').upper()
        output_filepath = 'data/' + state.upper() + '/' + state.lower() + '_output.csv'

        if state == 'AZ':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/AZ/az_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/AZ/az_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            break
        elif state == 'CA':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/CA/ca_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/CA/ca_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            break
        elif state == 'GA':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/GA/ga_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/GA/ga_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            break
        elif state == 'MA':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/MA/ma_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/MA/ma_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            break
        elif state == 'MD':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/MD/md_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/MD/md_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            break
        elif state == 'MS':
            # getting ballotpedia data
            bp_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/MS/ms_bp_data.csv'
            bp_data = bp.pd.read_csv(bp_url)
            bp_df = bp.pd.DataFrame(bp_data)
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/MS/ms_ctcl_data.csv'
            ctcl_data = bp.pd.read_csv(ctcl_url)
            ctcl_df = bp.pd.DataFrame(ctcl_data)
            # create bp and ctcl california data
            converted_bp = bp.convert_ballotpedia(bp_df)
            converted_ctcl = ctcl.convert_ctcl(ctcl_df)
            # unify and output the merged data
            unify.unify_bp_ctcl(converted_bp, converted_ctcl).to_csv(output_filepath, index=False, encoding='utf-8')
            break
        elif state == 'NY':
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/NY/ny_ctcl_data.csv'
            ctcl_data = ctcl.pd.read_csv(ctcl_url)
            ctcl_df = ctcl.pd.DataFrame(ctcl_data)
            # output oklahoma data
            ctcl.convert_ctcl(ctcl_df).to_csv(output_filepath, index=False)
            break
        elif state == 'OK':
            # getting ctcl data
            ctcl_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/OK/ok_ctcl_data.csv'
            ctcl_data = ctcl.pd.read_csv(ctcl_url)
            ctcl_df = ctcl.pd.DataFrame(ctcl_data)
            # output oklahoma data
            ctcl.convert_ctcl(ctcl_df).to_csv(output_filepath, index=False)
            break
        else:
            print("\nSorry, we couldn't find that state. Please try again using a two-letter postal code.\n")
