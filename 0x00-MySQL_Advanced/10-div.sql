-- Function: SafeDiv
-- Description: This function divides the first number by the second number if the second number is not zero,
--              otherwise, it returns 0 to avoid division by zero errors.

DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a FLOAT, b FLOAT) RETURNS FLOAT DETERMINISTIC
BEGIN
    IF b = 0.0 THEN
        RETURN 0.0;
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;
