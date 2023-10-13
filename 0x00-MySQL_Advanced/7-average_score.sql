-- Procedure: ComputeAverageScoreForUser
-- Description: This stored procedure calculates the average score for a user based on their
-- corrections and updates the user's record with the result.

DELIMITER $$
-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Update the 'average_score' field in the 'users' table with the calculated average
    -- from the 'corrections' table for the specified user.
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id)
    WHERE id = user_id;
END $$
DELIMITER ;
