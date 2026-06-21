CREATE VIEW irr_by_age_outcome AS
SELECT age_group, outcome, AVG(crude_irr) AS avg_irr
FROM vaccine
GROUP BY 2, 1;

CREATE VIEW irr_trend_by_month AS 
SELECT month, outcome, AVG(crude_irr) AS avg_irr
FROM vaccine
GROUP BY 1, 2;

CREATE VIEW cases_deaths_by_age AS
WITH irr_case_death AS (
	SELECT age_group,
	AVG(CASE WHEN outcome = 'case' THEN crude_irr END) AS case_irr,
	AVG(CASE WHEN outcome = 'death' THEN crude_irr END) AS death_irr
	FROM vaccine
	GROUP BY 1
)
SELECT age_group, (irr.case_irr - irr.death_irr) AS irr_difference
FROM irr_case_death AS irr;