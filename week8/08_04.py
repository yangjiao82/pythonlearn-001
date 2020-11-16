fname  = input("Enter file name: ")
fh = open(fname) #assign the txt file to filehandle
lst = list()    #create an empty list called lst
for line in fh:  # read each line in 'fh'
    for w in line.split():  # Iterates through each word on line
        if w not in lst:    # check if word is in list
            lst.append(w)   # append the word in the list
lst.sort()                  # sort the list
print(lst)                  # print the sorted list


#if I use lst=lst.sort(); or lst=lst.append();
#this program would only remember the last line because
#the previous line was repalced

#output is ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
