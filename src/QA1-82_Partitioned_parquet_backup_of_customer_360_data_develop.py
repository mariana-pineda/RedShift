from pyspark.sql.functions import col, current_timestamp, expr

# Define schema for the customer_360_raw table if necessary, based on requirement
# Assuming the schema is already known from the database definition.

# Backup the customer_360_raw table as compressed parquet files, partitioned by state
customer_360_raw_df = spark.table("agilisium_playground.purgo_playground.customer_360_raw")

# Validate the DataFrame content
if not customer_360_raw_df.rdd.isEmpty():
    # Writing the DataFrame to Parquet, partitioned by 'state' with compression
    customer_360_raw_df.write.mode("overwrite") \
        .partitionBy("state") \
        .parquet("/Volumes/agilisium_playground/purgo_playground/customer_360_raw_backup", compression="snappy")

    # Data Cleanup: Delete records older than 30 days based on 'last_updated' column
    # Using a placeholder column 'last_updated', which should exist in the data
    spark.sql("""
        DELETE FROM agilisium_playground.purgo_playground.customer_360_raw
        WHERE last_updated < current_timestamp() - INTERVAL 30 DAYS
    """)

    # Optimize and Clean up the table using VACUUM to remove old files, retaining data for 30 days (720 hours)
    spark.sql("VACUUM agilisium_playground.purgo_playground.customer_360_raw RETAIN 720 HOURS")
else:
    # Log a message or handle the scenario where no data is available for backup
    print("No data available in customer_360_raw table for backup operation.")

