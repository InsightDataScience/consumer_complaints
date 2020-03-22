This GitHub repository contains my solution to the coding challenge for Data Engineering program

Given a comma separated input file with 18 columns, Expected Output contains 5 columns, e.g., 

"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100

Summary
The consumer_complaints.py script reads the input file per line and creates a dictionary to get the result file containing the following:

1. product (name should be written in all lowercase)
2. year
3. total number of complaints received for that product and year
4. total number of companies receiving at least one complaint for that product and year
5. highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

Steps to run:

To execute the script move to the main directory of the project and run the following in the terminal:

    python3.7 ./src/consumer_complaints.py ./input/complaints.csv ./output/report.csv
    
Last two arguments should be input and output files, respectively. Two files are generated in the output folder report.csv and error_logfile.txt

Alternatively, to execute use ./run.sh script to run the codes.
