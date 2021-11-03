---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.7.3
latex_envs:
  LaTeX_envs_menu_present: true
  autoclose: false
  autocomplete: true
  bibliofile: biblio.bib
  cite_by: apalike
  current_citInitial: 1
  eqLabelWithNumbers: true
  eqNumInitial: 1
  hotkeys:
    equation: meta-9
  labels_anchors: false
  latex_user_defs: false
  report_style_numbering: false
  user_envs_cfg: false
toc:
  base_numbering: 1
  nav_menu: {}
  number_sections: true
  sideBar: true
  skip_h1_title: true
  title_cell: Table of Contents
  title_sidebar: Contents
  toc_cell: true
  toc_position:
    height: calc(100% - 180px)
    left: 10px
    top: 150px
    width: 226.364px
  toc_section_display: true
  toc_window_display: true
---

+++ {"toc": true}

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Importing-pandas-Library" data-toc-modified-id="Importing-pandas-Library-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Importing <code>pandas</code> Library</a></span></li><li><span><a href="#DataFrames-and-Series" data-toc-modified-id="DataFrames-and-Series-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>DataFrames and Series</a></span></li><li><span><a href="#Reading-a-CSV-File" data-toc-modified-id="Reading-a-CSV-File-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Reading a CSV File</a></span></li><li><span><a href="#Saving-to-a-CSV-File" data-toc-modified-id="Saving-to-a-CSV-File-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Saving to a CSV File</a></span></li><li><span><a href="#Quick-and-Easy-Summaries-of-a-DataFrame" data-toc-modified-id="Quick-and-Easy-Summaries-of-a-DataFrame-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Quick and Easy Summaries of a DataFrame</a></span><ul class="toc-item"><li><span><a href="#Summary-Statistics" data-toc-modified-id="Summary-Statistics-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Summary Statistics</a></span></li></ul></li><li><span><a href="#Working-with-DataFrame-Columns" data-toc-modified-id="Working-with-DataFrame-Columns-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Working with DataFrame Columns</a></span><ul class="toc-item"><li><span><a href="#Single-Columns" data-toc-modified-id="Single-Columns-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Single Columns</a></span></li><li><span><a href="#Multiple-Columns" data-toc-modified-id="Multiple-Columns-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Multiple Columns</a></span></li></ul></li><li><span><a href="#Plots" data-toc-modified-id="Plots-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Plots</a></span></li><li><span><a href="#Unique-Values-&amp;-Counting" data-toc-modified-id="Unique-Values-&amp;-Counting-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Unique Values &amp; Counting</a></span></li><li><span><a href="#Sorting" data-toc-modified-id="Sorting-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Sorting</a></span></li><li><span><a href="#Filtering" data-toc-modified-id="Filtering-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Filtering</a></span></li><li><span><a href="#Aggregation" data-toc-modified-id="Aggregation-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Aggregation</a></span></li><li><span><a href="#Setting-the-Index-of-a-DataFrame" data-toc-modified-id="Setting-the-Index-of-a-DataFrame-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Setting the Index of a DataFrame</a></span></li><li><span><a href="#Anatomy-of-a-DataFrame" data-toc-modified-id="Anatomy-of-a-DataFrame-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Anatomy of a DataFrame</a></span></li><li><span><a href="#Selection-Methods" data-toc-modified-id="Selection-Methods-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>Selection Methods</a></span><ul class="toc-item"><li><span><a href="#1.-Using-only-square-brackets" data-toc-modified-id="1.-Using-only-square-brackets-14.1"><span class="toc-item-num">14.1&nbsp;&nbsp;</span>1. Using only square brackets</a></span></li><li><span><a href="#2.-Positional-indexing-with-iloc" data-toc-modified-id="2.-Positional-indexing-with-iloc-14.2"><span class="toc-item-num">14.2&nbsp;&nbsp;</span>2. Positional indexing with <code>iloc</code></a></span></li><li><span><a href="#3.-Label-based-indexing-with-loc" data-toc-modified-id="3.-Label-based-indexing-with-loc-14.3"><span class="toc-item-num">14.3&nbsp;&nbsp;</span>3. Label-based indexing with <code>loc</code></a></span></li></ul></li></ul></div>

+++ {"slideshow": {"slide_type": "slide"}}

# Pandas Cheatsheet

