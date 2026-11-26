-- Weekly disposable income by city and industry
-- Assumptions: tax resident, 24 hours/week (12 weekday, 6 Saturday, 6 Sunday), Level 1 casual award rates

WITH hours(day_type, h) AS (VALUES ('Weekday', 12), ('Saturday', 6), ('Sunday', 6)),

gross AS (
  SELECT CASE WHEN award LIKE 'Restaurant%' THEN 'Hospitality' ELSE 'Retail' END AS industry,
         SUM(f.casual_hourly_rate * hr.h)      AS gross_week,
         SUM(f.casual_hourly_rate * hr.h) * 52 AS annual
  FROM fair_work_rates f
  JOIN hours hr USING (day_type)
  WHERE f.level = 'Level 1'
  GROUP BY 1),

bracket AS (
  SELECT g.industry, g.annual, t.base_tax, t.rate,
         GREATEST(t.income_from - 1, 0) AS thr,
         ROW_NUMBER() OVER (PARTITION BY g.industry ORDER BY t.income_from DESC) AS rn
  FROM gross g
  JOIN tax_rates t ON t.residency = 'Resident'
                  AND GREATEST(t.income_from - 1, 0) < g.annual),

tax AS (
  SELECT industry, annual, base_tax + rate * (annual - thr) AS tax_before_offset
  FROM bracket WHERE rn = 1),

offset_row AS (
  SELECT x.industry, l.max_offset, l.reduction_rate, l.reduction_starts_at,
         ROW_NUMBER() OVER (PARTITION BY x.industry ORDER BY l.income_from DESC) AS rn
  FROM tax x
  JOIN lito l ON l.income_from - 1 < x.annual),

net AS (
  SELECT x.industry,
         (x.annual - GREATEST(x.tax_before_offset
            - GREATEST(o.max_offset - o.reduction_rate * (x.annual - o.reduction_starts_at), 0), 0)) / 52
         AS net_week
  FROM tax x
  JOIN offset_row o ON o.industry = x.industry AND o.rn = 1),

costs AS (
  SELECT r.city,
         r.weekly_rent AS rent_share,
         a.weekly_rent AS rent_alone,
         t.weekly_cost_aud AS transport,
         fd.food_weekly_aud AS food
  FROM rent r
  JOIN rent a ON a.city = r.city AND a.housing_type = 'All units'
  JOIN transport t ON t.city = r.city AND t.scenario = 'base'
  JOIN food_scenarios fd ON fd.city = r.city AND fd.scenario = 'base'
  WHERE r.housing_type = 'Share room'),

fixed AS (
  SELECT (SELECT AVG(weekly_aud) FROM insurance)
       + (SELECT SUM(weekly_aud) FROM living_costs_other WHERE scenario = 'base') AS fixed_week)

SELECT c.city,
       n.industry,
       ROUND(n.net_week - (c.rent_share + c.transport + c.food + f.fixed_week), 2) AS disposable_share,
       ROUND(n.net_week - (c.rent_alone + c.transport + c.food + f.fixed_week), 2) AS disposable_alone,
       RANK() OVER (PARTITION BY n.industry
                    ORDER BY n.net_week - (c.rent_share + c.transport + c.food + f.fixed_week) DESC) AS rank_share
FROM costs c
CROSS JOIN net n
CROSS JOIN fixed f
ORDER BY n.industry, rank_share;