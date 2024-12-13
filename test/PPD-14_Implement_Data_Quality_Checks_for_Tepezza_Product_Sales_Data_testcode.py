from pyspark.sql.functions import col, isnan, when, count, date_format, to_date

# Validate completeness: Check for missing fields
completeness_checks = df.select(
    [count(when(col(c).isNull() | isnan(c), c)).alias(c) for c in df.columns]
)
completeness_checks.show()

# Validate accuracy: Check for correct data types and formats
accuracy_checks = df.withColumn("quantity_check", col("quantity").cast("int").isNotNull()) \
    .withColumn("price_check", col("price").cast("float").isNotNull()) \
    .withColumn("sale_date_check", to_date(col("sale_date"), "yyyy-MM-dd").isNotNull())

accuracy_checks.select("sales_id", "quantity_check", "price_check", "sale_date_check").show()

# Validate consistency: Check for business rule adherence
consistency_checks = df.withColumn("positive_quantity", col("quantity") > 0) \
    .withColumn("positive_price", col("price") > 0)

consistency_checks.select("sales_id", "positive_quantity", "positive_price").show()

# Flag records failing data quality checks
failed_records = df.filter(
    col("quantity").isNull() | col("price").isNull() | col("sale_date").isNull() |
    col("quantity").cast("int").isNull() | col("price").cast("float").isNull() |
    to_date(col("sale_date"), "yyyy-MM-dd").isNull() |
    (col("quantity") <= 0) | (col("price") <= 0)
)
failed_records.show()

# Log and alert for data quality issues
failed_records_count = failed_records.count()
if failed_records_count > 0:
    print(f"Data quality issues detected: {failed_records_count} records failed checks.")
    # Here you would implement logging and alerting mechanisms

# Update data quality rules
# This part would involve reloading or modifying the rules and re-running the checks
# For demonstration, assume rules are updated and checks are re-executed
# Re-run the checks after updating rules
