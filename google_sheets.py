from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def fetch_google_sheet(sheet_id, range_name, credentials_file):
    creds = Credentials.from_service_account_file(credentials_file)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return result.get('values', [])

def write_to_google_sheet(sheet_id, range_name, data, credentials_file):
    creds = Credentials.from_service_account_file(credentials_file)
    service = build('sheets', 'v4', credentials=creds)
    body = {"values": data}
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()
    return result
