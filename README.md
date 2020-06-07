# Kern Coding Task
The app includes two input forms, one to convert a "string" to "DNA template(s)" and another to convert "DNA template(s)" to a "string". 

#### project setup
- **string to DNA template(s) conversion**: When a query is submitted, a post request is submitted, which is handled by the **Conversions.post()** method in **converter/views.py**. The method extracts the input from the query, and then call **encode()** with the input to get a DNA template(s). The output is sent back to be displayed on the page and a dictionary with the nucleotide dcounts from the output, which is calculated by **get_nucleotide_counts()**, is passed to the page to be processed by a javscript codeblock in the page. The javascript codeblock then uses d3.js to create a bar chart showing each nuclotide count.

- **DNA template(s) to string conversion**: When a query is submitted, a post request is submitted, which is handled by the **Conversions.post()** method in **converter/views.py**. The method extracts the input from the query, and then call **decode()** with the input to get a string. The output is sent back to be displayed on the page.

#### Additional functions in codec/encoding/decode.py
- **template_to_packet**: converts a given DNA sequence to a ternary string
- **ternary_to_decimal**: converts a given ternary string to a decimal
- **packets_to_string**: converts a list of decimal packets to a string
- **decode**: given a list of DNA sequences, returns the decoded output as a string