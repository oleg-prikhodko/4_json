import json
import sys


def load_data(filepath):
    try:
        with open(filepath) as json_file:
            json_data = json.load(json_file)
            return json_data
    except FileNotFoundError:
        sys.exit("No such file")
    except OSError:
        sys.exit("File cannot be opened")
    except UnicodeDecodeError:
        sys.exit("Not a text file")
    except json.JSONDecodeError:
        sys.exit("File contents is not a valid JSON document")


def pretty_print_json(json_data):
    json_string = json.dumps(json_data, ensure_ascii=False, indent="\t")
    print(json_string)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No filename argument")
    else:
        filename = sys.argv[1]
        json_data = load_data(filename)
        pretty_print_json(json_data)
