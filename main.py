import ballotpedia as bp
import csv

data = pd.read_csv(r'metabase_query_results_1766.csv')
df = pd.DataFrame(data)

if __name__ == '__main__':
    print('hi')