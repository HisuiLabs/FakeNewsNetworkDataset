import pandas
from urllib.parse import urlparse
import asyncio
from pprint import pprint
import whodap
import time

def main():
    # read table in data/label.tsv
    df = pandas.read_csv('data/label.tsv', sep='\t')
    print(df['URL'])
    # get a domain
    df['domain'] = ''
    for i in range(len(df)):
        url = df['URL'][i]
        domain = urlparse(url).netloc
        df['domain'][i] = domain
    print(df['domain'])

    # get a scheme
    df['scheme'] = ''
    for i in range(len(df)):
        url = df['URL'][i]
        scheme = urlparse(url).scheme
        df['scheme'][i] = scheme
    print(df['scheme'])

    # get a tld
    df['tld'] = ''
    df['domains'] = ''
    for i in range(len(df)):
        url = df['URL'][i]
        tld = urlparse(url).netloc.split('.')[-1]
        domains = urlparse(url).netloc.split('.')[-2]
        df['tld'][i] = tld
        df['domains'][i] = domains
        df
    print(df['tld'])
    print(df['domains'])

    whois_json = []

    # whois = whodap.lookup_domain(domain=df['domains'][i], tld=df['tld'][i])

    for i in range(len(df)):
        try:
            if df['tld'][i] != 'jp':
                result = whodap.lookup_domain(domain=df['domains'][i], tld=df['tld'][i])
                whois = result.to_whois_dict()
                whois_json.append(whois)
                time.sleep(1)
        except:
            print('error')
            time.sleep(1)
    print(whois_json)
        
    whois_json = pandas.DataFrame(whois_json)
    whois_json.to_csv('data/whois.csv', index=False)

def makecsv():
    df = pandas.read_csv('data/label.tsv', sep='\t')
    df1 = pandas.read_csv('data/whois.csv')

    url = df['URL']
    df['label'] = df['Q1']
    label = df['label']

    new_df = pandas.concat([url, df1, label], axis=1)
    new_df.to_csv('data/whois_label.csv', index=False)


# main()
makecsv()