-- Stored Procedure: ComputeAverageScoreForUser
-- Description: This stored procedure computes and stores the average score for a student.
--              It takes a user_id as input, which is assumed to be linked to an existing user.

DELIMITER $$

-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Update the average_score for the specified user
    UPDATE users
    SET
        average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id)
    WHERE id = user_id;
END $$

DELIMITER ;
