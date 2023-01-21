import csv
import json
def write_to_json(file_handle, invoice_list):
    invoices_to_write = {
        "Inputs":
        {
            "WebServiceInput0": invoice_list
        },
        "GlobalParameters":{}
    }
    json.dump(invoices_to_write,file_handle,indent=4)


def read_from_csv(file_handle):
    reader = csv.DictReader(file_handle,delimiter=';')
    print(reader.fieldnames)
    records_list=[]
    for row in reader:
        print(row)
        records_list.append(row)

    return records_list


with open('test_payment_predictor.csv') as handle:
    invoice_list=read_from_csv(handle)
    handle.close()


with open('converted_csv_file.json','w') as json_handle:
    write_to_json(json_handle,invoice_list)
    json_handle.close()