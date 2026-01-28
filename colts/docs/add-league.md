# Devon RFU Colts Administration Portal - Add New League

## 9. ADD NEW LEAGUE FORM

**URL**: `/accounts/new_league/`

### Overview
The Add New League form allows administrators to create new competitions/leagues in the system.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts branding
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add New League"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: League Name**
- Type: Text input
- Required: Yes
- Purpose: Name of the competition/league
- Example: "Devon Colts North", "Devon Colts South", "Devon Cup"
- Character limit: Typically 100 characters

**Field 2: Age Group**
- Type: Text input or dropdown
- Required: Yes
- Purpose: Define age category for league
- Common values: U18, U16, U15, U14, U13, U12
- Example: "U18"

**Field 3: Gender**
- Type: Text input or dropdown
- Required: Yes
- Purpose: Define gender category
- Options: Male, Female, Mixed
- Example: "Male"

**Field 4: Season**
- Type: Dropdown selector
- Required: Yes
- Options: List of available seasons from system
- Default: "----------"
- Purpose: Link league to specific season
- Example: "2024/2025"

**Field 5: Notes**
- Type: Textarea (multi-line text)
- Required: No
- Purpose: Additional information about the league
- Example: "Demo league for northern clubs"
- Character limit: Typically 500 characters

### Form Actions

**Submit Button**: "Add League" or similar
- Saves new league to database
- Redirects to Manage Leagues page

### Instructions for Adding a League

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Home Dashboard → Click **New** under ACTIVE LEAGUES
   - OR from navigation → Club Management (if available)
   - OR go directly to `/accounts/new_league/`

2. **Enter League Name**:
   - Click in League Name field
   - Type descriptive league name
   - Use clear, consistent naming convention
   - Example: "Devon Colts North U18"

3. **Enter Age Group**:
   - Click Age Group field
   - Type or select age category
   - Use standard format (U + age)
   - Example: "U18"

4. **Select Gender**:
   - Click Gender field
   - Type or select from dropdown
   - Choose: Male, Female, or Mixed
   - Example: "Male"

5. **Select Season**:
   - Click Season dropdown
   - Select appropriate season from list
   - Must select existing season
   - Example: "2024/2025"

6. **Add Notes** (Optional):
   - Click in Notes field
   - Enter descriptive information
   - Explain league purpose, region, or special rules
   - Example: "Regional league for clubs in North Devon"

7. **Submit Form**:
   - Review all entries
   - Click submit button
   - System validates entries
   - Redirects to Manage Leagues page
   - New league appears in list

### Validation Rules

**League Name**:
- Cannot be empty
- Should be unique (avoid duplicates)
- Use clear, descriptive names

**Age Group**:
- Must follow standard format
- Common: U12, U13, U14, U15, U16, U18

**Gender**:
- Must be one of: Male, Female, Mixed
- Required field

**Season**:
- Must select from dropdown
- Cannot leave as "----------"
- Season must exist in system

### League Naming Best Practices

**Good League Names**:
- "Devon Colts North U18"
- "Devon Colts South U18"
- "Devon Cup U16"
- "Devon Championship U18"

**Include in Name**:
- Geographic area (North/South/East/West)
- Age group (if multiple age groups exist)
- Competition type (League/Cup/Championship)

### After Creation

**Next Steps**:
- League appears in Manage Leagues list
- Available in dropdown selectors for fixtures
- Teams can be assigned to league
- Fixtures can be scheduled in this league
- League table can be generated

### Use Cases

**When to Create New League**:
- Starting new season with different divisions
- Creating cup competitions
- Separating age groups
- Dividing regions (North/South)
- Creating friendly leagues

### Troubleshooting

**Form won't submit**:
- Verify all required fields completed
- Check season dropdown is not "----------"
- Ensure league name is entered
- Check for duplicate league names

**Season dropdown is empty**:
- No seasons exist in system
- Create season first (see Add New Season)
- Refresh page after creating season

### Navigation

**To Access Form**:
- Home Dashboard → New button (ACTIVE LEAGUES panel)
- Manage Leagues → ADD NEW LEAGUE button
- Direct URL: `/accounts/new_league/`

**To Cancel**:
- Click browser back button
- Navigate to Home or Manage Leagues
