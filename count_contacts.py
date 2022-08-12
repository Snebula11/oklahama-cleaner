import pandas as pd


def count():
    lines = []

    for inp in ['AZ', 'CA', 'CT', 'GA', 'IL', 'MD', 'MA', 'MS', 'NC', 'WI']:
        # inp = input("Type your state: ")

        bp_filepath = 'data/' + inp.upper() + '/' + inp.lower() + '_bp_data.csv'
        bp_df = pd.DataFrame(pd.read_csv(bp_filepath))
        bp_df = bp_df[bp_df['Stage'] == 'General']
        bp_df.reset_index(inplace=True)
        bp_df = bp_df.loc[bp_df['Office level'].isin(['Federal', 'State'])]
        bp_df.reset_index(inplace=True)

        ctcl_filepath = 'data/' + inp.upper() + '/' + inp.lower() + '_ctcl_data.csv'
        ctcl_df = pd.DataFrame(pd.read_csv(ctcl_filepath))

        bp_emails = 0
        bp_phones = 0
        ctcl_emails = 0
        ctcl_phones = 0

        for row in bp_df.index:
            if not pd.isna(bp_df["Campaign email"][row]) or not pd.isna(bp_df["Other email"][row]):
                bp_emails += 1
            if not pd.isna(bp_df["Campaign phone"][row]):
                bp_phones += 1

        for row in ctcl_df.index:
            if not pd.isna(ctcl_df["Email"][row]):
                ctcl_emails += 1
            if not pd.isna(ctcl_df["Phone"][row]):
                ctcl_phones += 1

        bp_rows = len(bp_df)
        bp_email_coverage = round((bp_emails / bp_rows)*100, 2)
        bp_phone_coverage = round((bp_phones / bp_rows)*100, 2)

        ctcl_rows = len(ctcl_df)
        ctcl_email_coverage = round((ctcl_emails / ctcl_rows)*100, 2)
        ctcl_phone_coverage = round((ctcl_phones / ctcl_rows)*100, 2)

        lines.append(f'{inp.upper()}: \n'
                     f'Ballotpedia covers {bp_email_coverage}% of emails for its {bp_rows} rows\n'
                     f'Ballotpedia covers {bp_phone_coverage}% of phone #s for its {bp_rows} rows\n'
                     f'CTCL covers {ctcl_email_coverage}% of emails for its {ctcl_rows} rows\n'
                     f'CTCL covers {ctcl_phone_coverage}% of phone #s for its {ctcl_rows} rows\n')
    with open('data/contact_info.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')


count()
