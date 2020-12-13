# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['get_added', 'get_removed', 'get_modified', 'get_delta', 'log_delta']

# Cell
import pandas as pd
import numpy as np

# Cell
def get_added(df_old, df_new, unique_id, trans_col="transaction", trans_vaL="added"):
    """get rows in df_new which are not in df_old

    Parameters
    ----------
        df_old : pd.DataFrame
            dataframe with previous information
        df_new: pd.DataFrame
            dataframe with new information
        unique_id: str or list
            unique identifier(s)
        trans_col: str
            name of column to track transaction
        trans_val: str
            name of value to reflect transaction status "added"

    Returns
    -------
    pd.DataFrame
        dataframe that contains added rows
    """
    cols = list(df_old.columns)
    new_rows = (pd
                .merge(df_old, df_new, how="outer", on=unique_id, indicator=True, suffixes=("_foo",""))
                .query('_merge == "right_only"')
                )
    new_rows = new_rows[cols]
    new_rows[trans_col] = trans_vaL
    return new_rows

# Cell
def get_removed(df_old, df_new, unique_id, trans_col="transaction", trans_val="removed"):
    """Returns the removed rows that are not any longer in df_new"""
    cols = list(df_old.columns)
    removed_rows = (pd
                .merge(df_new, df_old, how="outer", on=unique_id, indicator=True, suffixes=("_foo",""))
                .query('_merge == "right_only"')
                )
    removed_rows = removed_rows[cols]
    removed_rows[trans_col] = trans_val
    return removed_rows

# Cell
def get_modified(df_old, df_new, unique_id, added_rows=None, trans_col="transaction", trans_val="modified"):
    """Returns the modified rows in df_new"""
    cols = list(df_new.columns)
    if added_rows is not None:
        df_new = df_new[~df_new.isin(list(added_rows[unique_id].values))].dropna()
    modified_rows = df_old.merge(df_new, indicator=True, how='outer')
    modified_rows = modified_rows[modified_rows['_merge'] == 'right_only']
    modified_rows = modified_rows[cols]
    modified_rows[trans_col] = trans_val
    return modified_rows

# Cell
def get_delta(df_old, df_new, unique_id, sort_by=None, trans_col="transaction", trans_val_added="added", trans_val_removed="removed", trans_val_modified="modified"):
    added_rows = get_added(df_old=df_old, df_new=df_new, unique_id="id",trans_col=trans_col, trans_vaL=trans_val_added)
    removed_rows = get_removed(df_old=df_old, df_new=df_new, unique_id="id", trans_col=trans_col, trans_val=trans_val_removed)
    modified_rows = get_modified(df_old=df_old, df_new=df_new, unique_id="id", added_rows=added_rows, trans_col=trans_col, trans_val=trans_val_modified)
    df = added_rows.append([removed_rows, modified_rows])
    if sort_by:
        df = df.sort_values(by=sort_by)
    return df

# Cell
def log_delta(df_log, df_old, df_new, unique_id, trans_col="transaction", trans_val_added="added", trans_val_removed="removed", trans_val_modified="modified", sort_by=None):
    if df_log is None:
        df_log = df_old#.copy()
        df_log[trans_col] = trans_val_added
    else:
        subset = list(df_log.columns)
        subset.remove(trans_col)
        added_rows = get_added(df_old=df_old, df_new=df_new, unique_id=unique_id, trans_col=trans_col, trans_vaL=trans_val_added)
        removed_rows = get_removed(df_old=df_old, df_new=df_new, unique_id=unique_id, trans_col=trans_col, trans_val=trans_val_removed)
        modified_rows = get_modified(df_new=df_new, df_old=df_old, unique_id=unique_id, added_rows=added_rows, trans_col=trans_col, trans_val=trans_val_modified)
        df_log = df_log.append(modified_rows, ignore_index=True)
        df_log = df_log.drop_duplicates(subset=subset, keep="first")
        df_log = df_log.append(added_rows, ignore_index=True)
        df_log = df_log.append(removed_rows, ignore_index=True)
    if sort_by:
        df_log = df_log.sort_values(by=sort_by)
    return df_log