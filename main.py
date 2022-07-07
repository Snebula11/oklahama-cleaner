import ballotpedia as bp


if __name__ == '__main__':
    # input loop
    while True:
        # take user input
        state = input('Type the postal abbr. of the state you want: ').upper()

        if state == 'CA':
            url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/all_california_candidates.csv'
            data = bp.pd.read_csv(url)
            df = bp.pd.DataFrame(data)
            break
        else:
            print("\nSorry, we couldn't find that state. Please try again using a two-letter postal code.\n")

    bp.challengers(df).to_csv('out.csv', index=False)
