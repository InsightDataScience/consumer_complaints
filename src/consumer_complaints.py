"""
Problem:

The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies.

For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company. 

"""

import csv
import sys

input_filename, output_filename = sys.argv[1:]

input_open = open(input_filename, 'r')

data = csv.reader(input_open, delimiter=',')

error_file = open('error_logfile.txt', 'a')

length_header = len(next(data))

data_dict = {}

for eachline in data:
    try:
        product_year_key = (eachline[1].lower(), eachline[0][:4])
        if product_year_key not in data_dict.keys():
            data_dict[product_year_key] = {'Complaint_ID':[eachline[17]], 'Company':[eachline[7]]}
        else:
            data_dict[product_year_key]['Complaint_ID'].append(eachline[17])
            data_dict[product_year_key]['Company'].append(eachline[7].lower())
    except IndexError as err:
        #print(','.join(eachline) + '\nERROR:%s!  The above row should have %s columns to be processed.' % (str(err), str(length_header)))
        error_file.write(','.join(eachline) + '\nERROR:%s!  The above row should have %s columns to be processed.' % (str(err), str(length_header)))
    except BaseException as err:
        #print(','.join(eachline) + err)
        error_file.write(','.join(eachline) + '\n'+str(err))

# Write the output

with open(output_filename, 'wb') as out_file:

    for each_key in sorted(data_dict.keys()):
        product = str('"'+each_key[0]+'"') if ',' in each_key[0] else str(each_key[0])
        total_complaints = len(data_dict[each_key]['Complaint_ID'])
        companies_receiving_complaints = len(set(data_dict[each_key]['Company']))
        line = ','.join([product, str(each_key[1]), str(total_complaints), str(companies_receiving_complaints), str(round((companies_receiving_complaints/total_complaints)*100))])
        line += '\n'
        out_file.write(bytes(line, 'utf8'))
