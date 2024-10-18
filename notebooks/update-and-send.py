# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import requests
import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import datetime
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv('sendgrid.env')


# +
def data_from_row(row):
    row_data = {}
    for cell in row.select('td'):
        row_data[cell['headers'][0]] = cell.text
    return row_data

def retrieve_page(page_index,params):
    url = 'https://ocrcas.ed.gov/open-investigations?' + '&'.join([k + '=' + str(v) for k, v in zip(params.keys(),params.values())]) + f'&page={page_index}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    return soup

def page_has_data(page):
    return len(page.select('table')) > 0

def scrape_page(page):
    table = page.select('table')[0].select('tbody')[0]
    df = pd.DataFrame([data_from_row(row) for row in table.select('tr')])
    return df


# -

params = {
    'field_ois_state':'All',
    'field_ois_discrimination_statute':'All',
    'field_ois_type_of_discrimination':'All',
    'items_per_page':20,
    'field_ois_institution':'',
    'field_ois_institution_type':752,
    'field_open_investigation_date_1':str(date.today() - datetime.timedelta(days=7)),
    'field_open_investigation_date_2':str(date.today()),
    'field_open_investigation_date':'',
    'field_open_investigation_date_3':'',
}

tables = []
for i in range(0,99999999):
    page = retrieve_page(i,params)
    if page_has_data(page):
        tables.append(scrape_page(page))
    else:
        break

if len(tables) > 0:
    df = pd.concat(tables)
    df.columns = ['STATE','INST','INST_TYPE','DISCRIMINATION_TYPE','INVEST_START_DATES']

    df = df[['STATE','INST','DISCRIMINATION_TYPE','INVEST_START_DATES']]
    for col in ['STATE','INST','DISCRIMINATION_TYPE']:
        df[col] = df[col].str.strip()

    message = Mail(
        from_email='declan@declanrjb.com',
        to_emails='dbradley@chronicle.com',
        subject=f'{len(df["INST"])} DoE investigations opened last week',
        html_content=f'<p>Investigations spanned {len(df["INST"].unique())} institutions in {len(df["STATE"].unique())} states.</p><br>{df.to_html()}')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(e.message)
