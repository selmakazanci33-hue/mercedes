SELECT
    'PA Enrollment' AS Status_Type,
    PA_enrollment_status_description AS Status,
    COUNT(*) AS Total
FROM dbo.DuplicateEnrollment_Overlap
GROUP BY PA_enrollment_status_description

UNION ALL

SELECT
    'PA Enrollee',
    PA_enrollee_status_description,
    COUNT(*)
FROM dbo.DuplicateEnrollment_Overlap
GROUP BY PA_enrollee_status_description

UNION ALL

SELECT
    'Subscriber Enrollment',
    S_enrollment_status_description,
    COUNT(*)
FROM dbo.DuplicateEnrollment_Overlap
GROUP BY S_enrollment_status_description

UNION ALL

SELECT
    'Subscriber Enrollee',
    S_enrollee_status_description,
    COUNT(*)
FROM dbo.DuplicateEnrollment_Overlap
GROUP BY S_enrollee_status_description

ORDER BY Status_Type, Status;
