from openpyxl import load_workbook
from pathlib import Path


def get_excel_data():

    # Get project root directory
    project_path = Path(__file__).resolve().parents[1]

    # Excel file location
    excel_path = project_path / "testdata" / "testdata.xlsx"

    workbook = load_workbook(excel_path)

    sheet = workbook["SearchData"]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    workbook.close()

    return data