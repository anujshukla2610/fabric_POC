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

# CELL ********************

product_data = [
    ("P001", "Laptop", "Electronics", 65000),
    ("P002", "Monitor", "Electronics", 18000),
    ("P003", "Keyboard", "Accessories", 2500),
    ("P004", "Mouse", "Accessories", 1200),
    ("P005", "Printer", "Electronics", 15000),
    ("P006", "Headphones", "Accessories", 4500),
    ("P007", "Mobile", "Electronics", 35000),
    ("P008", "Tablet", "Electronics", 28000)
]

product_df = spark.createDataFrame(
    product_data,
    [
        "product_id",
        "product_name",
        "category",
        "unit_price"
    ]
)

product_df.write.mode("overwrite").format("delta").saveAsTable("dim_product")

display(spark.table("dim_product"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

sales_data = [
    (1001, "C001", "P001", "2026-09-01", 2, 65000, 130000, "Bhopal"),
    (1002, "C002", "P003", "2026-09-01", 5, 2500, 12500, "Indore"),
    (1003, "C003", "P007", "2026-09-02", 3, 35000, 105000, "Pune"),
    (1004, "C004", "P002", "2026-09-02", 4, 18000, 72000, "Mumbai"),
    (1005, "C005", "P005", "2026-09-03", 2, 15000, 30000, "Ahmedabad"),
    (1006, "C006", "P004", "2026-09-03", 10, 1200, 12000, "Surat"),
    (1007, "C007", "P001", "2026-09-04", 1, 65000, 65000, "Delhi"),
    (1008, "C008", "P008", "2026-09-04", 2, 28000, 56000, "Lucknow"),
    (1009, "C009", "P006", "2026-09-05", 4, 4500, 18000, "Kanpur"),
    (1010, "C010", "P007", "2026-09-05", 2, 35000, 70000, "Bengaluru"),
    (1011, "C001", "P002", "2026-09-06", 3, 18000, 54000, "Bhopal"),
    (1012, "C003", "P003", "2026-09-06", 8, 2500, 20000, "Pune"),
    (1013, "C005", "P001", "2026-09-07", 2, 65000, 130000, "Ahmedabad"),
    (1014, "C006", "P006", "2026-09-07", 5, 4500, 22500, "Surat"),
    (1015, "C007", "P005", "2026-09-08", 3, 15000, 45000, "Delhi"),
    (1016, "C008", "P004", "2026-09-08", 7, 1200, 8400, "Lucknow"),
    (1017, "C009", "P007", "2026-09-09", 1, 35000, 35000, "Kanpur"),
    (1018, "C010", "P008", "2026-09-09", 3, 28000, 84000, "Bengaluru"),
    (1019, "C002", "P001", "2026-09-10", 1, 65000, 65000, "Indore"),
    (1020, "C004", "P006", "2026-09-10", 6, 4500, 27000, "Mumbai")
]

sales_df = spark.createDataFrame(
    sales_data,
    [
        "sale_id",
        "customer_id",
        "product_id",
        "sale_date",
        "quantity",
        "unit_price",
        "amount",
        "plant_name"
    ]
)

sales_df = (
    sales_df
    .withColumn("sale_date", F.to_date("sale_date"))
    .withColumn("inserted_dttm", F.current_timestamp())
)

sales_df.write.mode("overwrite").format("delta").saveAsTable("fact_sales")

display(spark.table("fact_sales"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
