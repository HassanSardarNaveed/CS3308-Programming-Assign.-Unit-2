# CS3308-Programming-Assign.-Unit-2
 Assignment Description:
This assignment focuses on building an initial version of an inverted indexer for a collection of article documents submitted to the journal "Communications of the Association for Computing Machinery (CACM)." The purpose is to extract and index all unique terms from the corpus and associate them with their respective documents.

The Python script processes the corpus directory by reading all document files, tokenizing their content, identifying unique terms, and assigning index numbers to both documents and terms. The results are written to two separate files:

documents.dat: maps each document filename to a document index.

index.dat: maps each unique term to a term index.

🔍 Observations:
The tokenizer in the current version is basic (splits on whitespace), so terms may still include punctuation. This could be enhanced in future versions using regular expressions or libraries like nltk.

The use of set() significantly improved the performance in extracting unique terms, especially with large datasets.

The code tracks important metrics such as total documents, total tokens (words), and total unique terms, giving a good overview of the corpus structure.

Performance remained reasonable even with a larger number of documents (e.g., 300+), with execution times under a minute.

This foundational structure prepares the way for building the final inverted index that links terms directly to the documents they appear in.
