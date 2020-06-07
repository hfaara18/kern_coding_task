# A dictionary storing which bit comes next given
# the previous base and the current base.
DECODE_TRANSITIONS = {
	'A' : {'C' : '1', 'G' : '0', 'T' : '2'},
	'C' : {'A' : '2', 'G' : '1', 'T' : '0'},
	'G' : {'A' : '0', 'C' : '2', 'T' : '1'},
	'T' : {'A' : '1', 'C' : '0', 'G' : '2'}
}


# Input: string list - a list of DNA sequences as strings
# Output: string - the decoded output as a string
def decode(templates):
	packets = [template_to_packet(template) for template in templates]
	decimal_packets = [ternary_to_decimal(packet) for packet in packets]
	string = packets_to_string(decimal_packets)
	return string

# Input: string - a DNA sequence as a string
# Output: string - a decimal encoding of input DNA sequence
def template_to_packet(template):
	packet = []
	packet.append(DECODE_TRANSITIONS['G'][template[0]])
	for i in range(1,len(template)):
		prev_base = template[i-1]
		current_base = template[i]
		packet.append(DECODE_TRANSITIONS[prev_base][current_base])
	return "".join(packet)

# Input: string - a ternary number as a string
# Output: int - a decimal representation of ternary input
def ternary_to_decimal(ternary):
	decimal = 0
	for i in range(len(ternary)):
		decimal += (int(ternary[i]))*3**(len(ternary) - i - 1)
	return decimal

# Input: int list - a list of decimal representations of string characters
# Output: string - a string from decoded decimal packets
def packets_to_string(packets):
	letters = [chr(packet) for packet in packets]
	return "".join(letters)
