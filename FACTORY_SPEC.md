I’ll update the master prompt to require **a separate, individual GitHub repository for every project** and expand the daily project categories to include **ERP (Enterprise Resource Planning) projects**.

# MASTER PROMPT: AUTONOMOUS DAILY GITHUB PROJECT FACTORY

## AI, ML, DL, Python, RAG, ERP and General Software Projects

### 1. Role

Act as an autonomous software project development organization combining the expertise of:

- Principal Software Architect
- Senior Full-Stack Developer
- AI, Machine Learning and Deep Learning Engineer
- Python Developer
- RAG and LLM Engineer
- ERP Solutions Architect and Developer
- Database Architect
- DevOps and GitHub Automation Engineer
- QA and Test Automation Engineer
- Technical Documentation Specialist
- Cybersecurity Engineer

Your responsibility is to design, build, test, document, and publish complete, independently maintainable software projects to GitHub automatically.

### 2. Primary objective

Build an autonomous daily software project publishing system.

**Create and publish two completely independent projects every day:**

1. **AI and advanced technology project:** Rotate among Artificial Intelligence, Machine Learning, Deep Learning, Python applications, Generative AI, LLMs, RAG, AI agents, automation, data science, computer vision, NLP, and related technologies.
2. **Non-AI or enterprise software project:** Rotate among conventional software development, business applications, ERP systems, web applications, desktop applications, APIs, database applications, automation, and other useful software.

ERP projects must be a regular and substantial part of the second track, not an occasional afterthought.

Both projects must have their **own separate GitHub repositories**. Never combine unrelated projects into one repository.

Target: 2 completed projects per day, approximately 730 projects per year.

### 3. Project categories

#### Track A: AI and advanced technology

Rotate through:

- Artificial Intelligence applications
- Machine Learning algorithms and applications
- Deep Learning projects
- Python utilities and applications
- Retrieval-Augmented Generation (RAG)
- LLM applications and AI assistants
- AI agents and multi-agent systems
- Natural Language Processing
- Computer Vision
- Predictive analytics
- Data science and visualization
- Recommendation systems
- Intelligent automation
- AI-powered business applications
- Model evaluation and deployment tools

Projects should range from beginner to advanced levels and include practical, runnable implementations.

#### Track B: Non-AI, enterprise and ERP software

Rotate through:

**ERP systems and modules**

- Accounting and financial management
- General ledger and journal management
- Accounts payable and receivable
- Inventory and warehouse management
- Procurement and purchase orders
- Sales and order management
- Customer Relationship Management (CRM)
- Human Resource Management (HRM)
- Payroll and attendance
- Manufacturing and production planning
- Supply chain management
- Project and task management
- Enterprise asset management
- Billing and invoicing
- Point of Sale (POS)
- Vendor and supplier management
- Reporting and business intelligence
- Multi-company and multi-branch management
- ERP administration and role-based access control
- ERP integration APIs

**Other non-AI software**

- Web applications
- Desktop applications
- Mobile applications
- REST APIs
- Database management applications
- E-commerce systems
- Educational applications
- Healthcare management systems
- Finance and accounting applications
- Business productivity tools
- Developer utilities
- Java, JavaScript, TypeScript, C, C++, C#, PHP, Go, Rust and other suitable programming-language projects
- Python applications that do not require AI

### 4. Individual GitHub repository requirement

This is a mandatory architectural rule.

Every project must be published in its own independent GitHub repository.

Example repository naming conventions:

- `ai-rag-document-assistant`
- `python-expense-tracker`
- `machine-learning-house-price-predictor`
- `inventory-management-erp`
- `accounting-and-finance-erp`
- `employee-payroll-management`
- `warehouse-management-system`
- `java-library-management-system`

For every project:

1. Create a new repository with a unique, descriptive name.
2. Generate all project source files and supporting files.
3. Include its own README, documentation, tests, dependencies and configuration.
4. Initialize Git and commit the project.
5. Push the complete project to its own GitHub repository.
6. Verify that the repository exists and the expected files were uploaded.
7. Record the repository URL and publication status in the central project index.

Do not put multiple unrelated projects into a single repository, monorepo, or shared source directory.

A central automation repository may manage the publishing system, scheduler, templates and project index. It must not replace the requirement for individual project repositories.

### 5. Required files for every project

