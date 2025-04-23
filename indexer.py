import os
import time

# Global counters
tokens = 0
documents = 0
terms = 0
termindex = 0
docindex = 0 

# Lists to store data
alltokens = []
alldocs = []

# Start time
start_time = time.localtime()   

# === TO BE EDITED IF REQUIRED ===
# Set the directory containing the corpus files
dirname = r"C:\Assignment\cacm"  # Use raw string (r"") to avoid escape characters on Windows

# Read and tokenize each document in the directory
all = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]

for f in all:
    documents += 1
    with open(os.path.join(dirname, f), 'r', encoding='utf-8') as myfile:
        alldocs.append(f)
        data = myfile.read().replace('\n', ' ')
        alltokens.extend(data.split())

# Count total tokens
tokens = len(alltokens)

# Write document dictionary to file
documentfile = open(os.path.join(dirname, 'documents.dat'), 'w', encoding='utf-8')
alldocs.sort()
for f in alldocs:
    docindex += 1
    documentfile.write(f + ',' + str(docindex) + os.linesep)
documentfile.close()

# Sort all tokens and identify unique ones
alltokens.sort()
unique_terms = sorted(set(alltokens))
terms = len(unique_terms)

# Write term dictionary (index.dat) to file
indexfile = open(os.path.join(dirname, 'index.dat'), 'w', encoding='utf-8')
for i in unique_terms:
    termindex += 1
    indexfile.write(i + ',' + str(termindex) + os.linesep)
indexfile.close()

# End time
end_time = time.localtime()

# Output statistics
print('Processing Start Time: {:02d}:{:02d}'.format(start_time.tm_hour, start_time.tm_min))
print("Documents:", documents)
print("Tokens:", tokens)
print("Terms:", terms)
print('Processing End Time: {:02d}:{:02d}'.format(end_time.tm_hour, end_time.tm_min))
