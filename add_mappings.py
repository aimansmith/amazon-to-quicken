#!/usr/bin/env python3
# Want python 3.8+

# to make life easier, have your amazon order history csv as amazon-order-history.csv
#   and category mappings as category_mappings.csv
# Could set these as arguments as well if I was willing to write that
orderHistoryFile='amazon-order-history.csv'
categoryMappingFile='category_mappings.csv'

import getopt, sys, csv

def addCategoryWithoutMapping(amazonCategory):
    with open(categoryMappingFile, 'a') as file:
        file.write(amazonCategory + "\r\n")
    file.close()

def addMapping(amazonCategory,quickenCategory):
    with open(categoryMappingFile, 'a') as file:
        file.write(amazonCategory + "," + quickenCategory + "\r\n")
    file.close()

def getMapping(amazonCategory):
    quickenCategory=input("Please enter a Quicken category for Amazon category " + amazonCategory + ": ")
    if DUMMY==0:
        addMapping(amazonCategory,quickenCategory)
    else:
        print("DUMMY: not adding value but I would totally do it here")

# Deal w/ options
DUMMY=0
NOPROMPTS=0

options = "nd:"
long_options = ["no-prompts", "dummy"]
argumentList = sys.argv[1:]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-n", "--no-prompts"):
            print ("Will not prompt for values")
            NOPROMPTS=1
             
        elif currentArgument in ("-d", "--dummy"):
            print ("Dummy mode, not doing anything")
            DUMMY=1
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

seen={}
categorySamples={}
knownMapping={}
with open(orderHistoryFile, 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        #print(row['Category'])
        seen[row['Category']]=1
        if row['Category'] in categorySamples:
            categorySamples[row['Category']].append(row['Title'])
        else:
            categorySamples[row['Category']]=[]
            categorySamples[row['Category']].append(row['Title'])
file.close()
with open(categoryMappingFile, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        knownMapping[row[0]]=row[1]
file.close()
for category in seen.keys():
    if not category in knownMapping:
        if NOPROMPTS==1:
            if DUMMY==1:
                print("dummy mode: no-prompts selected: I would add " + category + " to category mapping file without a Quicken category")
            else:
                print("no-prompts selected: Adding " + category + " to category mapping file without a Quicken category")
                addCategoryWithoutMapping(category)
        else:
            print("Seem to be missing category: " + category)
            print("Samples for " + category + ":")
            for sample in categorySamples[category]:
                print("   " + sample)
            getMapping(category)
