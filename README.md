# CSV Reducer 0.1

CSV Reducer is a python script to filter columns from a CSV file with option to remove duplicate rows, saving results in other file.

## Table of contents
* [Installation](#installation)
* [Running aplication](#running-aplication)
* [Contributing](#contributing)
* [License](#license)

## Installation

First of all, clone the project.

```bash
git clone https://github.com/marcellusfrota/csv-reducer.git
```

Enter on created diretory and then use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

or run (linux users):

```bash
make init
```

## Running aplication

### To run application

From root project folder run:

```bash
csv-reducer.py -i my_input_file.csv -o my_output_file.csv
```

### To get help with parameters

```bash
csv-reducer.py -h
```

### To remove duplicated rows

```bash
csv-reducer.py -i my_input_file.csv -o my_output_file.csv -d True
```

### To change CSV separator

```bash
csv-reducer.py -i my_input_file.csv -o my_output_file.csv -s ;
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## TODO