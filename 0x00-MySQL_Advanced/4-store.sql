-- Trigger: Decrease item quantity when a new order is placed
-- The `items` table quantity can be a negative value

CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET
quantity = quantity - NEW.number
WHERE name = NEW.item_name;
