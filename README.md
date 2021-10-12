# Sypht Programming Excercises

The following are programming excercises for Sypht

## Getting Started

You will need to register a developer account with Sypht to obtain API credentials. Once registered you can obtain your `CLIENT_ID` and `CLIENT_SECRET`.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies and clone the repository.

```bash
pip install numpy flask sypht json2html pandas nltk scikit-learn
git clone https://github.com/christopher-nicol/sypht-excercises.git
```

Update and save your user credentials in `1-sypht-api/credentials.py`.

```python
CLIENT_ID = ""
CLIENT_SECRET = ""
```

## Usage

#### Mandatory Problem: Date Calculator

In your shell/terminal, navigate to the directory `/0-mandatory-problem` and then execute the script `main.py`

```bash
python main.py
```

You will be prompted to input the start and end dates that you would like to determine the number of days between. Enter them in the format DD/MM/YYYY:

```bash
Enter start date (in DD/MM/YYYY format): 04/07/1984
Enter end date (in DD/MM/YYYY format): 25/12/1984
```

Following this, the script will output the number of full days between the two dates entered:

```bash
There are 173 full days between 04/07/1984 and 25/12/1984
```

#### Bonus Problem #1: Sypht API

In your shell/terminal, navigate to the directory `/1-sypht-api` and then execute the script `app.py`

```bash
python app.py
```

Using your web browser, navigate to `localhost:5000`.

Make sure your invoice/file is located in the same directory and use the Upload and Submit buttons to retrieve the relevant data (a sample invoice has been provided in the repository called `invoice.pdf`).

On submit, you will be redirected to a summary page where you can then view the entire JSON payload with the button at the bottom of the page.

#### Bonus Problem #2: Progress Pie

In your shell/terminal, navigate to the directory `/2-progress-pie` and then execute the script `main.py`

```bash
python main.py
```

You will be prompted to input the number of points you would like to examine, T. It must be between an integer between 1 and 1000, entering a number outside this range will prompt you to re-input T (refer to example below):

```bash
Enter the number of points: 10000
T must be between 1 and 1000
Enter the number of points: 5
```

Once you enter a valid number for T, you will then input the point coordinates (X, Y) and percentages (P) for the cases you want to examine in the format [P X Y]. If P, X or Y :

```bash
Enter the number of points: 10000
T must be between 1 and 1000
Enter the number of points: 5
Enter Case 1 input here (in the format [% X Y]): 0 55 55
Enter Case 2 input here (in the format [% X Y]): 12 55 55
Enter Case 3 input here (in the format [% X Y]): 13 55 55
Enter Case 4 input here (in the format [% X Y]): 99 99 99
Enter Case 5 input here (in the format [% X Y]): 87 20 40
```

The results of each case will output in the shell as follows:

```bash
Case #1: white
Case #2: white
Case #3: black
Case #4: white
Case #5: black
```

##### Bonus Problem #3: Sentiment Analysis

Open the notebook using Jupyter Notebook and run the cells.

## Project Structure

```
.
├── 0-mandatory-problem
│   └── main.py
├── 1-sypht-api
│    ├── templates
│    │   ├── index.html
│    │   ├── results.html
│    │   └── summary.html
│    ├── app.py
│    └── invoice.pdf
├── 2-progress-pie
│   └── main.py
├── 3-sentiment-analysis
│    ├── input
│    │   ├── amazon_cells_labelled.txt
│    │   ├── imdb_labelled.txt
│    │   └── yelp_labelled.txt
│    └── sentiment.ipynb
├── .gitignore
├── LICENSE
└── README.md
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
