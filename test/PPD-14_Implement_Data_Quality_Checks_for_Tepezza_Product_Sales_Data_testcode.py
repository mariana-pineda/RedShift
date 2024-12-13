from pyspark.sql.functions import col, isnan, when, count, date_format, to_date

# Validate completeness: Check for missing fields
completeness_check = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
completeness_check.show()

# Validate accuracy: Check data types and formats
accuracy_check = df.withColumn("quantity_check", col("quantity").cast("int").isNotNull()) \
    .withColumn("price_check", col("price").cast("float").isNotNull()) \
    .withColumn("sale_date_check", to_date(col("sale_date"), "yyyy-MM-dd").isNotNull())

accuracy_check.select("sales_id", "quantity_check", "price_check", "sale_date_check").show()

# Validate consistency: Check business rules
consistency_check = df.withColumn("positive_quantity", col("quantity") > 0) \
    .withColumn("positive_price", col("price") > 0)

consistency_check.select("sales_id", "positive_quantity", "positive_price").show()

# Handle records failing data quality checks
failed_records = df.filter(
    col("quantity").isNull() | col("price").isNull() | col("sale_date").isNull() |
    col("quantity").cast("int").isNull() | col("price").cast("float").isNull() |
    to_date(col("sale_date"), "yyyy-MM-dd").isNull() |
    (col("quantity") <= 0) | (col("price") <= 0)
)

failed_records.show()

# Logging and alerting for data quality issues
failed_records_count = failed_records.count()
if failed_records_count > 0:
    print(f"Data quality issues detected: {failed_records_count} records failed checks.")
    # Here you would typically log the issues and send alerts

# Updating data quality rules
# This would involve reloading the rules and re-running the checks, which is not shown here
