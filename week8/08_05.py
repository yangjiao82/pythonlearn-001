fname = input("Enter file name: ") #open the file mbox-short.txt and read each line.
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)  #open the text file
count = 0           #start count variable with 0
for line in fh:     #iterate through each line
    line = line.rstrip()
    if not line.startswith("From "):
        continue  #skip
    email = line.split()  #split line into words
    if len(email) < 2:
        print(email[:])
    print(email[1])       # print the second word in the list
    count = count + 1     # this should be part of the loop
print("There were", count, "lines in the file with From as the first word")
