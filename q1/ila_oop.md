Sari-Sari Store Inventory System

1. Encapsulation
Encapsulation combines product attributes (“name”, “price”, “stock’’) and behaviors 
such as “update_stock” within a single “Product” class while protecting sensitive data 
from direct access. Private variables like “private_price” and “private_stock” can only be 
changed through getter and setter methods, which validate inputs to prevent negative prices 
or inventory. This keeps the data consistent and prevents accidental modification from other 
parts of the program.

2. Abstraction
Abstraction conceals the system’s internal processes and provides only the essential methods 
for users or operators. For example, a “PointOfSale” or “Inventory” class can offer a simple 
“sell_item(product_id, quantity)” method while internally handling stock verification, 
tax computation, and receipt generation. This allows the rest of the program to use a 
straightforward interface without knowing the underlying implementation.

3. Inheritance
Inheritance enables specialized product classes to inherit shared attributes (“name”, “price”
, “stock”) and behaviors from the “Product” superclass. Classes such as “PerishableProduct” 
(with an “expiration_date” property) and “Beverage” (with “liter_size” or “is_cold”) reuse 
the base functionality while adding their own features. This reduces repeated code and makes 
expanding product categories much easier.

4. Polymorphism
Polymorphism allows different product classes to share the same method names while performing
different actions. Both “StandardProduct” and “PerishableProduct” can implement
“calculate_discount()”, but the perishable version applies a clearance discount when the
product is close to its expiration date. A single loop can process different “Product” 
objects and call “.calculate_discount()” or “.get_details()” without checking each object’s
class.

Reflection
Among the four pillars, Encapsulation is the most important for a sari-sari store inventory 
system. Accurate stock levels and pricing are essential to avoid inventory errors and 
financial loss. By requiring all changes to pass through validated methods, encapsulation 
prevents invalid values such as negative stock and maintains reliable, consistent records 
that serve as the foundation of the entire system.

