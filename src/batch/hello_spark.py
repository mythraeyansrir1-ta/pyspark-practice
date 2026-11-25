
from pyspark.sql import SparkSession

# Create SparkSession
spark = (
    SparkSession.builder
    .appName("RetailDataEngineering")
    .master("local[*]")
    .getOrCreate()
)

# Sample retail transactions
data = [
    (101, "Laptop", 55000),
    (102, "Mouse", 800),
    (103, "Keyboard", 1500),
    (104, "Monitor", 12000)
]

columns = ["transaction_id", "product", "amount"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Display original DataFrame
print("Original Transactions:")
df.show()

# Transformation
high_value = df.filter(df.amount > 1000)

print("High Value Transactions:")
high_value.show()

# Stop SparkSession
spark.stop()
