-- List bands with Glam rock as their main style ranked by longevity

-- Select the band name and calculate the lifespan
SELECT band_name, COALESCE(SUBSTRING_INDEX(split, '-', -1), 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
