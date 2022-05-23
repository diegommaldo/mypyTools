import os 
import csv

# table with headers > column 1 "oldname", column 2 "newname"
# don't forget to add extension at the "newname"

csvFile = 'file.csv'

originFolder = 'path folder'

newFolder = 'path Folder'

# open and store the csv file
IDs = {}
with open(csvFile) as csvfile:
    timeReader = csv.reader(csvfile, delimiter = ',')
    # build dictionary with associated IDs
    for row in timeReader:
        IDs[row[0]] = row[1]

# move files
path = originFolder
tmpPath = newFolder

for oldname in os.listdir(path):
    # ignore files in path which aren't in the csv file
    if oldname in IDs:
        try:
            os.rename(os.path.join(path, oldname), os.path.join(tmpPath, IDs[oldname]))
        except:
            print ('File ' + oldname + ' could not be renamed to ' + IDs[oldname] + '!')