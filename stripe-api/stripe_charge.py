import stripe

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'sk_test_3It7UHCpvtNg73oXIUlDZNLB007TpqyIbY'

charge = stripe.Charge.create(
  amount=1000,
  currency='usd',
  source='tok_visa',
  receipt_email='jenny.rosen@example.com',
)

print(charge)

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'sk_test_3It7UHCpvtNg73oXIUlDZNLB007TpqyIbY'

pay = stripe.PaymentIntent.create(
  amount=1000,
  currency='usd',
  payment_method_types=['card'],
  receipt_email='jenny.rosen@example.com',
)

print(pay)
