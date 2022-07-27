import pandas as pd

import ballotpedia as bp
import ctcl

if __name__ == '__main__':
    # input loop
    while True:
        # take user input
        state = input('Type the postal abbr. of the state you want: ').upper()

        if state == 'CA':
            url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/all_california_candidates.csv'
            data = bp.pd.read_csv(url)
            df = bp.pd.DataFrame(data)
            bp.convert_ballotpedia(df).to_csv('out_bp.csv', index=False)
            break
        elif state == 'OK':
            data = ctcl.pd.read_csv('/Users/benswedberg/Desktop/oklahama-cleaner/OK_candidates.csv')
            df = ctcl.pd.DataFrame(data)
            ctcl.candidates(df).to_csv('out_ctcl.csv', index=False)
            break
        else:
            print("\nSorry, we couldn't find that state. Please try again using a two-letter postal code.\n")
