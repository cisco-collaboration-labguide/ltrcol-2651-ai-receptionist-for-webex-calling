<section class="home-hero">
  <div class="home-hero__content">
    <p class="home-hero__eyebrow">CISCO LIVE MELBOURNE 2026 · LTRCOL-2651</p>
    <h1>AI Receptionist<br>for Webex Calling</h1>
    <p class="home-hero__description">Configure an AI Receptionist, build its knowledge base, route callers to support teams, and test the complete experience.</p>
    <p class="home-hero__byline">Hussain Ali · Technical Marketing Engineer</p>
    <div class="home-hero__actions">
      <a class="home-hero__primary" href="tasks/01-access-the-lab/">Get started <span aria-hidden="true">⟶</span></a>
      <a class="home-hero__secondary" href="tasks/03-configure-ai-receptionist/">Go to the lab <span aria-hidden="true">⟶</span></a>
    </div>
  </div>
  <span class="home-hero__orb" aria-hidden="true"></span>
</section>

<p class="lab-meta">Guide date: November 12, 2026 · Estimated lab time: 74 minutes</p>

!!! info "Before you start"

    Have your assigned dCloud session available. Use your own session’s domain, credentials, and PSTN numbers wherever the guide shows examples. Tasks 4–6 require the Customer Assist queues and user roles described in the guide to exist in your lab.

## Learning Objectives \[1 minute\] { #learning-objectives-1-minute }

Upon completion of this lab, you will:

- Have fundamental knowledge of <strong>AI Receptionist for Webex Calling</strong>. Their key capabilities, how to configure them and how they work.

- How to configure an AI Receptionist along with its knowledge base and interact with the AI Receptionist to see the experience

## Scenario \[3 minutes\] { #scenario-3-minutes }

In this lab, you will gain hands-on experience in configuring and testing the <strong>AI Receptionist.</strong> This lab provides step-by-step instructions for setting up an AI Receptionist.

Here are the high-level TASKS to achieve the objectives of this lab:

- [TASK 1: Accessing the lab](tasks/01-access-the-lab.md)

- [TASK 2: Access the Collaboration Control Hub](tasks/02-control-hub.md)

- [TASK 3: Configure an AI Receptionist](tasks/03-configure-ai-receptionist.md)

- [TASK 4: Configure intent-based routing for the AI Receptionist](tasks/04-intent-based-routing.md)

- [TASK 5: Log into the Webex App for all users](tasks/05-webex-app.md)

- [TASK 6: Verify and interact with the AI Receptionist](tasks/06-verify-ai-receptionist.md)

## Lab Topology \[5 minutes\] { #lab-topology-5-minutes }

The lab already has the Unified Communications Manager and Unity Connection with preconfigured users and devices.

![Lab Topology [5 minutes] — screenshot 1](assets/images/image6.jpg){ .lab-screenshot width="668" loading="lazy" }

Table 1 - Lab Details

| <strong>Application</strong> | <strong>Version</strong> | <strong>IP address or URL</strong> | <strong>Username</strong> | <strong>Password</strong> |
| --- | --- | --- | --- | --- |
| Cisco Unified CM | 14.x | 198.18.133.3 | administrator | dCloud123! |
| Unity Connection | 14.x | 198.18.133.5 | administrator | dCloud123! |
| User Workstation 1 | Windows 10 | 198.18.1.36 | dcloud\cholland | dCloud123! |
| User Workstation 2 | Windows 10 | 198.18.1.37 | dcloud\aperez | dCloud123! |
| User Workstation 3 | Windows 10 | 198.18.1.35 | dcloud\kmelby | dCloud123! |
| User Workstation 4 | Windows 10 | 198.18.1.40 | dcloud\tbard | dCloud123! |
| Cisco CSR8000v (LGW) | 17.13.1a | 198.18.133.227<br>198.18.1.227 | admin | dCloud123! |
| Collaboration Control Hub |  | [https://admin.webex.com](https://admin.webex.com) | cholland@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | dCloud<mark>ZZZZ</mark>! |

Table 2 - User Details

| <strong>User</strong> | <strong>Mail ID</strong> | <strong>Directory Number</strong> | <strong>Webex Calling Enabled</strong> |
| --- | --- | --- | --- |
| Adam McKenzie | amckenzie@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6016 | N |
| Anita Perez | aperez@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6017 | <strong>Y</strong> |
| Charles Holland | cholland@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6018 | <strong>Y</strong> |
| Eric Steele | esteele@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6099 | N |
| Kellie Melby | kmelby@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6050 | <strong>Y</strong> |
| Monica Cheng | mcheng@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6020 | N |
| Rebekah Barretta | rbarretta@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6088 | N |
| Ricardo Filice | rfilice@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6083 | N |
| Stefan Mauk | smauk@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6072 | N |
| Taylor Bard | tbard@cb<mark>XXX</mark>.dc-<mark>YY</mark>.com | 6026 | <strong>Y</strong> |

!!! note

    Details on how to find your lab domain name (@cbXXX.dc-YY.com) and the last 4-digits of your lab session ID (<mark>ZZZZ</mark>) will be explained in <strong>Task 1: Accessing the Lab</strong>.
