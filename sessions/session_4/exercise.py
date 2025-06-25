# Each record represents an order. Orders contain nested details:
#   - A customer object (with ID, name, address).
#   - A list of items (products with price, quantity).
#   - A payment object.
#   - A shipping object.
# You will create the following tables:
#   - customers: one row per customer
#   - orders: one row per order
#   - order_items: one row per item per order
#   - products: optional (deduplicate products from order items)
#   - payment: one row per order
#   - shipping: one row per order

# Think about reuseability (modularity).
# We will want to run an update at some point, what are the unique identifiers to determine the update, how do you know if a row has changed?
# Export to a tabular format as a csv. 