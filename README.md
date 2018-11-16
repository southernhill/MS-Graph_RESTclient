# Microsoft Graph - Python3 REST client

Copyright 2018 SouthernHill and contributors. https://southernhill.nl

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

This repository holds a very undressed version of client code which can be used to query Microsoft Graph.
A non textbook definition of MS Graph is that Graph provides RESTful API services in order to integrate Office365 services into your own application.
We created this code based on a Stack Overflow discussion about the fact that Microsoft is quite vague on how to authenticate and manage authorization with MS Graph[[1]](https://stackoverflow.com/questions/46259183/authentication-in-outlook-365-api).
It should however be noted that Microsoft provides a [[web based GUI]](https://developer.microsoft.com/en-us/graph/graph-explorer#) that helps you test queries. However, the tool doesn't allow you to request tokens.

## Create application & set permissions

Before this code can interact with MS Graph, you first need to create an application in Office365. This can be done over [[here]](https://apps.dev.microsoft.com/).
The code currently only supports password based authentication. Therefore, if you're going to use the code you can only use password based authentication.
You also need to set the correct permissions. The required application permissions for Microsoft Planner can be found in the API documentation [[2]](https://developer.microsoft.com/en-us/graph/docs/api-reference/beta/api/plannerplan_list_tasks).
If the permissions require admin consent you can apply consent inside the Azure Active Directory console of Office365. The exact steps are: Azure Active Directory > App registrations (Preview) > applicationname > API permissions > Grant admin consent for TENANT).
Please note that the "Grant admin consent" can be found as a button at the bottom of the API permissions page.

A really useful tool we discovered during the creation of this client is the debugger on the website of JWT: https://jwt.io/. This tool allows you to decode encoded JSON Web Tokens.

## Modify tenant name

Before actually using the script modify the script with the following values:

* Replace `"TENANT"` with the name of the tenant of your Azure Active directory.
* Replace `"TENANT.TLD"` with the name of the tenant (including the TLD). This can be found in the Azure Active directory admin console.
* Replace `"APP_ID"` with the Application ID of the created application.
* Replace `"SECRET"` with the password of the created application. 
