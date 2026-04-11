# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

Choice: App Service (Web App)
Cost: Lower operational cost—no need to manage OS, patches, or infrastructure compared to VMs.
Scalability: Built-in auto-scaling makes it easy to handle traffic spikes without manual intervention.
Availability: High availability with SLA-backed uptime and managed load balancing.
Workflow: Simplified deployment (CI/CD integration) and faster development cycle.
Justification: App Service is ideal for a CMS web app because it reduces maintenance overhead, scales automatically, and supports modern deployment workflows, making it more efficient than managing a VM.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 