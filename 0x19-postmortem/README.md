> ### [Postmortem: API Service Outage](https://)

----------

Issue Summary:

-   Duration: August 10, 2024, 3:00 PM - 5:30 PM (UTC)
    
-   Impact: The API service was down for 2.5 hours, affecting 80% of users. During this period, users experienced timeouts and failure in data retrieval from our platform. Both web and mobile applications could not connect to the backend, rendering the service unusable.
    
-   Root Cause: The outage was caused by an unhandled exception in a newly deployed API endpoint, which triggered a cascading failure across multiple services.
    

----------

### Timeline:

-   3:00 PM: Issue detected by automated monitoring alert indicating a sudden drop in API response rates.
    
-   3:05 PM: Engineers confirmed the alert and began investigating API logs for anomalies.
    
-   3:15 PM: Initial suspicion pointed to a network connectivity issue; network logs were reviewed, but no abnormalities were found.
    
-   3:30 PM: API service team escalated the issue to the backend infrastructure team for deeper investigation.
    
-   3:45 PM: Misleading error logs led the team to investigate potential database connectivity issues.
    
-   4:15 PM: The database team confirmed there were no issues with the database servers.
    
-   4:30 PM: Focus shifted back to the API service. Deeper log analysis revealed an unhandled exception in a newly deployed endpoint.
    
-   4:45 PM: The problematic code was identified and the deployment was rolled back.
    
-   5:00 PM: System recovery began, and API services slowly returned to normal.
    
-   5:30 PM: Full service was restored, and monitoring confirmed normal operations.
    

----------

### Root Cause and Resolution:

Root Cause: The issue was traced back to a recent deployment that included an update to the API service. A new endpoint was introduced to handle bulk data requests, but it contained an unhandled exception that was not caught during testing. This exception caused the API service to crash, triggering failures in dependent services, and leading to a cascading outage.

Resolution: The team immediately rolled back the recent deployment once the unhandled exception was identified. The rollback restored the previous stable version of the API service, and normal functionality resumed. The team then conducted a code review and implemented a fix for the exception. The updated code was thoroughly tested and redeployed without issues.

----------

### Corrective and Preventative Measures:

Improvements Needed:

-   Enhance pre-deployment testing to include more comprehensive scenarios, especially for newly introduced features.
    
-   Improve logging clarity to avoid misleading errors that can waste investigation time.
    
-   Strengthen monitoring to detect similar issues earlier and prevent cascading failures.
    

Action Items:

1.  Patch API Service: Implement a fix for the unhandled exception and thoroughly test before redeployment.
    
2.  Expand Test Coverage: Add specific test cases for the newly introduced endpoint, including edge cases.
    
3.  Improve Logging: Refactor logging in the API service to provide clearer and more actionable error messages.
    
4.  Deploy Circuit Breaker: Implement a circuit breaker pattern in the API service to prevent cascading failures in case of future errors.
    
5.  Review Monitoring Rules: Update monitoring rules to catch similar exceptions earlier and alert the team before widespread impact occurs.

