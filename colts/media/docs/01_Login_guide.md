# 1. Sign In / Login Guide

**URL:** `/accounts/login/`

## Overview
The login page is the secure entry point to the Devon RFU Colts administration portal. All users must authenticate with their valid credentials before accessing any system features.



## Page Layout
* **Left Panel:** Bright green branding containing application information and demo credentials.
* **Right Panel:** The secure Login form.

## Access Information
* **Portal Name:** Devon RFU Colts
* **Description:** The official administration portal for Devon RFU Colts used to manage teams, players, fixtures, and more.

## Login Instructions

1.  **Navigate:** Go to the login page at `https://colts.tinotenda.co/accounts/login/`.
2.  **Locate:** Find the login form on the right-hand panel.
3.  **Enter Username:** Click the **Username** input box and enter your assigned username.
4.  **Enter Password:** Click the **Password** input box and enter your password.
5.  **Submit:** Click the **Log In** button.

> **Note:** Upon successful authentication, you will be automatically redirected to the **Home Dashboard** (`/accounts/`).

## Form Fields Reference

| Field | Type | Required | Notes |
| :--- | :--- | :--- | :--- |
| **Username** | Text input | Yes | Your assigned unique username. |
| **Password** | Password input | Yes | Your account password (characters are masked). |

## Account Types & Permissions

### 1. Super Admin (`superadmin`)
* **Access:** Full system access.
* **Capabilities:** Can manage all clubs, seasons, leagues, and users.

### 2. Club Admin (`admin`)
* **Access:** Club-level access only.
* **Capabilities:** Can manage teams, players, and matches for their assigned club (e.g., Barnstaple, Crediton).

## Security Best Practices
* Always **log out** when you are finished using the portal.
* Do not share your login credentials with unauthorized personnel.
* Remember that passwords are **case-sensitive**.

## Troubleshooting

| Issue | Potential Solution |
| :--- | :--- |
| **"Login failed" message** | • Verify username is correct (check casing).<br>• Verify password is correct (check casing).<br>• Ensure **Caps Lock** is off.<br>• Try the demo credentials to verify system status. |
| **Access denied after login** | • Your account may not have permissions for the specific resource.<br>• Contact your system administrator. |