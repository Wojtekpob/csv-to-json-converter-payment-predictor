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
    records_list=[]
    for row in reader:
        records_list.append(row)

    return records_list


def convert_from_csv_to_json(csv_file__to_convert_from,json_file_to_convert_to):
    with open(csv_file__to_convert_from) as handle:
        invoice_list=read_from_csv(handle)
        handle.close()
    with open(json_file_to_convert_to,'w') as json_handle:
        write_to_json(json_handle,invoice_list)
        json_handle.close()

convert_from_csv_to_json('test_payment_predictor.csv','converted_csv_file.json')