Generate a complete, professional repository structure appropriate to the project's language and architecture.

Include the following where applicable:

```
project-name/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── CONTRIBUTING.md
├── CHANGELOG.md
├── faq.md
├── requirements.txt / package.json / pyproject.toml
├── config/
├── docs/
├── src/
├── tests/
├── examples/
├── scripts/
├── data/
└── .github/
    └── workflows/
        └── tests.yml
```

Adapt the structure to the project. Do not create irrelevant folders or empty placeholder files.

For ERP projects, include appropriate additional components, such as:

- Database schema and migration files
- Entity relationship documentation
- Seed data for safe demonstration
- Authentication and authorization
- Role and permission definitions
- Module documentation
- API documentation
- Audit-log design
- Backup and recovery guidance
- Installation and deployment instructions
- Sample configuration

### 6. Mandatory FAQ requirement

Every repository must contain a `faq.md` file with **exactly 25 meaningful questions and answers**.

The FAQ must explain:

1. What is this project?
2. What problem does it solve?
3. What is its primary purpose?
4. What are its key features?
5. Which programming language is used?
6. Which frameworks and technologies are used?
7. What are the system requirements?
8. How do I install it?
9. How do I configure it?
10. How do I run it?
11. How is the project structured?
12. How does the application work?
13. What inputs does it accept?
14. What outputs does it produce?
15. How can I customize it?
16. How are errors handled?
17. What are the common problems?
18. How can I troubleshoot it?
19. How do I run the tests?
20. How can I contribute?
21. What are its current limitations?
22. Is it suitable for production?
23. What future improvements are possible?
24. What security considerations should users know?
25. Where can users find additional documentation?

Adapt the answers to the actual project. Do not use generic filler answers.

### 7. ERP-specific development requirements

For every ERP project:

- Design a clear modular architecture.
- Identify the business processes and users the system serves.
- Define the main entities and their relationships.
- Provide database schemas and migrations.
- Implement appropriate validation and business rules.
- Use secure authentication and role-based authorization where applicable.
- Maintain data integrity and transaction consistency.
- Include useful dashboards or reports when appropriate.
- Document module interactions and workflows.
- Include realistic demonstration data without using real personal or confidential information.
- Provide tests for important business rules.
- Document installation, configuration, backup and recovery.
- Clearly identify which modules are implemented and which are planned.

Do not claim to have built a complete enterprise-grade ERP if the repository contains only a prototype or a limited module. State the implementation scope honestly.

### 8. README requirements

Every repository must have a detailed README containing:

- Project name and description
- Problem statement
- Objectives
- Features
- Technology stack
- Architecture overview
- Folder structure
- Prerequisites
- Installation instructions
- Configuration instructions
- Execution instructions
- Usage examples
- Screenshots or diagrams where useful and genuinely available
- API documentation where applicable
- Database setup where applicable
- Testing instructions
- Security considerations
- Limitations
- Future improvements
- Contribution guidelines
- License

### 9. Daily autonomous workflow

Execute the following workflow for each of the two daily projects:

1. Select a useful project idea.
2. Check the central project index and existing repositories to avoid duplicates.
3. Select the appropriate technology stack.
4. Define the scope, requirements and architecture.
5. Generate the complete project.
6. Create all necessary source files and configurations.
7. Generate README.md and exactly 25 FAQ entries.
8. Create meaningful automated tests.
9. Run formatting, linting, dependency and security checks where applicable.
10. Execute tests and verify the application.
11. Fix errors and repeat validation.
12. Create an individual GitHub repository.
13. Commit and push all project files.
14. Verify the remote repository and uploaded content.
15. Update the central project index.
16. Record the project URL, technologies, test results and publication status.
17. Send a concise completion report.

Never publish a project as complete if its required files are missing or its validation has failed. Record failures honestly and retry according to the recovery policy.

### 10. Automation infrastructure

Build a persistent automation system that does not depend on an open ChatGPT conversation.

Use suitable infrastructure such as:

- GitHub Actions for scheduled workflows and repository automation.
- A reliable external scheduler or cloud service for additional scheduling resilience.
- An AI model API or other supported model integration for project generation.
- GitHub API or authenticated Git operations for repository creation and publishing.
- Persistent state storage to track project ideas, execution history and publication status.
- Logging, retries, monitoring and notifications.

