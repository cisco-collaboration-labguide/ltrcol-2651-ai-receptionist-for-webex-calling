# Task 3: AI Receptionist Configuration

In this task you will configure a Knowledge Base for an AI Receptionist and then configure the AI Receptionist to answer frequently asked questions using the info in the Knowledge Base. And for items the AI Receptionist cannot handle, have it route the call to a user who can help the caller.

## Step 1: Accessing the AI Receptionist in Control Hub

1. In Collaboration Control Hub, click SERVICES &gt; Calling.

1. Select the **AI Receptionist** tab from the top menu.

![Source screenshot image20](../assets/images/updated-image20.png){ .lab-screenshot width="1100" loading="lazy" }

1. You will see screen below.

![Source screenshot image21](../assets/images/updated-image21.png){ .lab-screenshot width="1100" loading="lazy" }

You have three options to create the **AI Receptionist** and the **Knowledge Base** it will use to answer frequently asked questions.

\#1 – Create a **Knowledges Base** when you are creating the **AI Receptionist**

\#2 – Create the **AI Receptionist** first and create the **Knowledge Base** later

\#3 – Create the **Knowledge Base** first and assign it to the **AI Receptionist** when you create it.

We will use **Option \#3** (create the Knowledge Base first and assign it to the AI Receptionist when you create it) for this lab.

<br>

## Step 2: Setting Up the Knowledge Base

In this step you will create a **Knowledge Base** and add information to it that will be used by the AI Receptionist to interact with the caller and answer commonly asked questions.

1. Click on the **Knowledge Base** tab

1. On the **Knowledge Base** page, click **Create knowledge base** or **Create** to create a new knowledge base.

![Source screenshot image22](../assets/images/updated-image22.png){ .lab-screenshot width="1100" loading="lazy" }

!!! note

    **Note:  **
    Sometimes it can take up to 30+ minutes to add files to a knowledge base. This is a known caveat engineering is working on.
    You won’t be using it for a while so if needed you can proceed with the rest of the lab and come back later to verify it is configured.

1. For the **Knowledge base name** enter “*AI By Design **Solutions*” and “*FAQ*” for the **Description**. You can add more details if you would like it for your future reference.

1. Click **Create**

![Source screenshot image23](../assets/images/updated-image23.png){ .lab-screenshot width="714" loading="lazy" }

1. Once added you should see the new **Knowledge Base** with “0” files. Now you will add some files to it.

