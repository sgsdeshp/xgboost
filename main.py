import pandas as pd
import xgboost as xgb
import gspread
import os

file = os.environ.get('PMGCPKEY')
# Google service account authentication
sa = gspread.service_account(filename=file)
# select workbook
sh = sa.open('PM Sales Export')
# select worksheet
wks = sh.worksheet('ValidOrders')
# get all records as pandas data frame
df = pd.DataFrame(wks.get_all_records())
