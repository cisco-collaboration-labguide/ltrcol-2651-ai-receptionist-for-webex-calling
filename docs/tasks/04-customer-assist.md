# Task 4: Prepare Webex Calling Customer Assist \[10 minutes\]

In this task you build the pieces that the Auto Attendant and the Customer Assist queues need, all in Collaboration Control Hub:

- Create the greeting callers hear, with text-to-speech

- Create an office hours schedule

- Create an Auto Attendant

- Create the queues

## Step 1: Create the greeting with text-to-speech

In this step, you create the greeting callers hear when they reach the Auto Attendant. You don't need an audio file: you type the text, and Webex turns it into speech.

Webex can create announcement audio files with **text-to-speech (TTS)**. You generate audio messages directly from written text, which makes it easier to create and manage audio announcements in the Webex Calling announcement repository. You can manage and update TTS announcements in one central place, with dynamic control over every announcement that uses the repository.

TTS also works across the supported features, allows rich customization with SSML tags for expressive, natural-sounding speech, and offers several voice and gender options to suit your business.

1. In Collaboration Control Hub, go to **SERVICES &gt; Calling**, click the **Features** tab, then click **Add new** on the **Announcements** card.

![Source screenshot image49](../assets/images/updated-image49.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the new announcement page, click the **Text to speech** tab. Use these details, then click **Generate**:

    1. **Location**: dCloud

    1. **Label: **Welcome Message

    1. **File name:** Welcome Message.wav

    1. **Text: ***Use the text below in the box*

!!! note

    Welcome to the support help desk. If you need Webex Calling support, please press 1. If you need Webex Contact Center Support, please press 2. To repeat this menu, please press 9.

    1. **Select Language: **English (default)

    1. **Select Voice: ***pick any*

![Source screenshot image50](../assets/images/updated-image50.png){ .lab-screenshot width="1100" loading="lazy" }

1. Generating the file takes a few seconds. When it’s ready, play the prompt to check it, then click **Save.**

![Source screenshot image51](../assets/images/updated-image51.png){ .lab-screenshot width="1100" loading="lazy" }

1. Your **Welcome Message **announcement is now in the announcement repository, marked **Text to speech**. Later you create an Auto Attendant and use it as its greeting.

![Source screenshot image52](../assets/images/updated-image52.png){ .lab-screenshot width="1100" loading="lazy" }

## Step 2: Create an office hours schedule

Schedules support several calling features, such as the Auto Attendant. A schedule sets time slots for each day of the week and weekend during which a feature behaves in a specific way. You create one **Business Hours** schedule for this lab.

1. In Collaboration Control Hub, under **MANAGEMENT**, click **Locations**, then select **dCloud**, the location where you create the schedule.

![Source screenshot image53](../assets/images/updated-image53.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click the **Calling** tab. Scroll down to the **Calling features settings** section and click **Schedules**.

![Source screenshot image54](../assets/images/updated-image54.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click **Add schedule**.

![Source screenshot image55](../assets/images/updated-image55.png){ .lab-screenshot width="1100" loading="lazy" }

1. For **Schedule name** enter OfficeHours, and for Schedule type select **Business Hours**.

1. Set the hours of operation to **07:00 AM to 11:00 PM** for **Monday to Friday**.

1. Leave **Sunday** and **Saturday** unchecked.

1. Uncheck **Lunch Break** at the bottom. Click **Save** when you're done.

![Source screenshot image56](../assets/images/updated-image56.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

The next screen shows the new **OfficeHours** schedule.

![Source screenshot image57](../assets/images/updated-image57.png){ .lab-screenshot width="1100" loading="lazy" }

## Step 3: Create an Auto Attendant

An **Auto Attendant** answers a call with a greeting and a menu, and sends the caller where they choose: "press 1 for…, press 2 for…". In this task you create the **SupportDeskIVR** Auto Attendant from scratch in Collaboration Control Hub. It plays the **Welcome Message** you created with text-to-speech, follows the **OfficeHours** schedule, and sends callers to the two support queues you create in the next task.

| **Setting** | **Value** |
| --- | --- |
| **Name** | SupportDeskIVR |
| **Extension** | 6500 |
| **Schedule** | OfficeHours |
| **Greeting** | Welcome Message (text-to-speech) |
| **Press 1** | Transfer to 6501 (Webex Calling Support queue) |
| **Press 2** | Transfer to 6502 (Webex Contact Center Support queue) |
| **Press 9** | Repeat the menu |
| **No input** | Repeat twice, then transfer to Anita Perez's voicemail |

<br>

1. In Collaboration Control Hub, go to **SERVICES &gt; Calling &gt; Features** and click **Add new** on the **Auto Attendant** card.

![Source screenshot image58](../assets/images/updated-image58.png){ .lab-screenshot width="1100" loading="lazy" }

1. The **Create Auto Attendant **wizard opens on the **Basics** page. Enter:

    - **Location:** dCloud

    - **Auto Attendant Name:** SupportDeskIVR

    - **Phone Number**: leave it blank, and enter **6500** for the **Extension**

    - Leave all the other settings at their defaults.

![Source screenshot image59](../assets/images/updated-image59.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click **Next**. On the **Business Schedule** page, select the **OfficeHours** schedule you created earlier. Click **Next**.

![Source screenshot image60](../assets/images/updated-image60.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Holiday Schedule** page, leave it empty and click **Next**.

![Source screenshot image61](../assets/images/updated-image61.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Menu** page, set up the **Business Hours** menu:

    - **Press 1: Transfer call with prompt**, to extension **6501**

    - **Press 2: Transfer call with prompt**, to extension **6502**

    - **Press 9: Repeat menu**

The keys match your greeting

These keys follow the **Welcome Message** you created with text-to-speech earlier. The greeting tells callers: *"If you need Webex Calling support, please press 1. If you need Webex Contact Center Support, please press 2. To repeat this menu, please press 9."* So:

- **1** goes to the Webex Calling Support queue (6501)

- **2** goes to the Webex Contact Center Support queue (6502)

- **9** plays the menu again

If you change the greeting text, change the menu keys to match.

The queues come next

Extensions 6501 and 6502 belong to the Customer Assist queues you will create next. If the Collaboration Control Hub doesn't let you select them yet, set up key **9** now, and come back to add keys **1** and **2** after creating the Queues.

![Source screenshot image63](../assets/images/updated-image63.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image64](../assets/images/updated-image64.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click **Next**. On the **Greeting** page, choose a **Custom greeting** and select the **Welcome Message** announcement you created with text-to-speech. Click **Next**.

![Source screenshot image65](../assets/images/updated-image65.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image66](../assets/images/updated-image66.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image67](../assets/images/updated-image67.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Review** page, check your settings and click **Create**.

![Source screenshot image68](../assets/images/updated-image68.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

## Step 4: Create the Queues

In this task you create the two Customer Assist queues in Collaboration Control Hub. They are where the Auto Attendant (keys 1 and 2) and, later, the AI Receptionist send callers who need help.

| **Queue name** | **Extension** | **Agents** | **Call routing** |
| --- | --- | --- | --- |
| Q1\_WebexCallingSupport | 6501 | Anita Perez, <br>Kellie Melby | Priority based, longest idle |
| Q2\_WebexContactCenterSupport | 6502 | Taylor Bard | Priority based, circular |

1. Go to **SERVICES &gt; Customer Assist**. Click the **Queues** tab, then **Add Queue**.

![Source screenshot image69](../assets/images/updated-image69.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Basics** page, enter:

- **Location**: dCloud

- **Queue name**: Q1\_WebexCallingSupport

- **Phone number**: leave it blank, and enter 6501 for the Extension

- **Dial by name**: Q1\_WebexCallingSupport

- **External caller ID phone number**: select **Location number**. This is the location's main number for your Webex tenant.

- Leave the other settings at their defaults, and click **Next**.

![Source screenshot image70](../assets/images/updated-image70.png){ .lab-screenshot width="1100" loading="lazy" }

1. For **Call routing**, choose **Priority based** with **Longest idle**, so each call goes to the agent who has been waiting longest. Click **Next**.

![Source screenshot image71](../assets/images/updated-image71.png){ .lab-screenshot width="1100" loading="lazy" }

1. Keep the default overflow and announcement settings, and click **Next** on each page until you reach **Agents**.

![Source screenshot image72](../assets/images/updated-image72.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image73](../assets/images/updated-image73.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Agents** page, search for and add **Anita Perez** and **Kellie Melby**. Click **Next**.

![Source screenshot image74](../assets/images/updated-image74.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image75](../assets/images/updated-image75.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Review** page, check your settings and click **Create**.

![Source screenshot image76](../assets/images/updated-image76.png){ .lab-screenshot width="1100" loading="lazy" }

1. Repeat \#1 to \#6 for the second queue, with these differences:

- **Queue name**: Q2\_WebexContactCenterSupport

- **Extension**: 6502

- **Dial by name**: Q2\_WebexContactCenterSupport

- **External caller ID phone number**: Location number

- **Call routing**: **Priority based** with **Circular**

- **Agents**: add only **Taylor Bard**. Don't add Anita Perez or Kellie Melby: they are agents in Q1 only.

![Source screenshot image77](../assets/images/updated-image77.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image78](../assets/images/updated-image78.png){ .lab-screenshot width="1040" loading="lazy" }

![Source screenshot image79](../assets/images/updated-image79.png){ .lab-screenshot width="854" loading="lazy" }

![Source screenshot image80](../assets/images/updated-image80.png){ .lab-screenshot width="786" loading="lazy" }

![Source screenshot image81](../assets/images/updated-image81.png){ .lab-screenshot width="1076" loading="lazy" }

![Source screenshot image82](../assets/images/updated-image82.png){ .lab-screenshot width="1058" loading="lazy" }

![Source screenshot image83](../assets/images/updated-image83.png){ .lab-screenshot width="1044" loading="lazy" }

1. Both queues are now on the Customer Assist **Queues** page: **Q1\_WebexCallingSupport** with extension **6501**, and **Q2\_WebexContactCenterSupport** with extension **6502**.

![Source screenshot image84](../assets/images/updated-image84.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

### Test the Auto Attendant

1. From the Webex App of your local machine, logged in as Charles Holland, dial **6500**.

1. You hear the greeting you created with text-to-speech: “*Welcome to the support help desk… *”. If you do not press anything, the menu repeats twice and the call goes to Anita’s voicemail.

**CALLING OUTSIDE OFFICE HOURS?**

The Auto Attendant follows the **OfficeHours** schedule you created earlier, and that schedule runs on the time zone of the **dCloud** location in the US (San Jose, California, US Pacific time). Depending on where in the world you're taking this lab, your call may land **outside** office hours, so you won't hear the business hours greeting and menu.

If that happens, open the schedule for the whole week:

1. Go to **MANAGEMENT &gt; Locations &gt; dCloud &gt; Calling &gt; Schedules**, and click **OfficeHours**.

1. Edit each day, **including Saturday and Sunday**, and set it to **All day**.

1. Click **Save**, then call 6500 again.

The office is now open 24/7, so every test call in the rest of the lab reaches the business hours menu.

<br>
