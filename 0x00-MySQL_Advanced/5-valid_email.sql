-- Trigger: Reset 'valid_email' attribute on email change
-- Description: Create a trigger to reset the 'valid_email' attribute in response to email changes.

DELIMITER $$
-- Create a trigger that activates before updating the 'email' column
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;
