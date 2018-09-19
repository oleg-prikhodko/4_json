# Prettify JSON

Скрипт выводит отформатированное содержание файла с произвольными данными в формате JSON 

# Quickstart

Скрипт принимает на вход один аргумент - путь к файлу

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
