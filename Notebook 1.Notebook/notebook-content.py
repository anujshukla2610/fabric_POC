# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "56967144-ff7c-43ac-b687-535d7078d321",
# META       "default_lakehouse_name": "lh",
# META       "default_lakehouse_workspace_id": "092db2e9-3190-4705-83a3-7c56a9884c12",
# META       "known_lakehouses": [
# META         {
# META           "id": "56967144-ff7c-43ac-b687-535d7078d321"
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

from pyspark.sql import functions as F

customer_data = [
    ("C001", "Rahul Sharma", "Bhopal", "Madhya Pradesh", "Retail"),
    ("C002", "Amit Verma", "Indore", "Madhya Pradesh", "Retail"),
    ("C003", "Priya Singh", "Pune", "Maharashtra", "Corporate"),
    ("C004", "Neha Gupta", "Mumbai", "Maharashtra", "Retail"),
    ("C005", "Arjun Patel", "Ahmedabad", "Gujarat", "Corporate"),
    ("C006", "Sneha Mehta", "Surat", "Gujarat", "Retail"),
    ("C007", "Rohit Jain", "Delhi", "Delhi", "Corporate"),
    ("C008", "Pooja Yadav", "Lucknow", "Uttar Pradesh", "Retail"),
    ("C009", "Karan Mishra", "Kanpur", "Uttar Pradesh", "Corporate"),
    ("C010", "Anjali Rao", "Bengaluru", "Karnataka", "Retail")
]

customer_df = spark.createDataFrame(
    customer_data,
    [
        "customer_id",
        "customer_name",
        "city",
        "state",
        "customer_type"
    ]
)

customer_df.write.mode("overwrite").format("delta").saveAsTable("dim_customer")

display(spark.table("dim_customer"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
