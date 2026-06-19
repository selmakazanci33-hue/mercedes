SELECT *
FROM dbo.DuplicateEnrollment_Overlap
WHERE
    PA_enrollment_status_description='Cancelled'
 OR PA_enrollee_status_description='Cancelled'
 OR S_enrollment_status_description='Cancelled'
 OR S_enrollee_status_description='Cancelled';
