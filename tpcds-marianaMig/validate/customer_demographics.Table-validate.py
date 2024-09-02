import sys
import os
from sqlalchemy import create_engine
from databricks import sql

redshiftHost = os.getenv("PURGO_REDSHIFT_HOST")
if not redshiftHost:
    sys.exit("PURGO_REDSHIFT_HOST env variable not set")

redshiftPort = os.getenv("PURGO_REDSHIFT_PORT")
if not redshiftPort:
    sys.exit("PURGO_REDSHIFT_PORT env variable not set")

redshiftDB = os.getenv("PURGO_REDSHIFT_DB")
if not redshiftDB:
    sys.exit("PURGO_REDSHIFT_DB env variable not set")

redshiftUser = os.getenv("PURGO_REDSHIFT_USER")
if not redshiftUser:
    sys.exit("PURGO_REDSHIFT_USER env variable not set")

redshiftPassword = os.getenv("PURGO_REDSHIFT_PASSWORD")
if not redshiftPassword:
    sys.exit("PURGO_REDSHIFT_PASSWORD env variable not set")

databricksToken = os.getenv("PURGO_DATABRICKS_TOKEN")
if not databricksToken:
	sys.exit("PURGO_DATABRICKS_TOKEN env variable not set")
	
databricksHost = os.getenv("PURGO_DATABRICKS_HOST")
if not databricksHost:
	sys.exit("PURGO_DATABRICKS_HOST env variable not set")

databricksPort = os.getenv("PURGO_DATABRICKS_PORT")
if not databricksPort:
	sys.exit("PURGO_DATABRICKS_PORT env variable not set")
	
databricksHttpPath = os.getenv("PURGO_DATABRICKS_HTTP_PATH")
if not databricksHttpPath:
	sys.exit("PURGO_DATABRICKS_HTTP_PATH env variable not set")
	
databricksCatalog = os.getenv("PURGO_DATABRICKS_CATALOG")
if not databricksCatalog:
	sys.exit("PURGO_DATABRICKS_CATALOG env variable not set")
	
databricksSchema = os.getenv("PURGO_DATABRICKS_SCHEMA")
if not databricksSchema:
	sys.exit("PURGO_DATABRICKS_SCHEMA env variable not set")

# Redshift

connect = 'postgresql://' + redshiftUser + ':' + redshiftPassword + "@" + redshiftHost + ":" + redshiftPort + "/" +  redshiftDB  
redshiftEngine = create_engine(connect)

redshiftCols = list()
with redshiftEngine.connect() as connection:
	result = connection.execute("SELECT * FROM information_schema.columns WHERE table_schema = 'tpcds' AND table_name = 'customer_demographics'")
	for row in result:
		redshiftCols.append(row["column_name"])

redshiftCols.sort()

redshiftCount = 0
with redshiftEngine.connect() as connection:
	result = connection.execute("select count(*) as Count from tpcds.customer_demographics")
	for row in result:
		redshiftCount = row["count"]

# Databricks
connection = sql.connect(server_hostname = databricksHost, http_path = databricksHttpPath, access_token = databricksToken)              

databricksCols = list()
tablename = databricksCatalog + "." + databricksSchema + "." + "customer_demographics"
query = "SHOW COLUMNS IN " + tablename
with connection.cursor() as cursor:
	cursor.execute(query)
	result = cursor.fetchall()
	for row in result:
		databricksCols.append(row["col_name"])

databricksCols.sort()

databricksCount = 0
query = "select count(*) as Count from " + tablename
with connection.cursor() as cursor:
	cursor.execute(query)
	result = cursor.fetchall()
	for row in result:
		databricksCount = row["Count"]

if redshiftCols == databricksCols:
	print("Columns are identical")
else:
	print("Columns mismatch")
	print("# of Columns in Redshift: ", len(redshiftCols))
	print("# of Columns in Databricks: ", len(databricksCols))
	print("Redshift Columns: ", redshiftCols)
	print("Databricks Columns: ", databricksCols)
	
if redshiftCount == databricksCount:
	print("Number of rows match")
else:
	print("Row count mismatch")
	print("Redshift Row count: ", redshiftCount)
	print("Databricks Row count: ", databricksCount)
