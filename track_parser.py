import binascii
import re
import base64

def read_file_as_hex(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        return binascii.hexlify(content).decode('utf-8')

file_path = "Cache data path"
hex_content = read_file_as_hex(file_path)

start_hex = '68747470733a2f2f747261636b2e6a616e6469' # track.jandi
end_hex = '0000000000'

pattern = start_hex + '(.*?)' + end_hex
matches = re.findall(pattern, hex_content)

output_file_path = "Text result path"
with open(output_file_path, 'w') as output_file:
    for match in matches:
        if len(match) % 2 != 0: 
            match = match + '0'  
        decoded_match = binascii.unhexlify(match).decode('utf-8', 'ignore')  

        footprint_pattern = 'footprint=(.*?)(?=%3D)'
        footprint_matches = re.findall(footprint_pattern, decoded_match)
        
        for footprint_match in footprint_matches:
            padding_needed = len(footprint_match) % 4
            if padding_needed != 0:
                footprint_match += '=' * (4 - padding_needed)

            base64_decoded = base64.b64decode(footprint_match)
            print(base64_decoded.decode('utf-8'))
            output_file.write(base64_decoded.decode('utf-8') + '\n')