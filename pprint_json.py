import json
import sys


def load_content_from_file(filepath):
    with open(filepath) as json_file:
        decoded_file_content = json.load(json_file)
        return decoded_file_content


def pretty_print(decoded_file_content):
    prettified_string = json.dumps(
        decoded_file_content, ensure_ascii=False, indent="\t"
    )
    print(prettified_string)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No filename argument")

    filename = sys.argv[1]
    try:
        decoded_file_content = load_content_from_file(filename)
        pretty_print(decoded_file_content)
    except FileNotFoundError:
        sys.exit("No such file")
    except json.JSONDecodeError:
        sys.exit("File contents is not a valid JSON document")
