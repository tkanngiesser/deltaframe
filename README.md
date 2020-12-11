# Deltaframe
> Delta between two or more Pandas dataframes.


This file will become your README and also the index of your documentation.

## Install

`pip install deltaframe`

## How to use deltaframe

First, lets create two dataframes (one from the previous day, one from the current day) - items have been 
- added
- removed and
- modified

```
df1=pd.DataFrame({
    'date':['2013-11-24','2013-11-24','2013-11-24','2013-11-24'],
    'id':['001','002','003','004'],
    'quantity':[22,8,7,10],
    'color':['Yellow','Orange','Red','Yellow'],
})
df2=pd.DataFrame({
    'date':['2013-11-24','2013-11-25','2013-11-24','2013-11-24'],
    'id':['001','002', '004', '005'],
    'quantity':[22,6,5,10],
    'color':['Yellow','Orange','Red','Pink'],
})
```

```
df1
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
df2
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



First look at entries that were added (in df2 but not in df1)

```
added_entries = get_added_entries(df_old=df1, df_new=df2, unique_id="id")
added_entries
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



What about removed entries (in df1 but not any longer in df2)

```
removed_entries = get_removed_entries(df_old=df1, df_new=df2, unique_id="id")
removed_entries
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



Awesome, finally we check for the modified entries (initially not considering new items)

```
modified_entries = get_modified_entries(df_old=df1, df_new=df2, unique_id="id")
modified_entries
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
  </tbody>
</table>
</div>


