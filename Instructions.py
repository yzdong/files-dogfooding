# Databricks notebook source
# MAGIC %md # Instructions

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Part 1: Developing shareable Python code
# MAGIC You are a data scientist who has just joined a team. Your team works on analyzing wine quality. You noticed that your team members have been copying and pasting Python utility functions across their individual notebook. Your task is to create a shared library that can be used across different notebooks
# MAGIC 
# MAGIC In this repo, you'll find 2 of your coworkers' code, Abby and Zach. Find a way to refactor out shared code such that both their notebooks run. 
# MAGIC 
# MAGIC Start by creating a new file in the file navigator called "utils.py"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Part 2: Working with small datasets within a repo 
# MAGIC 
# MAGIC Your new Python module was well-received by your team and used on other data-sets. However, the quality of the new datasets are low and you see the need to develop a data-cleaning function. 
# MAGIC 
# MAGIC In your new Python module, create a new function clean_data that can handle the dirty data from this [test dataset](https://docs.google.com/spreadsheets/d/1D4lp8uA4c3ezKR25Zp5dp5YEmVU0VbbyKAOjipnwIIA/edit#gid=0)
# MAGIC 
# MAGIC Data cleaning rules:
# MAGIC 1. All values should be numerical
# MAGIC 2. Any row without data should be discarded
# MAGIC 3. pH should be between 0 and 14
# MAGIC 4. Quality should be between 0 and 10
# MAGIC 
# MAGIC You should start by downloading the data and putting it into the repo

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Part 3: Unit testing
# MAGIC 
# MAGIC Your utils.py library works well. However, your team is starting to make changes to it and sometimes breaks the functionality of that module. You'd like to develop unit tests for this library.
# MAGIC 
# MAGIC Start by creating a notebook called "utils_test" that invokes the utils.py library. Write unit tests that test the util functions in utils.py. If this notebook runs without failures, then the unit tests for utils.py passes.

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ## Extension-- CI/CD
# MAGIC 
# MAGIC Your unit tests works well. However, you find that your team isn't as diligent about running the utils_test notebook before merging. Using an external CI/CD provider (like Jenkins or Github actions), [run unit tests on commit](https://docs.databricks.com/repos.html#set-up-git-automation-to-update-repos-on-merge) by calling the [repos API](https://docs.databricks.com/dev-tools/api/latest/repos.html) and then the jobs API.

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ## Extension-- refactor our existing ML end-to-end example 
# MAGIC 
# MAGIC Refactor our existing [end-to-end example](https://docs.databricks.com/_static/notebooks/mlflow/mlflow-end-to-end-example-aws.html) and add unit tests
