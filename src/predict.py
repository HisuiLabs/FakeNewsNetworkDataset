import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# predict the target on the test dataset
def predict(json_data):
    model = pickle.load(open('model/random_forest_model.pkl','rb'))
    df = pd.DataFrame(json_data, index=[0])
    df['created_date'] = pd.to_datetime(df['created_date']).astype(int)/ 10**9
    df['updated_date'] = pd.to_datetime(df['updated_date']).astype(int)/ 10**9
    df['expires_date'] = pd.to_datetime(df['expires_date']).astype(int)/ 10**9
    df['nameservers'] = ','.join(df['nameservers'][0]) if isinstance(df['nameservers'][0], list) else df['nameservers'][0]
    df['status'] = ','.join(df['status'][0]) if isinstance(df['status'][0], list) else df['status'][0]
    for column in df.columns:
        if df[column].dtype == type(object):
            le = LabelEncoder()
            df[column] = df[column].fillna('')
            df[column] = le.fit_transform(df[column])
    # df = df.reindex(columns = X.columns, fill_value=0)
    feature_names = model.feature_names_in_
    df = df[feature_names]
    prediction = model.predict(df)[0]
    return prediction

json_data = {
    'URL': 'https://bitcoin.org/',
    'abuse_email': 'abuse@namecheap.com',
    'abuse_phone': None,
    'admin_address': 'Kalkofnsvegur 2, Reykjavik, Capital Region, 101, IS',
    'admin_email': '43280f540155444088dee67adf69c821.protect@withheldforprivacy.com',
    'admin_fax': None,
    'admin_name': 'Redacted for Privacy',
    'admin_organization': 'Privacy service provided by Withheld for Privacy ehf',
    'admin_phone': None,
    'billing_address': None,
    'billing_email': None,
    'billing_fax': None,
    'billing_name': None,
    'billing_organization': None,
    'billing_phone': None,
    'created_date': '2008-08-18 13:19:55',
    'domain_name': 'bitcoin.org',
    'expires_date': '2029-08-18 13:19:55',
    'nameservers': 'keanu.ns.cloudflare.com',
    'registrant_address': 'Kalkofnsvegur 2, Reykjavik, Capital Region, 101, IS',
    'registrant_email': '43280f540155444088dee67adf69c821.protect@withheldforprivacy.com',
    'registrant_fax': None,
    'registrant_name': 'Redacted for Privacy',
    'registrant_organization': None,
    'registrant_phone': None,
    'registrar_address': '4600 E Washington St #305, Phoenix, Arizona, 85034',
    'registrar_email': 'support@namecheap.com',
    'registrar_fax': None,
    'registrar_name': 'NAMECHEAP INC',
    'registrar_phone': None,
    'status': 'client transfer prohibited',
    'technical_address': 'Kalkofnsvegur 2, Reykjavik, Capital Region, 101, IS',
    'technical_email': '43280f540155444088dee67adf69c821.protect@withheldforprivacy.com',
    'technical_fax': None,
    'technical_name': 'Redacted for Privacy',
    'technical_organization': 'Privacy service provided by Withheld for Privacy ehf',
    'technical_phone': None,
    'updated_date': '2019-11-24 13:58:35'
}
print(predict(json_data))