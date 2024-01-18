def decode_bytes(input_bytes):
    # 앞부분의 b' 이후 첫 문자열을 만날 때까지의 \x00”\x00 삭제
    start_index = input_bytes.find(b'\x00"\x00') + 3
    modified_input_bytes = input_bytes[start_index:]

    # 뒷부분의 " 이후 부분을 '로 변경
    modified_input_bytes = modified_input_bytes.replace(b'"\x00', b"'\x00")

    # b'\x00\x3C\x00\x62\x00\x72\x00\x3E'이 있다면 이 부분부터 모든 값을 삭제
    cut_index = modified_input_bytes.find(b'\x00\x3C\x00\x62\x00\x72\x00\x3E')
    if cut_index != -1:
        modified_input_bytes = modified_input_bytes[:cut_index] + b'\x00'
    
    try:
        decoded_string = modified_input_bytes.decode('utf-16-le')
        # '&nbsp;'를 ' '로 변경
        final_result = decoded_string.replace('&nbsp;', ' ')
        return final_result
    except UnicodeDecodeError:
        print("입력된 바이트 배열을 'utf-16-le'로 디코딩하는 데 실패했습니다.")

hex_values = [
              "43 00 71 C5 D0 C5 1C C1 26 00 6E 00 62 00 73 00 70 00 3B 00 04 C8 A1 C1 5C D5 26 00 6E 00 62 00 73 00 70 00 3B 00 08 C6 DC C2 85 C7 C8 B2 E4 B2 0A 00 3C 00 62 00 72 00 3E 00 0A 00 3C 00 62 00 72 00 3E 00 27 34 99 E8 8E 00 01 A9 00 00 00 00 00 00 00 02 00  00 00 01" 
              #헥스 값 여기에 대입            
]

for hex_value in hex_values:
    hex_value = hex_value.replace(" ", "")  # 공백 제거
    input_bytes = bytes.fromhex(hex_value)
    result = decode_bytes(input_bytes)
    print(result)
