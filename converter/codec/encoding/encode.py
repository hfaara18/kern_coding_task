# A dictionary storing which base comes next given
# the previous base and the current bit.
ENCODE_TRANSITIONS = {
	'A' : {'0' : 'G', '1' : 'C', '2' : 'T'},
	'C' : {'0' : 'T', '1' : 'G', '2' : 'A'},
	'G' : {'0' : 'A', '1' : 'T', '2' : 'C'},
	'T' : {'0' : 'C', '1' : 'A', '2' : 'G'},
}

# A dictionary storing which bit comes next given
# the previous base and the current base.
DECODE_TRANSITIONS = {
	'A' : {'C' : '1', 'G' : '0', 'T' : '2'},
	'C' : {'A' : '2', 'G' : '1', 'T' : '0'},
	'G' : {'A' : '0', 'C' : '2', 'T' : '1'},
	'T' : {'A' : '1', 'C' : '0', 'G' : '2'}
}


# Input: string - a string to be encoded into DNA
# Output: string list - the encoded input as a list of DNA sequences
def encode(myString):
	packets = get_packets(myString)

	templates = []
	for packet in packets:
		templates.append(get_template(packet))

	return templates


# Input: string - a string to be converted to a ternary represenations
# Output: string list - a list of ternary bit string, each corresponding
#		to a character in the input
def get_packets(myStr):
	packets = []
	for c in myStr:
		packets.append(decimal_to_ternary(ord(c)))
	return packets


# Input: string - a single string of ternary bits
# Output: string - a DNA sequence corresponding to the input
def get_template(packet):
	template = []
	template.append(ENCODE_TRANSITIONS['G'][packet[0]])
	for i in range(1,len(packet)):
		prev_base = template[i-1]
		current_bit = packet[i]
		template.append(ENCODE_TRANSITIONS[prev_base][current_bit])
	return "".join(template)


# Input: int - a decimal number to convert to ternary
# Output: string - the input as ternary bits
def decimal_to_ternary(decimal):
	ternary_list = []
	dividend = decimal

	while not (dividend < 3):
		ternary_list.append(str(dividend % 3))
		dividend = dividend // 3

	ternary_list.append(str(dividend))
	return "".join(ternary_list)[::-1]
