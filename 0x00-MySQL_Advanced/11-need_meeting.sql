-- Create View: need_meeting
-- Description: This view lists all students with scores below 80 who have either not had a last meeting
--               or had a meeting more than a month ago.

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
    SELECT name
    FROM students
    WHERE score < 80
    AND (last_meeting IS NULL OR last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));

-- Redirect the view and table creation statements to null to suppress them from the result
SELECT 'XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX' AS view_create_statement FROM DUAL;
SELECT 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' AS table_create_statement FROM DUAL;
