import stripe

def create_customer(metadata=None):
  try:
    customer_data = {}
    customer_data["metadata"] = {"user_id": metadata}
    customer = stripe.Customer.create(**customer_data)
    return customer
  except stripe.error.StripeError as e:
    return None