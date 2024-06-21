import sys


def remove_dublicate(input_str):
    result = []
    for char in input_str:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
        elif char == result[-1]:
            result.pop()

    return ''.join(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Example: python alice.py path/to/file.txt")
    else:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as file:
                text = file.read().strip()
                output_text = remove_dublicate(text)
                print(output_text)
        except FileNotFoundError:
            print("File not found")
