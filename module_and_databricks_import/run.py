# Databricks notebook source
# MAGIC %run "./lib"

# COMMAND ----------

if "lib" not in globals():
    from module_and_databricks_import.lib import *

a = lib.some_lib_function(1, 2, 3, "module", "databricks")
b = lib.some_namespace_class()

