from validateDisposable import validateDisposable, disposableDomains
from validateDNS import validateDNS
from validateMX import validateMX
from validateRegex import validateRegex
from read import read
import xlsxwriter


def main():
    disposable_domains = disposableDomains("disposable list.txt")

    excel_file_path = "emails.xlsx"
    emails_to_validate = read(excel_file_path)
    
    excel = xlsxwriter.Workbook('valid ' + excel_file_path)
    worksheet = excel.add_worksheet('valid emails')
    row = 0
    column = 0
    
    for email in emails_to_validate:
        regex = validateRegex(email)
        dns = validateDNS(email)
        mx = validateMX(email, [25, 587, 465])
        disposable = validateDisposable(email, disposable_domains)
        
        if regex and dns and mx and disposable:
            worksheet.write(row, column, email)
            row += 1  

        print(f"\nEmail Validation Results for {email}:")
        print(f"Regex: {'Valid' if regex else 'Invalid'}")
        print(f"DNS Records: {'Valid' if dns else 'Invalid'}")
        print(f"MX Records: {'Valid' if mx else 'Invalid'}")
        print(f"Disposable Email: {'Yes' if disposable else 'No'}")
        
    excel.close()

if __name__ == "__main__":
    main()