### Importing `pandas` Library
```python
import pandas
```
> In general, it's good practice to collect all your `import` commands together and put them at the start of the notebook.

### DataFrames and Series

Data in `pandas` is organized into DataFrames and Series.

- **DataFrame:** 2-dimensional array, like a table in a spreadsheet
  - The rows are axis 0
  - The columns are axis 1
- **Series:** 1-dimensional array, like a single column or row in a spreadsheet
  - Each individual column or row of a DataFrame is represented as a Series

### Reading a CSV File

To read a CSV file and store it as a DataFrame variable:
```python
df = pandas.read_csv('some_cool_data.csv')
```

Missing data in a DataFrame or Series is represented as `NaN` ("not a number").

### Saving to a CSV File

To save a DataFrame to a CSV file: 
```python
df.to_csv('cool_output.csv', index=False)
```
- To include the DataFrame's index as a column in the CSV file, omit the `index=False` keyword argument.

+++ {"slideshow": {"slide_type": "slide"}}

### Quick and Easy Summaries of a DataFrame

|**feature** |dataframe attribute/method|
|---|---|
|**Useful Attributes** |
|Number of rows and columns (rows first, columns second) | `df.shape` |
|Names and data types of each column |  `df.dtypes` 
|Just the names of each column | `df.columns` 
|**Rows at a Glance** |
|First `n` rows (default 5) |`df.head(n)`
|Last `n` rows (default 5) | `df.tail(n)`
|A random sampling of `n` rows (default 1) | `df.sample(n)`

+++ {"slideshow": {"slide_type": "slide"}}

#### Summary Statistics

Full set of summary statistics (min, max, mean, standard deviation, etc.) for each numerical column of a DataFrame:
```python
df.describe()
```

Mean value of each column:
```python
df.mean()
```

And similarly for other summary statistics: `df.min()`, `df.max()`, `df.median()`, `df.std()`

+++ {"slideshow": {"slide_type": "slide"}}

### Working with DataFrame Columns

#### Single Columns

Each column of a DataFrame is a Series.
```python
series_X = df['X']
```

Most DataFrame methods can be applied to a Series, for example:
```python
df['X'].head()
df['X'].max()
```

Basic calculations with a Series and adding a new column to a DataFrame: 
```python
df['Double X'] = 2 * df['X']
```

#### Multiple Columns

Use a list of column names to select several columns of a DataFrame, in a specified order:
```python
df_subset = df[['E', 'A', 'C']]
```

+++ {"slideshow": {"slide_type": "slide"}}

### Plots

Create quick and easy plots of Series and DataFrames with the `plot` method, for example:
- Line plot of one column of a DataFrame:
```python
df['A'].plot()
```
- Line plot of column `'B'` vs. column `'A'` of a DataFrame:
```python
df.plot(x='A', y='B')
```
- Histogram of one column of a DataFrame:
```python
df['A'].plot(kind='hist', bins=30)
```
- Plot all columns of a DataFrame, with each column as a line on the same plot:
```python
df.plot()
```
- Plot bar charts of each column of a DataFrame, with a separate subplot for each column:
```python
df.plot(kind='bar', subplots=True)
```

Plots can be adjusted with keyword arguments such as `figsize`, `fontsize`, `title`, `colormap`. 
- To adjust the size of a graph, use the `figsize` keyword argument to the `plot` method, where `figsize` is a tuple of (width, height). For example to create 6" wide by 8" tall figure with subplots:
```python
df.plot(kind='bar', subplots=True, figsize=(6, 8))
```

+++ {"slideshow": {"slide_type": "slide"}}

### Unique Values & Counting

For a column `df['A']` which contains many repeated values (such as categories), some useful summary methods are:

|**feature**|method|
|---|---|
|Unique values | `df['A'].unique()`|
|Number of unique values | `df['A'].nunique()`|
|Counts of each unique value | `df['A'].value_counts()`|


> Note: The `unique`, `nunique`, and `value_counts` methods can only be applied to a Series (not a DataFrame)

+++ {"slideshow": {"slide_type": "slide"}}

### Sorting

Sorting a DataFrame based on the values in the column `'B'`:
```python
df.sort_values('B')
```
To sort in descending order, use the keyword argument `ascending=False`.

Sorting a Series:
```python
series_a.sort_values()
```