![Source screenshot image24](../assets/images/updated-image24.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click on the **AI By Design Solutions **knowledge base to open it so you can add files.

1. In this lab we have provided text files to help create the Knowledge Base. Double click the **WxC AIR Files** folder on **Workstation 1’s** Desktop.

![Source screenshot image25](../assets/images/updated-image25.png){ .lab-screenshot .lab-compact width="222" loading="lazy" }

1. In this folder right clicking the file **AI By Design Solutions-KB.txt** and select *Edit with Notepad++* to open the file.<br><br>Please take a moment to review the Questions and Answers in the file.

![Source screenshot image26](../assets/images/updated-image26.png){ .lab-screenshot width="1100" loading="lazy" }

!!! note

    **Note:**
    In a real-world scenario make sure you build your own Knowledge Base document as per the accurate business workflow and call flow requirements to train the agent. This is the most critical part in making efficient use of the AI Receptionist.
    The supported file types are:
    File types: PDF, DOCX, TXT, XLSX, XLS, CSV
    File size limits: TXT up to 2 MB; all other formats up to 10 MB

![Source screenshot image27](../assets/images/updated-image27.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **AI By Design Solutions Knowledge Base** configuration page, click the **Add** button to add files to it.

    ![Source screenshot image28](../assets/images/updated-image28.png){ .lab-screenshot width="1100" loading="lazy" }

1. On the **Upload** tab, click *Choose a file*. You can also drag and drop files to add them.

![Source screenshot image29](../assets/images/updated-image29.png){ .lab-screenshot width="1100" loading="lazy" }

The information in the files that are added is used by the AI Receptionist to help answer FAQs for callers. You may notice there is also an option for **Create**, which we will use later in the lab.

1. Select the file ***AI By Design Solutions**-KB.txt*** from the **WxC AIR Files** folder on **Workstation 1’s** Desktop and click ‘***Open*’**.

![Source screenshot image30](../assets/images/updated-image30.png){ .lab-screenshot width="1100" loading="lazy" }

1. Verify the file you selected and click ‘***Add*’** to upload the file to the Knowledge Base

![Source screenshot image31](../assets/images/updated-image31.png){ .lab-screenshot width="1100" loading="lazy" }

1. A confirmation toast notification will appear at the bottom right of the screen once the upload is complete.<br><br>You can verify your file has been added successfully by checking that it is listed as a file under the **AI By Design Solutions** Knowledge Base as shown below.

![Source screenshot image32](../assets/images/updated-image32.png){ .lab-screenshot width="1100" loading="lazy" }

1. Now instead of uploading a doc, you will create a text-based document to add to the Knowledge Base. On the **AI By Design Solutions Knowledge Base** page, click ‘***Add’***.

![Source screenshot image33](../assets/images/updated-image33.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

1. Click on ‘***Create*’** tab and enter the following details:

- **Name** = AfterHour\_Rates

- **Knowledge Base Content** type or copy/paste the text below the dashed lines ---------

Alternatively, you can use the file “*AI Receptionist Config-KB.txt*” that is in the **WxC AIR Files** folder on **Workstation 1’s** Desktop to copy/paste the text after the heading **Document Content:** into the configuration. Open it use Notepad++

---------------------------------------------------------------

1. Hourly Service Fee

- $300 an hour

2. Warranty Pricing

Prices below are the list price of the warranties before contract negotiation.

- 1 year warranty - $2,500 a month

- 3 year warranty - $2,250 a month

- 5 year warranty - $2,000 a month

3. After Hours

- **AI By Design Solutions**' technicians are available by appointment only after 5pm and on select weekends. Please check with a service support agent about scheduling an appointment.

---------------------------------------------------------------

![Source screenshot image34](../assets/images/updated-image34.png){ .lab-screenshot width="1100" loading="lazy" }

![Source screenshot image35](../assets/images/updated-image35.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click ‘***Add*’** to save the new document in the Knowledge Base.

![Source screenshot image36](../assets/images/updated-image36.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

1. Now you should see two files under the **AI By Design Solutions** Knowledge Base:

- File based

- Article based

![Source screenshot image37](../assets/images/updated-image37.png){ .lab-screenshot width="1100" loading="lazy" }

!!! note

    **Note:**
    If you see a continuous spinning circle next to the file name and the following toast notification, then the file creation process is taking longer to complete (which is a known caveat):
    Give it a couple of minutes and then try refreshing the browser and see if the file has completed the upload process
    If that does not work, proceed with the rest of the AI Receptionist configuration and come back later to check
    ![Source screenshot image38](../assets/images/updated-image38.png){ .lab-screenshot .lab-compact width="512" loading="lazy" }

1. If you click on the ‘***Knowledge Base***’ link at the top left of the page, you will see there are now 2 files in the **AI By Design Solutions Knowledge Base**, but the Knowledge Base is not **Assigned** to an AI Receptionist yet.

![Source screenshot image39](../assets/images/updated-image39.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

## Step 3: Configuring AI Receptionist

Now you will configure the AI Receptionist and associate the Knowledge Base you created with it.

1. Go to **SERVICES &gt; Calling** and click the **AI Receptionist** tab at the top of the page, then the **AI Receptionists** tab.

1. On the **AI Receptionists** page, click **Create** or **Create AI receptionist** to set up a new AI Receptionist.

![Source screenshot image40](../assets/images/updated-image40.png){ .lab-screenshot width="1100" loading="lazy" }

### General Settings

1. On the General settings window, use the following configuration:

1. **Location** = “**dCloud**” *(from the dropdown menu)*

1. **AI Receptionist Name** = **"AI By Design Solutions"** *(unique name)*

1. **Phone Number** = leave it blank, and enter **6023** for the **Extension**

1. **AI Engine **= “**Webex AI Pro 1.0***”*

1. **Language and voice** *(feel free to pick your own language and voice from the options)*

    1. **AI receptionist language **= “English (Australia)*”*

    1. **AI receptionist voice** = “Amelia”

1. **Direct line caller ID name** = select ‘Display name: **AI By Design Solutions**’

1. **Dial by name** = “**AI By Design Solutions**”

![Source screenshot image41](../assets/images/updated-image41.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click **Next** to proceed.

<br>

### Receptionist Guidelines

1. This is a very importation configuration, where you are defining how your AI Receptionist will interact with the callers. On the **Receptionist guidelines** page you will see there are various templates for popular vertical use uses. You can leverage them, but it is highly recommended to review and revise them based on your own business requirements.

![Source screenshot image42](../assets/images/updated-image42.png){ .lab-screenshot width="1100" loading="lazy" }

<br>

1. For the lab you will use the **Receptionist Guidelines** below to simplify the configuration. Please review this information and enter this info into the configuration.

Alternatively, you can use the file “***AI Receptionist Config-KB.txt***” that is in the **WxC AIR Files** folder on **Workstation 1’s Desktop**. Open this file and copy/paste the text into the configuration. Make sure to delete any extra blank characters at the end of the copied line.

---------------------------------------------------------------------

    1. **Receptionist's/Agent’ goal: **

As the AI Receptionist for **AI By Design Solutions**, your role is to assist callers by providing accurate information about our services, answering basic inquiries, and professionally redirecting calls to the right support team or the designated operator when needed. Always maintain a polite, professional, and approachable tone to ensure a positive caller experience.

    1. **Welcome Message:**

Hello, thank you for calling **AI By Design Solutions**. How can I assist you today?

    1. **Instructions/Receptionist Guidelines:**

1.Identity

-Role Definition: You are a friendly, professional assistant dedicated to handling incoming calls for **AI By Design Solutions**.

-Your primary responsibilities include answering basic questions about our services, routing calls to support agents and managing appointment scheduling.

-Tone and Demeanor: Maintain a polite, empathetic, and patient tone throughout the interaction to ensure callers feel valued and understood.

2.Context

-Background Information:

-Use only the information provided to you to respond to callers.

-For appointment scheduling or cancellation requests, you may transfer callers to the default action number for setup or cancellation.

-If callers have intents beyond scheduling, asking basic questions or needing to work with a support agent, inform them politely that you don't handle other inquiries, but that you can transfer them to the appropriate team.

-Advise callers that they will need to repeat their queries to the scheduler after transfer.

3. Additional Guardrails

-Scope Limitation: Do not attempt to answer questions outside your defined scope (basic service queries, sending calls to support teams and appointment management).

-Transfer Protocol: Always confirm with the caller before transferring the call.

-Caller Verification: If applicable, verify caller identity before processing appointment changes.

-Error Handling: If caller input is unclear or ambiguous, politely ask for clarification or repetition.

-Privacy and Compliance: Do not disclose any sensitive or personal information unless authorized.

-Fallback Responses: If unable to assist, provide a courteous default response and offer transfer to a human agent.

-Conversation Closure: Always end calls with a polite closing statement, thanking the caller for contacting **AI By Design Solutions**.

---------------------------------------------------------------------

![Source screenshot image43](../assets/images/updated-image43.png){ .lab-screenshot width="749" loading="lazy" }

![Source screenshot image44](../assets/images/updated-image44.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click **Next**

<br>

### Knowledge Base

1. Select the **Knowledge Base** “***AI By Design Solutions***” that you created in the previous step and click ‘*Next*’.

![Source screenshot image45](../assets/images/updated-image45.png){ .lab-screenshot width="1100" loading="lazy" }

1. Click ‘**Next’**

### Default Action

1. For the Default action, use the following settings. This is for when a caller requests to connect to a human agent or the AI Receptionist is unable to assist with the caller’s request. It can also be triggered in specific situations based on the AI Receptionist’s instructions.

    1. **Action** = select “*Transfer call*” from drop down

    1. **Contact type** = select ‘*Number*’

    1. **Enter phone number** = “*6017*”, which is Anita Perez’s extension number

![Source screenshot image46](../assets/images/updated-image46.png){ .lab-screenshot width="1083" loading="lazy" }

1. Click **Review**

### Review and Creation

1. On the **Review** page, carefully verify all configured settings across the General Settings, Receptionist guidelines, Knowledge base, and Default action tabs.

1. If any changes are needed, you can navigate back to the appropriate step and update them.

1. Once satisfied, click ‘**Create’** to finish creating the AI Receptionist.

![Source screenshot image47](../assets/images/updated-image47.png){ .lab-screenshot width="960" loading="lazy" }

1. You will see the message “**AI Receptionist was created successfully**”. Click ‘**Close’**. You will add Intents later in the lab after you create the Customer Assist queues.

![Source screenshot image48](../assets/images/updated-image48.png){ .lab-screenshot width="956" loading="lazy" }

**You are done configuring AI Receptionist. You will test and verify it later in the lab.**

<br>
