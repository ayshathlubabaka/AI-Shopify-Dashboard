import shopify
from django.conf import settings

SHOP_NAME = settings.SHOPIFY_STORE_NAME
API_KEY = settings.SHOPIFY_API_KEY
PASSWORD = settings.SHOPIFY_PASSWORD
SHOPIFY_STORE_URL = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}/admin/api/2023-04"

# Initialize Shopify Session
shopify.ShopifyResource.set_site(f"{SHOPIFY_STORE_URL}/api/2023-07")
session = shopify.Session(SHOPIFY_STORE_URL, "2023-07", PASSWORD)
shopify.ShopifyResource.activate_session(session)

def fetch_shopify_data():
    products = shopify.Product.find()
    orders = shopify.Order.find()

    # Extract relevant product and order data
    data = []
    for product in products:
        data.append({
            "product": product.title,
            "sales": product.variants[0].inventory_quantity,  # Example sales data
            "category": product.product_type
        })
    return data
