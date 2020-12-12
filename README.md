# Deltaframe
> Build the delta between two Pandas dataframes.


## Install

`pip install deltaframe`

## How to use deltaframe

First, lets create two dataframes (e.g. transaction date from consecutive days). 

```
df_old = pd.DataFrame({
    'date':['2013-11-24','2013-11-24','2013-11-24','2013-11-24'],
    'id':['001','002','003','004'],
    'quantity':[22,8,7,10],
    'color':['Yellow','Orange','Red','Yellow'],
})
df_new = pd.DataFrame({
    'date':['2013-11-24','2013-11-25','2013-11-24','2013-11-24'],
    'id':['001','002', '004', '005'],
    'quantity':[22,6,5,10],
    'color':['Yellow','Orange','Red','Pink'],
})
```

```
df_old
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-11-24</td>
      <td>001</td>
      <td>22</td>
      <td>Yellow</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-11-24</td>
      <td>002</td>
      <td>8</td>
      <td>Orange</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>10</td>
      <td>Yellow</td>
    </tr>
  </tbody>
</table>
</div>



```
df_new
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-11-24</td>
      <td>001</td>
      <td>22</td>
      <td>Yellow</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-11-25</td>
      <td>002</td>
      <td>6</td>
      <td>Orange</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>5</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-11-24</td>
      <td>005</td>
      <td>10</td>
      <td>Pink</td>
    </tr>
  </tbody>
</table>
</div>



Let's look at the main function `show_delta`first.

```
show_delta(df_old=df_old, df_new=df_new, unique_id="id", sort_by="date")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-7a7f960399f2> in <module>
    ----> 1 show_delta(df_old=df_old, df_new=df_new, unique_id="id", sort_by="date")
    

    NameError: name 'show_delta' is not defined


First look at entries that were added in df_new.

```
added_rows = get_added_rows(df_old=df_old, df_new=df_new, unique_id="id")
added_rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2013-11-24</td>
      <td>005</td>
      <td>10.0</td>
      <td>Pink</td>
      <td>added</td>
    </tr>
  </tbody>
</table>
</div>



What about removed rows (in df_old but not any longer in df_new) ?

```
removed_rows = get_removed_rows(df_old=df_old, df_new=df_new, unique_id="id")
removed_rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7.0</td>
      <td>Red</td>
      <td>removed</td>
    </tr>
  </tbody>
</table>
</div>



Awesome, finally we check for the modified rows (also showing added rows).

```
modified_rows = get_modified_rows(df_old=df_old, df_new=df_new, unique_id="id")
modified_rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2013-11-25</td>
      <td>002</td>
      <td>6</td>
      <td>Orange</td>
      <td>modified</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>5</td>
      <td>Red</td>
      <td>modified</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2013-11-24</td>
      <td>005</td>
      <td>10</td>
      <td>Pink</td>
      <td>modified</td>
    </tr>
  </tbody>
</table>
</div>



If we don't want to show added rows as modified, we can pass the added_rows dataframe created above.

```
modified_rows = get_modified_rows(df_old=df_old, df_new=df_new, unique_id="id", added_rows=added_rows)
modified_rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2013-11-25</td>
      <td>002</td>
      <td>6</td>
      <td>Orange</td>
      <td>modified</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>5</td>
      <td>Red</td>
      <td>modified</td>
    </tr>
  </tbody>
</table>
</div>



Finally, let's build a logging file to document when a row been added, modified or deleted.

Initially there is no log file so we set `df_log=None`.

```
df_log = logging(df_log=None, df_old=df_old, df_new=df_new, unique_id="id")
df_log
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-11-24</td>
      <td>001</td>
      <td>22</td>
      <td>Yellow</td>
      <td>added</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-11-24</td>
      <td>002</td>
      <td>8</td>
      <td>Orange</td>
      <td>added</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7</td>
      <td>Red</td>
      <td>added</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>10</td>
      <td>Yellow</td>
      <td>added</td>
    </tr>
  </tbody>
</table>
</div>



When there's an existing log file we happily pass it to our logging function...

```
df_log = logging(df_log=df_log, df_old=df_old, df_new=df_new, unique_id="id")
df_log
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-11-24</td>
      <td>001</td>
      <td>22.0</td>
      <td>Yellow</td>
      <td>added</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-11-24</td>
      <td>002</td>
      <td>8.0</td>
      <td>Orange</td>
      <td>added</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7.0</td>
      <td>Red</td>
      <td>added</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>10.0</td>
      <td>Yellow</td>
      <td>added</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013-11-25</td>
      <td>002</td>
      <td>6.0</td>
      <td>Orange</td>
      <td>modified</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>5.0</td>
      <td>Red</td>
      <td>modified</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2013-11-24</td>
      <td>005</td>
      <td>10.0</td>
      <td>Pink</td>
      <td>added</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7.0</td>
      <td>Red</td>
      <td>removed</td>
    </tr>
  </tbody>
</table>
</div>



Finally, if we want to sort our log file by a particular column.

```
df_log = logging(df_log=df_log, df_old=df_old, df_new=df_new, unique_id="id", sort_by=["date"])
df_log
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>id</th>
      <th>quantity</th>
      <th>color</th>
      <th>transaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-11-24</td>
      <td>001</td>
      <td>22.0</td>
      <td>Yellow</td>
      <td>added</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-11-24</td>
      <td>002</td>
      <td>8.0</td>
      <td>Orange</td>
      <td>added</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7.0</td>
      <td>Red</td>
      <td>added</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>10.0</td>
      <td>Yellow</td>
      <td>added</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2013-11-24</td>
      <td>004</td>
      <td>5.0</td>
      <td>Red</td>
      <td>modified</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2013-11-24</td>
      <td>005</td>
      <td>10.0</td>
      <td>Pink</td>
      <td>added</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2013-11-24</td>
      <td>005</td>
      <td>10.0</td>
      <td>Pink</td>
      <td>added</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2013-11-24</td>
      <td>003</td>
      <td>7.0</td>
      <td>Red</td>
      <td>removed</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013-11-25</td>
      <td>002</td>
      <td>6.0</td>
      <td>Orange</td>
      <td>modified</td>
    </tr>
  </tbody>
</table>
</div>


