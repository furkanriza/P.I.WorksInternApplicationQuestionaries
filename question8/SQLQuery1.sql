UPDATE country_vaccination_stats AS v1
SET daily_vaccinations = COALESCE((
  SELECT MEDIAN(daily_vaccinations) AS median_daily_vaccinations
  FROM vaccination_data AS v2
  WHERE v2.country = v1.country AND daily_vaccinations IS NOT NULL
), 0)
WHERE daily_vaccinations IS NULL;
