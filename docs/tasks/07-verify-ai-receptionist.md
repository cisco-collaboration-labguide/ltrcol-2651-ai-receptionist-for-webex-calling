# Task 7: Verify the AI Receptionist \[10 minutes\]

You will now test the AI Receptionist you built, by calling the assigned number and interacting with it using natural language.

- The AI Receptionist has an internal extension of **6023** (no phone number), and you can call it from **Charles Holland's Webex App** from your physical workstation.

- Reference the table below for information on users, workstations and numbers to use.

| User | Extension | Role | Workstation to use |
| --- | --- | --- | --- |
| **Charles Holland** | 6018 | Caller / Customer | Physical workstation |
| **AI Receptionist** | 6023 | Interactive Agent | Call from Charles Holland (Webex App) |
| **Anita Perez** | 6017 | Operator / Human Agent | Not log into Webex App – call sent to her Voicemail<br>Logged into Webex App – call sent to her Webex App |

## Step 1: Call the AI Receptionist

1. Call the AI Receptionist: Dial ‘***6023*’** from Charles Holland’s Webex App

1. When the AI Receptionist answers the call, ask some questions that you have configured for its Knowledge Base.

Here are some example questions you can use:

- *What are your hours?*

- *What is your address?*

- *Do you have warranties?*

1. Try asking if you can schedule an appointment or talk to someone about warranties? The AI Receptionist should transfer the call to Anita Perez at x6017.

- If you are still logged into the **Webex App** as **Anita** on **Workstation 2**, you will hear and see the incoming call and can answer it.

- If you are not logged into the **Webex App** as **Anita** on **Workstation 2**, you will hear the call transferred to Anita Perez’s Voicemail box.

1. Now let’s try one of the intent-based transfers by asking the AI Receptionist a question around Webex Contact Center support or configuration.

Repeat step 1 and call back into the AI Receptionist. Now ask one of the following questions:

- I need help with configuring Webex Contact Center?

- I’m having issues configuring a Webex Contact Center supervisor and need help?

1. This time the call should be routed to the Webex Contact Center Customer Assist Support queue. This is based on the intent you configured to route calls to this resource for any topics related to Webex Contact Center.

- If you are logged into the **Webex App** as **Taylor Bard** on **Workstation 1 **and **Taylor Bard** is set to **Available**, the call will be forwarded from the queue to Taylor and you will see the incoming call. You can answer or decline the call.

- If you are not logged into the **Webex App** as **Taylor Bard** on **Workstation 1 **or **Taylor** is set to **Unavailable**, the call will wait in the queue for an available agent.

1. If you answered the call, hang up.

**Congratulations! This completes the AI Receptionist for Webex Calling Lab. **

**Please take a moment to review this lab from within the Cisco Live App. **
