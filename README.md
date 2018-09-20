# Prettify JSON

Pretty print contents of an arbitrary JSON document

# Quickstart

Program requires one argument - path to file to be printed

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
{
        "menu": {
                "id": "file",
                "value": "File",
                "popup": {
                        "menuitem": [
                                {
                                        "value": "New",
                                        "onclick": "CreateNewDoc()"
                                },
                                {
                                        "value": "Open",
                                        "onclick": "OpenDoc()"
                                },
                                {
                                        "value": "Close",
                                        "onclick": "CloseDoc()"
                                }
                        ]
                }
        }
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
