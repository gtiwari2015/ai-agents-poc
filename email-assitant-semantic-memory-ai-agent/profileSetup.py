import os
from dotenv import load_dotenv
_ = load_dotenv()

profile = {
    "name": "Gaurav",
    "full_name": "Gaurav Tiwari",
    "user_profile_background": "Senior Technical Architect",
}

prompt_instructions = {
    "triage_rules": {
        "ignore": "Marketing newsletters, spam emails, mass company announcements",
        "notify": "Team member out sick, build system notifications, project status updates",
        "respond": "Direct questions from team members, meeting requests, critical bug reports",
    },
    "agent_instructions": "Use these tools when appropriate to help manage Gaurav's tasks efficiently."
}

# Example incoming email
email = {
    "from": "Gaurav Tiwari <gaurav.tiwari@company.com>",
    "to": "John Doe <john.doe@company.com>",
    "subject": "Quick question about API documentation",
    "body": """
Hi John,

I was reviewing the API documentation for the new authentication service and noticed a few endpoints seem to be missing from the specs. Could you help clarify if this was intentional or if we should update the docs?

Specifically, I'm looking at:
- /auth/refresh
- /auth/validate

Thanks!
Gaurav""",
}