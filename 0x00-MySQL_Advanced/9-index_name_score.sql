-- Create Index: idx_name_first_score
-- Index the first letter of the 'name' and 'score' columns in the 'names' table.
CREATE INDEX idx_name_first_score ON names(name(1), score);
