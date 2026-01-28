# Devon RFU Colts Administration Portal - Sign In

## 1. SIGN IN / LOGIN

**URL**: `/accounts/login/`

### Overview
The login page is the entry point to the Devon RFU Colts administration portal. All users must authenticate with their credentials before accessing the system.

### Page Layout
- Left panel: Bright green branding with application information and demo credentials
- Right panel: Login form

### Access Information

**Portal Name**: Devon RFU Colts  
**Description**: The official administration portal for Devon RFU Colts. Manage teams, players, fixtures, and more.

### Login Instructions

**Step-by-Step Process**:

1. Navigate to the login page at: `https://colts.tinotenda.co/accounts/login/`

2. Locate the login form on the right panel

3. Enter your credentials:
   - **Username Field**: Click the Username input box and enter your assigned username
   - **Password Field**: Click the Password input box and enter your password

4. Click the **Log In** button

5. Upon successful authentication, you will be redirected to the main dashboard (`/accounts/`)

### Form Fields

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| Username | Text input | Yes | Your assigned username |
| Password | Password input | Yes | Your account password (masked) |

### Login Redirect
After successful login, the system redirects users to: `/accounts/` (Home Dashboard)

### Account Types

**1. Super Admin**
- Full system access
- Can manage all clubs, seasons, leagues, and users
- Username: `superadmin`

**2. Club Admin**
- Club-level access only
- Can manage teams, players, matches for assigned club
- Username: `admin`
- Assigned to specific club (e.g., Barnstaple, Crediton)

### Security Notes
- Always log out when finished using the portal
- Do not share your login credentials
- Passwords are case-sensitive
- Demo credentials are for testing purposes only

### Troubleshooting

**"Login failed" message**:
- Verify username is entered correctly (case-sensitive)
- Verify password is entered correctly (case-sensitive)
- Ensure Caps Lock is not activated
- Try the demo credentials first if testing

**Access denied after login**:
- Your account may not have the required permissions for the requested resource
- Contact your system administrator
