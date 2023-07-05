import pandas as pd
import pygsheets


class DataSet:
    """Holds tournament data"""
    def __init__(self):
        self.data_frame = pd.DataFrame(columns=['Date', 'Title', 'Club', 'Distance', 'ClosingDate', 'WithdrawalDate',
                                                'Entries', 'Players', 'Grade', 'Age', 'Cohort', 'Link'])
        self.google_creds = pygsheets.authorize(service_file='./creds.json')
        self.google_sheet = self.google_creds.open('Upcoming Tournaments')
        self.google_worksheet = self.google_sheet[0]
        self.google_worksheet.clear()

    def insert_data(self, data):
        """Inserts a tournaments into the tournament dataset"""
        self.data_frame = self.data_frame._append(data, ignore_index=True)

    def export_google(self):
        """Exports the tournament dataset to Google sheets"""
        self.google_worksheet.set_dataframe(self.data_frame, (1, 1))

    def export_xls(self, start):
        """Exports the tournament dataset to xlsx file"""
        self.data_frame.to_excel(f'tournaments_{start}.xlsx', sheet_name=start)
