#!/usr/bin/env python3

import fastwer
import os
import csv

with open('wer_data.csv', mode='w', newline='') as wer_data:
  rows = []
  
  files = os.listdir("./ground/")
  files.sort()
 
  for filename in files:
    print(filename)

    f = open("ground/" + filename, "r")
    ground = f.read()
    f.close()

    f = open("ocr/" + filename, "r")
    ocr = f.read()
    f.close()

    cer = fastwer.score_sent(ocr, ground, char_level=True)
    wer = fastwer.score_sent(ocr, ground, char_level=False)

    row = {
        "filename": filename, 
        "cer": round(cer, 1),
        "wer": round(wer, 1),
        "glen": len(ground),
        "olen": len(ocr)
    }
    
    rows.append(row)  
  
  rows.sort(key=lambda row: row.get("cer"))
  
  
  keys = rows[0].keys()

  dict_writer = csv.DictWriter(wer_data, keys)
  dict_writer.writeheader()
  dict_writer.writerows(rows)
