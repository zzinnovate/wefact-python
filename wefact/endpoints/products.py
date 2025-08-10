# File: /wefact-python/wefact-python/src/wefact/endpoints/products.py

from wefact.endpoints.base import BaseEndpoint

class ProductsEndpoint(BaseEndpoint):
    def list(self):
        """List all products."""
        return self.get('products')

    def create(self, product_data):
        """Create a new product.

        Required parameters: ProductName, ProductKeyPhrase, PriceExcl.
        """
        return self.post('products', json=product_data)

    def edit(self, product_id, product_data):
        """Update an existing product.

        Required parameter: Identifier or ProductCode.
        """
        return self.put(f'products/{product_id}', json=product_data)

    def show(self, product_id):
        """Show details of a specific product.

        Required parameter: Identifier or ProductCode.
        """
        return self.get(f'products/{product_id}')

    def delete(self, product_id):
        """Delete a product.

        Required parameter: Identifier or ProductCode.
        """
        return self.delete(f'products/{product_id}')