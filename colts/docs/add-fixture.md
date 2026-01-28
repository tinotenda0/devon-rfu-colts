# Devon RFU Colts Administration Portal - Add New Fixture

## 12. ADD NEW FIXTURE FORM

**URL**: `/accounts/new_fixture/`

### Overview
The Add New Fixture form allows administrators to schedule upcoming matches between teams in the system.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts information
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add New Fixture"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: League**
- Type: Dropdown selector
- Required: Yes
- Default: "----------"
- Options: List of active leagues in system
- Purpose: Assign fixture to specific competition
- Example: "Devon Colts North", "Devon Colts South"

**Field 2: Season**
- Type: Dropdown selector
- Required: Yes
- Default: "----------"
- Options: List of active seasons
- Purpose: Link fixture to season year
- Example: "2024/2025"

**Field 3: Date**
- Type: Date picker
- Required: Yes
- Format: dd/mm/yyyy
- Input method: Click to open calendar picker
- Purpose: Select match date
- Example: "15/09/2024"

**Field 4: Time**
- Type: Time picker
- Required: Yes
- Format: HH:MM (24-hour format)
- Default: "--:--"
- Input method: Click to open time selector
- Purpose: Set kickoff time
- Example: "14:30" (2:30 PM)

**Field 5: Venue**
- Type: Text input
- Required: Yes
- Purpose: Match location/ground name
- Character limit: Typically 200 characters
- Example: "Recreation Ground, Barnstaple"

### Additional Fields (requires scrolling)

**Field 6: Home Team**
- Type: Dropdown selector
- Required: Yes
- Options: List of all teams in system
- Purpose: Select home team
- Example: "Barnstaple"

**Field 7: Away Team**
- Type: Dropdown selector
- Required: Yes
- Options: List of all teams in system
- Purpose: Select away/visiting team
- Example: "Bideford"
- Validation: Cannot be same as Home Team

**Field 8: Notes** (Optional)
- Type: Textarea
- Required: No
- Purpose: Additional fixture information
- Example: "Cup semi-final", "Rearranged fixture"

### Form Actions

**Submit Button**: "Add Fixture" or "Create Fixture"
- Saves fixture to database
- Fixture appears in match listings
- Redirects to fixtures page or dashboard

### Instructions for Adding a Fixture

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Home Dashboard → Club Management → Add Fixture
   - OR from Club Admin Dashboard → Add New Fixture button
   - OR go directly to `/accounts/new_fixture/`

2. **Select League**:
   - Click League dropdown
   - Select appropriate competition
   - Must choose league before proceeding
   - Example: Select "Devon Colts North"

3. **Select Season**:
   - Click Season dropdown
   - Select current season
   - Typically matches current rugby season
   - Example: Select "2024/2025"

4. **Choose Date**:
   - Click Date field
   - Calendar picker opens
   - Navigate to desired month/year
   - Click on specific date
   - Date populates in dd/mm/yyyy format
   - Example: Select September 15, 2024 → "15/09/2024"

5. **Set Time**:
   - Click Time field
   - Time picker opens
   - Select hours and minutes
   - Use 24-hour format
   - Example: 14:30 for 2:30 PM kickoff

6. **Enter Venue**:
   - Click Venue field
   - Type full ground/location name
   - Include town/area if helpful
   - Example: "Memorial Ground, Exeter"

7. **Select Home Team**:
   - Click Home Team dropdown
   - Scroll through team list
   - Select team playing at home
   - Example: "Barnstaple"

8. **Select Away Team**:
   - Click Away Team dropdown
   - Select visiting team
   - Must be different from Home Team
   - Example: "Bideford"

9. **Add Notes** (Optional):
   - Click Notes field
   - Enter any additional information
   - Examples:
     - "Rescheduled from 01/09"
     - "Cup quarter-final"
     - "Derby match"

10. **Submit Form**:
    - Review all entries
    - Ensure Home and Away teams are different
    - Verify date and time are correct
    - Click submit button
    - System validates entries
    - Redirects to match listings
    - Fixture appears in calendars

### Validation Rules

**League**:
- Must select from dropdown
- Cannot be "----------"
- Must be active league

**Season**:
- Must select from dropdown
- Cannot be "----------"
- Should match current or future season

**Date**:
- Must be valid date format
- Should be future date (for new fixtures)
- Cannot be empty

**Time**:
- Must be valid time format (HH:MM)
- Typically during daylight hours
- Common kickoff times: 10:00, 11:00, 14:00, 14:30, 15:00

**Venue**:
- Cannot be empty
- Should be descriptive location

**Teams**:
- Home and Away must be different
- Both teams must exist in system
- Both fields required

### Match Scheduling Best Practices

**Typical Kickoff Times**:
- Morning matches: 10:00, 10:30, 11:00
- Afternoon matches: 14:00, 14:30, 15:00
- Avoid evening kickoffs for youth rugby

**Venue Information**:
- Include ground name
- Include town/city
- Add postcode if helpful for navigation
- Example: "The Recreation Ground, Barnstaple, EX32 8DP"

**Scheduling Considerations**:
- Check team availability
- Avoid school holidays if possible
- Consider travel distances
- Check for fixture clashes
- Coordinate with referee availability

### After Creation

**Next Steps**:
- Fixture appears in match listings
- Visible on Home Dashboard (recent matches)
- Teams can view upcoming fixtures
- Can add result after match played
- Can edit fixture details if needed
- Can delete if fixture cancelled

**Fixture Visibility**:
- Home Dashboard → Matches section
- Club Admin Dashboard → Club Matches section
- Public fixtures page (if available)
- Team-specific fixture lists

### Common Use Cases

**When to Create Fixtures**:
- Season start: Create full fixture list
- Mid-season: Add cup/playoff fixtures
- Rescheduling: Create replacement fixture
- Friendly matches: Add non-league fixtures

**Bulk Fixture Creation**:
- Create entire season's fixtures at start
- Use consistent time slots
- Ensure home/away balance
- Consider derby dates

### Troubleshooting

**Form won't submit**:
- Verify all required fields completed
- Check League and Season dropdowns are selected (not "----------")
- Ensure Home and Away teams are different
- Verify date format is correct
- Check time is in valid format

**Teams dropdown empty**:
- No teams created in system yet
- Create teams first (see Add New Team)
- Refresh page after creating teams

**Date picker not working**:
- Try typing date manually in dd/mm/yyyy format
- Check browser compatibility
- Clear browser cache
- Try different browser

**Cannot select future date**:
- Check calendar year is correct
- Navigate to future month using arrows
- Ensure date restrictions aren't in place

### Navigation

**To Access Form**:
- Home Dashboard → Club Management menu → Add Fixture
- Club Admin Dashboard → Add New Fixture button
- Direct URL: `/accounts/new_fixture/`

**To Cancel**:
- Click browser back button
- Navigate to Dashboard
- Fixture not saved if form not submitted

### Related Forms

**After Fixture Created**:
- Use Add New Result form to record match outcome
- Use Edit Fixture to modify details
- Use Delete to cancel fixture
