-- Stored Procedure: AddBonus
-- Description: Adds a new correction for a student. If the project doesn't exist in the projects table, it creates it.

DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id INTEGER,
    IN project_name VARCHAR(255),
    IN score INTEGER
)
BEGIN
    -- Check if the project name already exists in the projects table
    INSERT INTO projects (name)
    SELECT project_name
    FROM DUAL
    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name LIMIT 1);

    -- Insert the correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$
DELIMITER ;