### Filtering

To select a subset of rows with a filter:
  - Create a filter (Boolean Series) using a comparison operator or other functions (such as the `isnull` method)
  - Use the filter to extract the desired rows from the DataFrame

Example: comparison operator
```python
warm = weather_data['Temperature (C)'] > 25
weather_warm = weather_data[warm]
```

You can also use Boolean Series and DataFrames to count occurrences of specified criteria, for example: count the missing values in each column of a DataFrame with `df.isnull().sum()`


### Aggregation

For basic aggregation operations, use the `groupby` method chained with an aggregation method (e.g., `sum`, `mean`, `sum`, `max`, etc.).

For example, to find the sum totals of column `'population'` grouped by column `'region'`: `
```python
world.groupby('region')['population'].sum()
```

You can also group by multiple columns:
```python
world.groupby(['region', 'income_group'])['population'].sum()
```

For more complex aggregations, you can use the `agg` method.
- Specify a list of aggregation statistics, for example: 
```python
world.groupby('region')['population'].agg(['sum', 'min', 'max'])
```
- Use a dictionary to specify different aggregation statistics for different columns, for example:

```python
agg_dict = {'population' : 'sum', 
            'life_expectancy' : ['min', 'max']}
world.groupby('region').agg(agg_dict)
```

+++ {"slideshow": {"slide_type": "slide"}}

---
### Setting the Index of a DataFrame

The index of a DataFrame can be set with the `set_index` method. For example, to set the column `'country'` as the index of DataFrame `world` and save the output as a new DataFrame:
```python
world_new = world.set_index('country')
```

### Anatomy of a DataFrame

![dataframe3](img/dataframe3.png)

- Each cell in a DataFrame is associated with:
  - A row position and column position (integers, starting from 0), and
  - A row label and column label
- Row and column labels are part of the DataFrame's metadata, stored in attributes:
  - `df.index` contains the labels for the DataFrame's rows
  - `df.columns` contains the labels for the DataFrame's columns
- `df.values` contains the underlying data array

### Selection Methods

There are three main ways of selecting subsets of a DataFrame (or Series):
<ol>
    <li>Using only square brackets `[]`</li>
    <li>Positional indexing with `.iloc[]`</li>
    <li>Label-based indexing with `.loc[]`</li>
</ol>


#### 1. Using only square brackets
|||
---|----
Use a Boolean Series to select rows matching some criteria | `df[bool_series]`
Use a list of column names to select several columns in a specified order | `df[['E', 'A', 'C']]`
Select a single column (as a Series) | `series_A = df['A']`
Select a single column (as a DataFrame) | `df_A = df[['A']]`


#### 2. Positional indexing with `iloc`

With `iloc`, we specify the row selection first, followed by column selection, separated by a comma. For example, selecting a single cell at row 2, column 4:
```python
df.iloc[2, 4]
```

With `iloc` can select:
- A single cell
- A single row or column
- Slices of rows and/or columns
  - As with Python lists, `iloc` slices are inclusive of the start bound and exclusive of the stop bound
- Multiple rows and/or columns in arbitrary order, using a list of positions

A few examples:
```python
df.iloc[100:201:2, [5, 2, 4]]
df.iloc[[4, 2], 3:7]
df.iloc[175:, :]
```


#### 3. Label-based indexing with `loc`

As with `iloc`, we specify the row selection first, followed by column selection, separated by a comma, but using the row and column labels instead of their positions. For example, selecting a single cell at a row labelled `'Algeria'` and a column labelled `'life_expectancy'`:
```python
world_new.loc['Algeria', 'life_expectancy']
```

Similar to `iloc`, with `loc` we can select:
- A single cell
- A single row or column
- Slices of rows and/or columns
  - However, unlike `iloc` and Python list slicing, `loc` slices are inclusive of the start bound but also **inclusive** of the stop bound.
  - Example:
```python
world_new.loc['Canada':'Denmark', 'income_group':'gdp_per_capita']
```
- Multiple rows and/or columns in arbitrary order, using a list of labels

We can also select rows and/or columns with a Boolean Series, and mix and match these with the other selection options listed above, for example:
```python
densely_populated = world_new['pop_density'] > 500
world_new.loc[densely_populated, ['region', 'pop_density', 'population']]
```
