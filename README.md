Mostly a HOWTO with a couple of helper scripts for adding Amazon purchases to Quicken.
Note that I'm using Quicken for Mac and have no intention of testing on other platforms

# Background
I buy a lot of stuff on Amazon; besides making most day-to-day purchases on it, we also buy online from Whole Foods and have it delivered.  However, Quicken doesn't allow much for way to categorize Amazon spend other than cross-referencing a credit card charge with an order and then splitting the receipt in Quicken.
Furthermore, I sometimes buy discounted Amazon gift cards which makes it even more difficult.
The following is my method for categorizing my Amazon spend.

# General Instructions / Workflow
1. Download an Amazon order history report for a specific period.
2. Import Amazon order history into spreadsheet
2. Go into Quicken and remove all Amazon purchases from the same period and/or applicable gift card purchases
3. Confirm your category mappings
4. Use Excel to create a csv file for import
5. Import the csv file in Quicken and rename the resulting account
6. Be amazed at your beautifully categorized purchases


## Download order history report
Go [here](https://www.amazon.com/gp/b2b/reports) to request an Amazon order history report.  I suggest doing this for a year at a time, but for the first time you do it you could set up a single report up until the present year.  Note that Amazon doesn't seem to be capable of handling more than a few years at a time (it will error out) so try until you succeed.

## Confirm category mappings
If you want to do this in bulk, you can use the script `add_mappings.py` to modify your mapping list.  You'll need a relatively recent Python version (3.8+).  I wrote this on my Mac, feel free to fix it if it doesn't work for you.

## Import Amazon order history into spreadsheet
Note: I do this on Google Sheets, the process may be a bit different in Excel
1. Go to File->Import
2. Select "Upload" and choose the order history report
3. Select "Insert new sheet".  Allow autodetection of the delimiter or select comma.
4. Copy and paste all entries into the amazon-order-history tab.

## Export from Excel and import into Quicken
1. Go to the "for-import" sheet.  The first row should be automatically filled out
2. Count the number of rows you have in the "amazon-order-history" sheet and create the same number in the "for-import" sheet.  Copy the first row all the way down to that number.
3. Check column F ("Category") to confirm that all categories have a mapping.  For those that fail, you can manually add an entry into the "category_mappings" sheet.  All items that don't have a clean mapping will return "Uncategorized".
4. Export the for-import sheet to a CSV.  Rename the CSV to something meaningful like "Amazon-purchase-feb-2021.csv"
5. Import the CSV file into Quicken as a Mint CSV.  In the Mac version of Quicken this is "File"->"Import"->"Mint.com File (CSV)"
6. To keep things clean, you can/should remove any Amazon charges in your other accounts (e.g. credit cards etc) so that the bills don't get counted twice.
