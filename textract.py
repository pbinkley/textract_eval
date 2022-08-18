#!/usr/bin/env python3
from textractcaller.t_call import call_textract, Textract_Features
from trp.trp2 import TDocument, TDocumentSchema
from trp.t_pipeline import order_blocks_by_geo
import trp
import json
import pdb
import sys

imagePath = sys.argv[1]

# Read image content
with open(imagePath, 'rb') as document:
    imageBytes = bytearray(document.read())

# Call AWS Textract
j = call_textract(input_document=imagePath, features=[])
t_doc = TDocumentSchema().load(j) # class 'trp.trp2.TDocument'
#print("t_doc: ", type(t_doc))
# the ordered_doc has elements ordered by y-coordinate (top to bottom of page)
ordered_doc = order_blocks_by_geo(t_doc) # class 'trp.trp2.TDocument'
#print("ordered_doc: ", type(ordered_doc))
t_doc = TDocumentSchema().dump(ordered_doc) #class 'dict'
#print("t_doc: ", type(t_doc))
trp_doc = trp.Document(t_doc) # class 'trp.Document'
#print("trp_doc: ", type(trp_doc))

serialized = TDocumentSchema().dump(ordered_doc) # class 'dict'
#print("Serialized: ", type(serialized))

with open(f"{imagePath}.json", "w") as outfile:
    json.dump((serialized), outfile)

# Capture detected text
text = ''

# Iterate over elements in the document
for page in trp_doc.pages:
    for line in page.lines:
        text += (line.text + "\n")

#with open(f"{imagePath}.txt", "w") as outfile:
#    outfile.write(text)
print(text)
