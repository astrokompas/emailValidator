from validateDisposable import validateDisposable, disposableDomains
from validateDNS import validateDNS
from validateMX import validateMX
from validateRegex import validateRegex
from filterAndDelete import filterAndDelete
from filterAndKeep import filterAndKeep
from read import read
import xlsxwriter


def main():
    disposable_domains = disposableDomains("disposable list.txt")

    excel_file_path = "file.xlsx"
    
    emails_to_validate = read(excel_file_path)
    
    # filterAndDelete
    # domains_to_delete = ['domain.com']
    # emails_to_validate = filterAndDelete(emails_to_validate, domains_to_delete)

    # filterAndKeep
    # domains_to_keep = ['domain.com']
    # emails_to_validate = filterAndKeep(emails_to_validate, domains_to_keep)
    
    excel = xlsxwriter.Workbook('valid ' + excel_file_path)
    worksheet = excel.add_worksheet('valid emails')
    row = 0
    column = 0
    
    for email in emails_to_validate:
        regex = validateRegex(email)
        if not regex:
            print(f"\nValidation stopped for {email}. Regex validation failed.")
            continue
        
        dns = validateDNS(email)
        if not dns:
            print(f"\nValidation stopped for {email}. DNS validation failed.")
            continue
        
        mx = validateMX(email, [25, 587, 465])
        if not mx:
            print(f"\nValidation stopped for {email}. MX validation failed.")
            continue
        
        disposable = validateDisposable(email, disposable_domains)
        if not disposable:
            print(f"\nValidation stopped for {email}. Disposable validation failed.")
            continue
        
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