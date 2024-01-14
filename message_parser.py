import os

def print_hex(directory):
    all_results = []

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'rb') as f:
            content = f.read()
            hex_output = content.hex()

            start_hex = "6d657373616765496e707574"
            end_hex = "0000"

            start_index = 0
            while start_index < len(hex_output):
                start_index = hex_output.find(start_hex, start_index)
                if start_index == -1:
                    break
                end_index = hex_output.find(end_hex, start_index)
                if end_index == -1:
                    break

                result = hex_output[start_index + len(start_hex):end_index]
                all_results.append(result)

                print(f"filename: {filename}")
                print(f"hex result: {result}\n")

                start_index = end_index + len(end_hex)

    print("Total:")
    for result in all_results:
        print(result)

print_hex('leveldb path')