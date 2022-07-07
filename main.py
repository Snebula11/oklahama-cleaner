import ballotpedia as bp


if __name__ == '__main__':
    bp.challengers().to_csv('out.csv', index=False)
