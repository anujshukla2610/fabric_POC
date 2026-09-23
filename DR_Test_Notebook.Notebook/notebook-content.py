# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ed1a9a92-8862-4947-91c0-bb87a0ae3a00",
# META       "default_lakehouse_name": "DRPOCLakehouse",
# META       "default_lakehouse_workspace_id": "092db2e9-3190-4705-83a3-7c56a9884c12",
# META       "known_lakehouses": [
# META         {
# META           "id": "ed1a9a92-8862-4947-91c0-bb87a0ae3a00"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * from dim_customer

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
