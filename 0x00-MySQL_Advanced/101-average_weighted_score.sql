-- Update users' average scores by calculating weighted averages for each user

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
    JOIN (
        SELECT u.id, SUM(c.score * p.weight) / SUM(p.weight) AS weight_avg
        FROM users AS u
        JOIN corrections AS c ON u.id = c.user_id
        JOIN projects AS p ON c.project_id = p.id
        GROUP BY u.id
    ) AS w
    ON u.id = w.id
    SET u.average_score = w.weight_avg;
END$$

DELIMITER ;
