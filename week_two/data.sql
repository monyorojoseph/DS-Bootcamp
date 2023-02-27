SELECT
  s.submission_date AS date,
  COUNT(DISTINCT s.hacker_id) AS num_hackers,
  h.hacker_id,
  h.name,
  COUNT(s.submission_id) AS num_submissions
FROM
  Submissions s
  JOIN Hackers h ON s.hacker_id = h.hacker_id
WHERE
  s.submission_date BETWEEN '2016-03-01' AND '2016-03-15'
GROUP BY
  s.submission_date,
  h.hacker_id
HAVING
  COUNT(s.submission_id) = (
    SELECT MAX(subs.num_submissions)
    FROM (
      SELECT
        submission_date,
        hacker_id,
        COUNT(submission_id) AS num_submissions
      FROM
        Submissions
      WHERE
        submission_date = s.submission_date
      GROUP BY
        submission_date,
        hacker_id
    ) subs
  )
ORDER BY
  s.submission_date
