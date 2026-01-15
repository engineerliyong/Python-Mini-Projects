---

# CSV Data Analyzer 📊

**Project 03** of 30 Python Mini Projects

A Python command-line tool that loads, cleans, and analyzes CSV data using **pandas**, with a focus on handling missing values and generating meaningful statistical summaries.

This project simulates a **real-world employee dataset**, making it a strong foundation for data analysis, data science, and AI workflows.

---

## Features

* ✅ **CSV File Loading** – Reads CSV files into pandas DataFrames
* ✅ **Dataset Overview** – Displays number of rows and columns
* ✅ **Column Data Types** – Shows data types for each column
* ✅ **Data Preview** – Displays the first 5 rows of the dataset
* ✅ **Missing Value Detection** – Identifies missing values per column
* ✅ **Automatic Data Cleaning**

  * Numeric columns filled with column mean
  * Categorical columns filled with `"Unknown"`
* ✅ **Statistical Analysis**

  * Count, mean, min, max, and standard deviation
* ✅ **Column-Specific Analysis** – Calculates salary statistics
* ✅ **Error Handling** – Gracefully handles file loading errors

---

## Dataset Description

The dataset represents employee information across multiple departments.

### Columns

| Column             | Description              |
| ------------------ | ------------------------ |
| `name`             | Employee name            |
| `age`              | Employee age             |
| `salary`           | Annual salary            |
| `department`       | Department name          |
| `years_experience` | Years of work experience |

### Sample Data

```csv
name,age,salary,department,years_experience
Alice,28,65000,Engineering,5
Bob,35,75000,Marketing,8
Frank,38,,Engineering,12
Iris,,71000,Marketing,9
```

---

## Installation

### Prerequisites

* Python 3.7 or higher

### Dependencies

```bash
pip install pandas
```

### Setup

```bash
# Clone the repository
git clone https://github.com/engineerliyong/python-mini-projects.git

# Navigate to this project
cd python-mini-projects/project-03-csv-data-analyzer
```

---

## Usage

### Basic Usage

```bash
python analyzer.py
```

⚠️ Ensure your CSV file is named:

```text
sample_data.csv
```

or update this line in the code:

```python
file_path = "sample_data.csv"
```

---

## Example Output

```
CSV file 'sample_data.csv' loaded successfully.

BASIC DATASET INFORMATION
------------------------------
Number of rows: 14
Number of columns: 5

Column Data Types
name                 object
age                 float64
salary              float64
department            object
years_experience      int64

First 5 rows of the dataset
      name   age   salary   department  years_experience
0    Alice  28.0  65000.0  Engineering                 5
1      Bob  35.0  75000.0    Marketing                 8
2  Charlie  42.0  95000.0  Engineering                15
3    Diana  29.0  68000.0        Sales                 6
4      Eve  31.0  72000.0    Marketing                 7

CLEANING DATA
------------------------------
Missing values before cleaning:
age        1
salary     1

Missing values after cleaning:
age        0
salary     0

DATA ANALYSIS
------------------------------
```

---

## Code Structure

### Functions

### `load_csv(file_path)`

* Loads CSV file into a pandas DataFrame
* Handles file-related errors
* **Parameters**: `file_path` (str)
* **Returns**: `DataFrame` or `None`

---

### `show_basic_info(df)`

* Displays dataset size
* Shows column data types
* Prints first 5 rows
* **Parameters**: `df` (DataFrame)

---

### `clean_data(df)`

* Detects missing values
* Fills:

  * Numeric columns → mean
  * Categorical columns → `"Unknown"`
* **Parameters**: `df` (DataFrame)
* **Returns**: cleaned `DataFrame`

---

### `analyze_data(df)`

* Displays statistical summary using `df.describe()`
* Performs salary analysis (mean, min, max)
* **Parameters**: `df` (DataFrame)

---

## Data Flow

```
1. CSV file path defined
   ↓
2. load_csv() loads file into DataFrame
   ↓
3. show_basic_info() inspects dataset
   ↓
4. clean_data() handles missing values
   ↓
5. analyze_data() generates statistics
```

---

## What I Learned

### 1. **pandas DataFrames**

```python
df = pd.read_csv(file_path)
```

* Core structure for tabular data
* Enables fast and flexible data analysis

---

### 2. **Handling Missing Values**

```python
df.fillna(df.mean())
```

* Missing data is common in real datasets
* Numeric and categorical data require different strategies

---

### 3. **Selecting Data by Type**

```python
df.select_dtypes(include="number")
```

* Prevents applying numeric operations to text columns
* Makes code safer and more robust

---

### 4. **Exploratory Data Analysis (EDA)**

```python
df.describe()
```

* Quickly summarizes key statistics
* Essential first step in any data project

---

## Challenges & Solutions

### Challenge 1: Missing Salary Values

**Problem**: NaN values caused incorrect statistics

**Solution**:

```python
df[numeric_columns.columns] = numeric_columns.fillna(numeric_columns.mean())
```

---

### Challenge 2: Mixed Column Types

**Problem**: Statistical methods failed on non-numeric columns

**Solution**:

```python
df.select_dtypes(include="number")
```

---

### Challenge 3: Code Readability

**Problem**: Main logic became cluttered

**Solution**:

* Broke code into clear, single-responsibility functions
* Improved maintainability and clarity

---

## Testing

### Test Cases

```
✅ Valid CSV file – Passed
✅ Missing salary values – Filled correctly
✅ Missing age values – Filled correctly
✅ Multiple departments – Handled correctly
✅ No file found – Error handled
```

---

## Future Improvements

### Version 2.0

* [ ] Save cleaned data to a new CSV file
* [ ] Command-line arguments for file path
* [ ] Data visualizations (histograms, bar charts)

### Version 3.0

* [ ] Group-by analysis (salary by department)
* [ ] Correlation analysis
* [ ] Automated insights generation

### Version 4.0

* [ ] GUI with Tkinter
* [ ] Web interface with Flask
* [ ] Integration with AI-powered analytics

---

## Project Statistics

| Metric               | Value           |
| -------------------- | --------------- |
| **Lines of Code**    | ~110            |
| **Functions**        | 4               |
| **Time to Complete** | ~2 hours        |
| **Difficulty**       | ⭐⭐ Intermediate |
| **Date Completed**   | January 2026    |

---

## Reflection

### What I’m Proud Of

* Clean and modular code
* Proper handling of missing data
* Using pandas effectively
* Realistic dataset design
* Strong foundation for future data projects

### Key Takeaways

1. **Data cleaning is essential**
2. **pandas simplifies complex analysis**
3. **EDA should always come first**
4. **Readable code scales better**
5. **Small projects build real skills**

---

**Part of:** [30 Python Mini Projects](https://github.com/engineerliyong/python-mini-projects)
**Author:** Liza Bambu
**Date:** January 2026
**Status:** ✅ Complete
**Next:** Project 04 – Data Visualization Dashboard

---

*From raw CSVs to real insights* 📈🚀

---
