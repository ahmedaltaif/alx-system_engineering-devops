incident report for the recent website outage

JUNE 18, 2023

By Digitalplus team

The following is the incident report for the recent website outage caused by a firewall configuration issue.

Issue Summary

Duration of Outage: The outage lasted for 30 minutes, starting at 4:45 PM and ending at 5:15 PM (GMT).

Impact: The website was completely down, affecting 100% of users. Users were unable to access any part of the website, resulting in complete service disruption.

Root Cause: The root cause was a misconfiguration in the UFW firewall settings that inadvertently blocked a critical port necessary for the website's operation.
Timeline

    4:45 PM: Issue detected via automated monitoring alert indicating the website was down.
    4:47 PM: Alert acknowledged by the on-call engineer.
    4:50 PM: Initial investigation began, focusing on the web server status and logs.
    4:55 PM: Checked application server and database server status, found both to be operational.
    5:00 PM: Reviewed recent deployments and configuration changes; no issues found.
    5:05 PM: Identified a firewall configuration change as a potential cause.
    5:10 PM: Verified the UFW firewall settings and discovered a blocked port critical for the website's operation.
    5:12 PM: Adjusted UFW settings to unblock the necessary port.
    5:13 PM: Confirmed that the website began to recover.
    5:15 PM: Full service restored, and monitoring confirmed website functionality.

Root Cause and Resolution

Root Cause: The outage was caused by an accidental misconfiguration of the UFW firewall. A critical port required for the website's operation was blocked due to a recent update to the firewall rules. This blocked all incoming traffic to the web server, causing a complete outage.

Resolution: The issue was resolved by identifying the misconfigured firewall settings and unblocking the required port. Specifically, the following command was used to unblock the port:

sudo ufw allow <port_number>

Once the port was unblocked, normal traffic resumed, and the website became accessible again.
Corrective and Preventative Measures

Improvements and Fixes:

    Enhance Monitoring:
        Implement more granular monitoring to detect firewall-related issues immediately.
        Set up alerts specifically for changes in firewall settings.

    Review and Documentation:
        Conduct a comprehensive review of firewall rules and document the configuration process to prevent future errors.
        Implement a change management process that includes peer review for all firewall changes.

    Automation:
        Automate the deployment of firewall rules with proper validation checks to prevent accidental misconfigurations.