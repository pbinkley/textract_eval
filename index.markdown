---
layout: simplehome
---

<div id="update" style="text-align: right; margin-bottom: 1em; font-size: small">Updated on {{ site.time | date: "%a, %d %b, %Y" }}</div>

This is set of results from the [AWS Textract](https://aws.amazon.com/textract/) service to demonstrate its ability to handle 
handwritten text. I processed about 5000 handwritten pages from the 1920s-40s, mostly letters or rough notes. I then randomly selected 50 pages for this demonstration. I prepared ground truth files for each of the sample pages manually, and used [fastwer](https://github.com/kahne/fastwer) to calculate the Character Error Rate and Word Error Rate (CER and WER). In the [table](#table) below you can see the sample pages, sorted by CER from best to worst. Click the sample image to see the text returned by Textract and the page image.

The Python script used in this testing is available in the [main branch](https://github.com/pbinkley/textract_eval)

## Notes on method

- I removed the text of any printed letterheads from the OCR and the ground truth, so as to evaluate only the handwritten text

## Observations

- wide line spacing is good
- it's remarkably good at ignoring printed lines or graph pattern
- sloped lines are very bad (see [corr.1930-32_C_3611_002](#corr.1930-32_C_3611_002) - the last sample) - Textract doesn't do well at following the slope - I am using ```order_blocks_by_geo```, which sorts the blocks by their y coordinates and fixes the fairly common problem of getting two lines out of order, but with sloped lines it ends up mingling the words to two consecutive lines. If you want the words and don't care about the order, the results are usable.
- when it's good, it is quite good, probably due to a good match of the hand of the image to the hands Textract was trained on

## Table

<table>
  <thead>
  <tr>
    <th>File</th>
    <th>Sample (click for OCR and page image)</th>
    <th><abbr title="Character Error Rate">CER</abbr></th>
    <th><abbr title="Word Error Rate">WER</abbr></th>
  </tr>
  </thead>
  <tbody>
  {% for row in site.data.wer_data %}
    {% if forloop.first %}
    {% endif %}
    {% assign filename = row["filename"] | replace: '.txt', '' %}
    <tr id="{{ filename }}">
      <td>{{ filename }}</td>
      <td><a href="pages/{{ filename }}.html" rel="nofollow" title="{{ filename }}"><img src="samples/{{ filename }}.jpg"/></a></td>
      <td class="dec">{{ row["cer"] }}</td>
      <td class="dec">{{ row["wer"] }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
