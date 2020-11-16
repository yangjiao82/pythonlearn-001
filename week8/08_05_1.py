fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)  #open the text file
count = 0           #start count variable with 0
for line in fh:     #iterate through each line
    line = line.rstrip()
#    print('Line:', line)
    wds = line.split()
#    print('Words', wds)
    if len(wds) < 2:    # the line needs at least 2 words, otherwise we skip
        continue
#   if len(wds) < 1: This may work, but if a line has only 1 word which is 'from'
# then it will blow up when we print wds[1]
    if wds[0] != 'From':
#        print('Ignore')
        continue
# Guardian in a compound statement, using 'or'
    # if len(wds) < 2 or wds[0] != 'From':    ## checks the 1st statment first
        #continue
    print(wds[1])
    count = count + 1     # this should be part of the loop
print("There were", count, "lines in the file with From as the first word")
