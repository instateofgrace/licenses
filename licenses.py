import clr
clr.AddReference("auth_gen_dll")
from auth_gen_dll import main_entry
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scopes) #access the json key you downloaded earlier
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("GRYD Licensing") #open sheet
sheet = sheet.worksheet("Ответы на форму (1)")
sheet2 = file.open("spokenTable_licenses") #open sheet
sheet2 = sheet2.worksheet("Лист3")
col = sheet.col_values(3)
i = 0
result = []
for i in range(len(col)):
    col[i].replace(" ", "")
    result.append(main_entry.Command(col[i]))
result[0] = "License_key"
cols = f'F1:F{len(result)}'

sheet.update("F1",[[e] for e in result], value_input_option="USER_ENTERED")
print(col)
print(result)
print(len(col))
print(len(result))
