-- Rank country origins of bands by the number of (non-unique) fans

-- Select the origin and the total number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