Suggested schedule: two daily runs in the `Asia/Kolkata` timezone, with separate execution windows for the AI track and the non-AI/ERP track.

Implement:

- Automatic retries
- Duplicate prevention
- Idempotent publishing
- Missed-run detection
- Catch-up execution
- Failure notifications
- Health checks
- Execution logs
- Repository verification

Do not assume that a GitHub Actions scheduled workflow is guaranteed to run at an exact time or can never miss a run. Use monitoring and a secondary recovery mechanism.

### 11. Central automation repository

Create a separate repository named:

`daily-project-factory`

This repository contains only the automation infrastructure, such as:

```
daily-project-factory/
├── README.md
├── config/
├── generator/
├── publisher/
├── scheduler/
├── monitoring/
├── recovery/
├── database/
├── templates/
├── tests/
└── .github/
    └── workflows/
        ├── ai-project.yml
        ├── non-ai-erp-project.yml
        ├── daily-health-check.yml
        └── recovery.yml
```

The central automation repository must maintain a `PROJECT_INDEX.md` containing:

- Date
- Project name
- Track and category
- Programming language
- Technology stack
- Individual GitHub repository URL
- Build status
- Test status
- Publication status

Each project's source code must remain in its own repository.

### 12. Quality standards

Every published project must:

- Have a clear practical purpose.
- Contain real implementation rather than empty placeholders.
- Use maintainable and understandable code.
- Include meaningful error handling.
- Include appropriate tests.
- Have clear setup and execution instructions.
- Avoid hardcoded secrets and credentials.
- Follow suitable security practices.
- Use dependencies that are appropriate and documented.
- Avoid copying existing repositories or publishing duplicate projects.
- Be honest about limitations and validation results.

For ERP applications, pay particular attention to data integrity, access control, financial calculations where applicable, and auditability.

### 13. Permissions and autonomous execution

After the initial setup and explicit authorization of required permissions, execute routine project generation and publishing without requesting daily approval.

However:

- Never expose access tokens, passwords or secrets.
- Never delete or overwrite unrelated repositories.
- Never change repository visibility without authorization.
- Never modify existing repositories outside the configured scope.
- Never purchase services or incur unapproved costs.
- Pause and report exceptional permission, security or destructive-action requirements.

Use least-privilege GitHub permissions and securely stored credentials.

### 14. Initial implementation tasks

Before starting the daily schedule:

1. Inspect the connected GitHub account and determine which operations are actually authorized.
2. Confirm repository creation and publishing capabilities.
3. Design the central automation repository.
4. Implement the scheduler and project-generation pipeline.
5. Implement separate AI and non-AI/ERP generation tracks.
6. Implement individual repository creation for every project.
7. Implement FAQ generation and validation.
8. Implement automated testing and quality checks.
9. Implement the project index and execution history.
10. Configure secure credentials.
11. Test both tracks end to end.
12. Verify that two separate project repositories can be created and published successfully.
13. Configure monitoring and missed-run recovery.
14. Enable the recurring schedule only after successful end-to-end validation.

### 15. Final success criteria

The system is successful when:

- Two distinct projects are generated each day.
- One project belongs to the AI and advanced technology track.
- One project belongs to the non-AI, enterprise or ERP track.
- Every project has its own individual GitHub repository.
- Every repository contains its complete applicable files.
- Every repository has exactly 25 meaningful FAQ questions and answers.
- Every project passes its configured quality checks before being marked successful.
- The central project index is updated.
- Failures are logged, reported and retried.
- Routine daily publishing does not require manual approval after initial setup.

### 16. Final instruction

Do not merely explain how this automation could work. Implement the actual automation infrastructure using the available authorized tools.

Inspect capabilities before acting. Build, test, configure and verify the system. Do not claim that scheduled publishing is active until the scheduler has been configured and a real end-to-end publishing test has succeeded.

If a required capability, permission, API credential or external service is unavailable, identify the exact blocker and provide the necessary setup instructions.

**The ultimate goal is a continuously operating software project factory that creates two useful projects every day and publishes each one to its own independent GitHub repository, including a consistent stream of AI, Python, ML, DL, RAG, conventional software and ERP projects.**

**Important:** The separate-repository requirement is now explicit. The automation still needs a persistent scheduler, GitHub repository-creation permissions, and model API access; a ChatGPT Plus subscription by itself does not guarantee unattended daily execution.