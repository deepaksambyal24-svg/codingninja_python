# Python & Data Science Learning Portfolio

A structured portfolio of Python practice, data structures and algorithms, object-oriented programming, and introductory data-science work.

The repository records an ongoing learning journey. It contains independent exercises as well as selected documented projects; not every historical script is production-ready or independently tested.

## Data science focus

Start with the [Data Science & Data Analysis guide](04-data-science-and-analysis/README.md).

**Featured runnable project:** [Vehicle Rental Pricing — Exploratory Data Analysis](04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/README.md). This project demonstrates dataset validation, descriptive statistics, grouped analysis, visualizations, and automated tests using a small included sample dataset.

Data-science topics covered include:
- Python, Pandas and NumPy
- Data cleaning, missing-value handling and data validation
- Exploratory data analysis and descriptive statistics
- Matplotlib and Seaborn visualizations
- Sampling, probability and hypothesis-testing concepts
- Introductory data-science and API experiments

> The featured vehicle-rental dataset has only 12 sample rows. Its results demonstrate the workflow and should not be interpreted as statistically reliable market or pricing conclusions.

## Other learning areas

| Area | Topics |
|---|---|
| Python fundamentals | Variables, conditionals, loops, functions, strings, lists, dictionaries, sets and tuples |
| Object-oriented programming | Classes, constructors, inheritance, abstraction and polymorphism |
| Data structures & algorithms | Arrays, linked lists, stacks, queues, trees, recursion, searching, sorting and complexity |
| AI & API experiments | Prompt engineering and introductory API experiments |

## Repository structure

```text
01-python-fundamentals/
02-oop-and-python-concepts/
03-data-structures-and-algorithms/
04-data-science-and-analysis/
    README.md
    datasets/
    functions/
    notebooks/
    projects/
05-ai-and-api-experiments/
06-miscellaneous/
archive/
```

Historical and duplicate learning material is retained in topic folders or `archive/` rather than silently discarded.

## Getting started

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/deepaksambyal24-svg/codingninja_python.git
cd codingninja_python
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\\Scripts\\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Run an individual exercise with `python path/to/example.py`. Some historical scripts require course-specific input files or interactive terminal input; check the relevant project README before running them.

## Run the featured data-science project

Install its dependencies:

```bash
python -m pip install pandas matplotlib pytest
```

Run the analysis and tests:

```bash
python 04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/analysis.py
python -m pytest 04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/tests -v
```

## Quality and scope

- Project documentation identifies datasets and execution requirements.
- The featured project includes input validation and unit tests.
- Generated charts are written to a local outputs directory and are not committed.
- Learning scripts are being improved incrementally; their presence does not imply production readiness.

## Author

**Deepak Sambyal**

- GitHub: [@deepaksambyal24-svg](https://github.com/deepaksambyal24-svg)
