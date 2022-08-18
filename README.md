# textract_eval

This is the source for [https://pbinkley.github.io/textract_eval](https://pbinkley.github.io/textract_eval), which presents a smal set of handwritten documents (1920s-40s) and the OCR text rendered from them by the [AWS Textract](https://aws.amazon.com/textract/) service.

In includes the script I used in my testinging: ```textract.py```. To run it:

- follow the instructions to [set up an AWS Account and create an IAM User, and install the AWS CLI and SDKS](https://docs.aws.amazon.com/textract/latest/dg/analyzing-document-expense.html), with appropriate authorization to all it to run Textract requests. It should create a credentials file and store it in your home directory where Python scripts can find it.
- install dependencies: ```pip install -r requirements.txt```
- run ```./textract.py <image file path>```. The OCR text will be writtent to stdout.

Note that the basic [$US pricing](https://aws.amazon.com/textract/pricing/) for AWS Textract is currently $1.50 for 1000 pages, or 0.15¢ per page, or 6⅔ pages per penny.
