# Devon RFU Colts Administration Portal - Add Club Admin

## 14. ADD CLUB ADMIN FORM

**URL**: `/accounts/add_new/`

### Overview
The Add Club Admin form allows system administrators to create new user accounts for club administrators in the portal.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts branding
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add Club Admin"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: Username**
- Type: Text input
- Required: Yes
- Purpose: Unique login identifier
- Format: Alphanumeric, no spaces
- Character limit: Typically 30 characters
- Example: "jsmith", "admin_exeter"
- Note: Must be unique in system

**Field 2: First Name**
- Type: Text input
- Required: Yes
- Purpose: User's first/given name
- Format: Standard text
- Character limit: Typically 50 characters
- Example: "John"

**Field 3: Last Name**
- Type: Text input
- Required: Yes
- Purpose: User's surname/family name
- Format: Standard text
- Character limit: Typically 50 characters
- Example: "Smith"

**Field 4: Email**
- Type: Email input
- Required: Yes
- Purpose: User's email address for communications
- Format: Valid email format (user@domain.com)
- Validation: Must be valid email format
- Example: "john.smith@example.com"
- Note: Used for password resets and notifications

**Field 5: Password**
- Type: Password input
- Required: Yes
- Purpose: Initial login password
- Format: Masked/hidden text
- Requirements:
  - Minimum length (typically 8+ characters)
  - May require mix of upper/lowercase
  - May require numbers
  - May require special characters
- Example: "SecurePass123!"
- Note: User should change on first login

**Field 6: Select Club**
- Type: Dropdown selector
- Required: Yes
- Options: List of all teams/clubs in system
- Purpose: Assign admin to specific club
- Example: "Barnstaple (U18, Male)"
- Note: Determines which team the admin can manage

### Form Actions

**Submit Button**: "Add Club Admin"
- Creates new user account
- Sends welcome email (if configured)
- Redirects to user management page or home
- New admin appears in Club Admins table

### Instructions for Adding a Club Admin

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Home Dashboard → Click **Add** in CLUB ADMINS section
   - OR go directly to `/accounts/add_new/`
   - Note: Typically requires super admin permissions

2. **Enter Username**:
   - Click Username field
   - Create unique login identifier
   - Use lowercase letters and numbers
   - No spaces allowed
   - Example: "jsmith" or "exeter_admin"

3. **Enter First Name**:
   - Click First Name field
   - Type user's first name
   - Use proper capitalization
   - Example: "John"

4. **Enter Last Name**:
   - Click Last Name field
   - Type user's last name
   - Use proper capitalization
   - Example: "Smith"

5. **Enter Email**:
   - Click Email field
   - Type valid email address
   - Format: user@domain.com
   - Double-check for typos
   - Example: "john.smith@example.com"

6. **Create Password**:
   - Click Password field
   - Create secure initial password
   - Follow password requirements
   - Note password to share with user securely
   - Example: "TempPass2024!"
   - User should change on first login

7. **Select Club**:
   - Click Select Club dropdown
   - Scroll through club list
   - Select appropriate club/team
   - Admin will manage this club only
   - Example: Select "Barnstaple (U18, Male)"

8. **Submit Form**:
   - Review all entries for accuracy
   - Ensure email is correct
   - Verify correct club selected
   - Click "Add Club Admin" button
   - System validates entries
   - Creates user account
   - Redirects to admin management page
   - New admin appears in Club Admins table

### Validation Rules

**Username**:
- Cannot be empty
- Must be unique (not already in use)
- Alphanumeric characters only
- No spaces allowed
- Typically 3-30 characters

**Names**:
- Cannot be empty
- Standard text characters
- Use proper capitalization

**Email**:
- Must be valid email format
- Must contain @ symbol
- Must have domain extension
- Should be unique (best practice)

**Password**:
- Cannot be empty
- Minimum length requirement
- May require complexity (uppercase, numbers, symbols)
- Case-sensitive

**Club Selection**:
- Must select from dropdown
- Cannot be empty
- Determines admin's access level

### Password Requirements

**Typical Password Rules**:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$%^&*)
- No common passwords (password123, etc.)

**Good Password Examples**:
- "Secure123!"
- "Rugby2024#"
- "Admin@Pass2024"

### User Permissions

**Club Admin Access**:
- Manage own club's players
- Add/edit fixtures for own club
- Record match results for own club
- View own club's league standings
- Cannot access other clubs' data
- Cannot create seasons or leagues (typically)

**Super Admin Access** (for reference):
- All club admin permissions
- Manage all clubs
- Create/edit seasons
- Create/edit leagues
- Manage all users
- System-wide settings

### After Account Creation

**Next Steps**:
1. Share login credentials with new admin securely
2. Provide portal URL: `https://colts.tinotenda.co/accounts/login/`
3. Share username and temporary password
4. Instruct user to change password on first login
5. Provide basic training/documentation

**New Admin Can Now**:
- Log in to portal
- View club dashboard
- Add players to roster
- Schedule fixtures
- Record match results
- Manage team information

### Account Information to Share

**Provide to New Admin**:

- Portal URL: https://colts.tinotenda.co/accounts/login/
- Username: [username created]
- Temporary Password: [password created]
- Assigned Club: [club name]


### Security Best Practices

**When Creating Accounts**:
- Use strong temporary passwords
- Share credentials securely (not via email if possible)
- Require password change on first login
- Use work email addresses when possible
- Document who has admin access
- Review admin accounts regularly

**Account Management**:
- Remove accounts for users who leave
- Update email addresses when changed
- Reset passwords if compromised
- Audit admin actions periodically

### Common Use Cases

**When to Create Club Admin**:
- New club joining the system
- New volunteer taking over admin role
- Additional admin for large club
- Replacing departed admin
- Season start preparation

**Multiple Admins Per Club**:
- System may allow multiple admins per club
- Useful for larger clubs
- Backup admin if primary unavailable
- Different roles (fixtures vs players)

### Troubleshooting

**Form won't submit**:
- Verify all required fields completed
- Check username is not already in use
- Ensure email format is valid
- Verify password meets requirements
- Confirm club is selected from dropdown

**Username already exists**:
- Try different username
- Add numbers or club name to username
- Check if account already exists for this person
- Contact administrator if needed

**Email invalid error**:
- Check for typos
- Ensure @ symbol present
- Verify domain is correct (.com, .co.uk, etc.)
- No spaces in email address

**Password rejected**:
- Check minimum length requirement
- Add uppercase letters
- Add numbers
- Add special characters (!@#$%^&*)
- Try more complex password

**Club dropdown empty**:
- No clubs exist in system
- Create clubs first (see Add New Team)
- Refresh page
- Contact system administrator

### Navigation

**To Access Form**:
- Home Dashboard → CLUB ADMINS section → Add button
- User management page → Add User button
- Direct URL: `/accounts/add_new/`
- Note: Requires admin permissions

**To Cancel**:
- Click browser back button
- Navigate to Home Dashboard
- Account not created if form not submitted

### Related Functions

**User Management**:
- Edit User → Modify admin details
- Delete User → Remove admin account
- Reset Password → Send password reset email
- View Admins → See all club administrators
