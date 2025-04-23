#  Example code in python programming language demonstrating some of the features of an inverted index.
#  In this example, we scan a directory containing the corpus of files. (In this case the documents are reports on articles
#  and authors submitted to the Journal "Communications of the Association for Computing Machinery"  
#
#  In this example we see each file being read, tokenized (each word or term is extracted) combined into a sorted 
#  list of unique terms.  
#
#  We also see the creation of a documents dictionary containing each document in sorted form with an index assigned to it.
#  Each unique term is written out into a terms dictionary in sorted order with an index number assigned for each term.  
#  From our readings we know that to complete teh inverted index all that we need to do is create a third file that will
#  coorelate each term with the list of documents that it was extracted from.  We will do that in a later assignment.
##
#  We can further develop this example by keeping a reference for each term of the documents that it came from and by 
#  developing a list of the documents thus creating the term and document dictionaries. 
#
#  As you work with this example, think about how you might enhance it to assign a unique index number to each term and to 
#  each document and how you might create a data structure that links the term index with the document index. 


import os
import time

# Define global counters
tokens = 0
documents = 0
terms = 0
termindex = 0
docindex = 0

# Initialize lists
alltokens = []
alldocs = []

# Capture start time
t2 = time.localtime()

# Set directory path
dirname = r"C:\Users\croom\Downloads\Compressed\New folder (3)\cacm"

# Read and tokenize each document in the directory
all_files = [f for f in os.listdir(dirname)]
for f in all_files:
    documents += 1
    with open(os.path.join(dirname, f), 'r', encoding='utf-8') as myfile:
        alldocs.append(f)
        data = myfile.read().replace('\n', '')
        for token in data.split():
            alltokens.append(token)
            tokens += 1

# Write document dictionary to file
documentfile = open(os.path.join(dirname, 'documents.dat'), 'w', encoding='utf-8')
alldocs.sort()
for f in alldocs:
    docindex += 1
    documentfile.write(f + ',' + str(docindex) + os.linesep)
documentfile.close()

# Sort tokens
alltokens.sort()

# Identify unique terms
g = []
for i in alltokens:
    if i not in g:
        g.append(i)
        terms += 1

# Write term index to file
indexfile = open(os.path.join(dirname, 'index.dat'), 'w', encoding='utf-8')
for i in g:
    termindex += 1
    indexfile.write(i + ',' + str(termindex) + os.linesep)
indexfile.close()

# Output metrics
print('Processing Start Time: {:02d}:{:02d}'.format(t2.tm_hour, t2.tm_min))
print("Documents:", documents)
print("Tokens:", tokens)
print("Terms:", terms)

t2 = time.localtime()
print('Processing End Time: {:02d}:{:02d}'.format(t2.tm_hour, t2.tm_min))
