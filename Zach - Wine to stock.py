# Databricks notebook source
import pandas as pd

# Load wine data
data = pd.read_csv("/dbfs/databricks-datasets/wine-quality/winequality-red.csv", sep=";")

# Remove spaces from column names
data.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

# COMMAND ----------

# Wines with free_sulfur_dioxide less than 15 can be labelled as no added sulfur

no_added_sulfur = (data["free_sulfur_dioxide"] <= 15).astype(int)
data["no_added_sulfur"] = no_added_sulfur

# COMMAND ----------

# Wines with residual_sugar less than 2 is considered brut

is_brut = (data["residual_sugar"] <= 2).astype(int)
data["brut"] = is_brut
