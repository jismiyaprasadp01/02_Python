'''
 Task 1: Word Count Script
 Covers: Basic syntax, data types, and file I/O
 Description: Read a text file, count the frequency of each word, and output the results as a 
dictionary.
'''
file=open("word.txt","r")
data=file.read()
words=data.split()
count={}
for i in words:
        if i in count:
                count[i]=count[i]+1
        else:
                count[i]=1
print(count)
file.close()
