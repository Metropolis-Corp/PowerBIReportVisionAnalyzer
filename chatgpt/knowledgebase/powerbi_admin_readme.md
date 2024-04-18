# README.md for ChatWithPowerBI App Registration

## Overview

This document provides a step-by-step guide for the ChatWithPowerBI app registration within Azure, detailing the necessary configurations for Azure App Registration, OAuth endpoints, and permissions required for the application to function correctly. This guide is intended for developers and administrators who need to understand or replicate the app registration process for ChatWithPowerBI.

## Azure App Registration Details

- **Application Name:** [Application Name]
- **Client ID:** [Client ID]
- **Tenant ID:** [Tenant ID]
- **Object ID:** [Object ID]
- **Tenant Domain:** [Tenant Domain]
- **App Instance ID:** [App Instance ID]
- **Location:** [Azure Region]

## OAuth 2.0 Endpoints

### Version 2 Endpoints

- **Authorization Endpoint (v2):** [Authorization Endpoint URL for OAuth2 v2]
- **Token Endpoint (v2):** [Token Endpoint URL for OAuth2 v2]

### Version 1 Endpoints

- **Authorization Endpoint (v1):** [Authorization Endpoint URL for OAuth2 v1]
- **Token Endpoint (v1):** [Token Endpoint URL for OAuth2 v1]

## Other Relevant Endpoints

- **OpenID Connect Metadata Document:** [URL for OpenID Connect Metadata Document]
- **Microsoft Graph API Endpoint:** `https://graph.microsoft.com`
- **Federation Metadata Document:** [URL for Federation Metadata Document]
- **WS-Federation Sign-on Endpoint:** [URL for WS-Federation Sign-on]
- **SAML-P Sign-on/Sign-out Endpoints:** [URL for SAML-P Sign-on/Sign-out]

## Configured Permissions

### Microsoft Graph Permissions

- **offline_access:** Maintain access to data you have given it access to.
- **openid:** Sign users in.
- **profile:** View users' basic profile.
- **User.Read:** Sign in and read user profile.
- **User.ReadBasic.All:** Read all users' basic profiles.

### Power BI Service Permissions

- **Dataset.Read.All:** View all datasets.
- **Dataset.ReadWrite.All:** Read and write all datasets.
- **Notebook.Read.All:** Read permissions on all notebooks.
- **PaginatedReport.Read.All:** Read permissions on all paginated reports.
- **Report.Read.All:** Read permissions on all reports.
- **SemanticModel.Execute.All:** Execute permissions on all semantic models.
- **SemanticModel.Read.All:** Read permissions on all semantic models.
- **SemanticModel.ReadWrite.All:** Read and write permissions on all semantic models.
- **SemanticModel.Reshare.All:** Reshare permissions on all semantic models.
- **Workspace.Read.All:** View all workspaces.
- **Workspace.ReadWrite.All:** Read and write all workspaces.

## Conclusion

This README provides a comprehensive overview of the ChatWithPowerBI app registration process in Azure, including detailed configurations and permissions required for the application. Developers and administrators should use this guide as a reference to ensure the correct setup for the ChatWithPowerBI integration with Azure and Power BI services.
