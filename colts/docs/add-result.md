# Devon RFU Colts Administration Portal - Add New Result

## 13. ADD NEW RESULT FORM

**URL**: `/accounts/new_result/`

### Overview
The Add New Result form allows administrators to record match outcomes and scores for completed fixtures.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts branding
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add New Result"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: Match**
- Type: Dropdown selector
- Required: Yes
- Default: "----------"
- Options: List of fixtures without results
- Format: Displays as "Home Team vs Away Team (Date)"
- Purpose: Select which fixture to add result for
- Example: "Barnstaple vs Bideford (15/09/2024)"

**Field 2: Home Score**
- Type: Numeric input
- Required: Yes
- Purpose: Points scored by home team
- Format: Whole number (0-999)
- Example: "32"

**Field 3: Away Score**
- Type: Numeric input
- Required: Yes
- Purpose: Points scored by away team
- Format: Whole number (0-999)
- Example: "17"

**Field 4: Home Tries**
- Type: Numeric input
- Required: Yes
- Purpose: Number of tries scored by home team
- Format: Whole number (0-99)
- Example: "5"
- Note: Used for bonus points calculation

**Field 5: Away Tries**
- Type: Numeric input
- Required: Yes
- Purpose: Number of tries scored by away team
- Format: Whole number (0-99)
- Example: "2"
- Note: Used for bonus points calculation

### Additional Fields (may exist)

**Home Conversions**:
- Number of successful conversions
- Optional field

**Away Conversions**:
- Number of successful conversions
- Optional field

**Home Penalties**:
- Number of successful penalty kicks
- Optional field

**Away Penalties**:
- Number of successful penalty kicks
- Optional field

**Match Notes**:
- Textarea for additional information
- Notable events, injuries, cards
- Man of the match
- Weather conditions

### Form Actions

**Submit Button**: "Add Result" or "Save Result"
- Saves match result to database
- Updates league tables automatically
- Calculates bonus points
- Redirects to matches page

### Instructions for Adding a Result

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Home Dashboard → Club Management → Add Result
   - OR from Club Admin Dashboard → Add New Result button
   - OR go directly to `/accounts/new_result/`

2. **Select Match**:
   - Click Match dropdown
   - List shows fixtures without results
   - Format: "Home vs Away (Date)"
   - Select completed match
   - Example: Select "Barnstaple vs Bideford (15/09/2024)"

3. **Enter Home Score**:
   - Click Home Score field
   - Type total points scored by home team
   - Include all: tries (5pts), conversions (2pts), penalties (3pts), drop goals (3pts)
   - Example: "32"

4. **Enter Away Score**:
   - Click Away Score field
   - Type total points scored by away team
   - Include all scoring
   - Example: "17"

5. **Enter Home Tries**:
   - Click Home Tries field
   - Type number of tries scored by home team
   - Count tries only, not conversions
   - Example: "5"

6. **Enter Away Tries**:
   - Click Away Tries field
   - Type number of tries scored by away team
   - Count tries only
   - Example: "2"

7. **Enter Additional Stats** (If Available):
   - Enter conversions, penalties, etc.
   - Complete all available fields
   - Ensure accuracy

8. **Add Match Notes** (Optional):
   - Enter notable match information
   - Record man of the match
   - Note any incidents
   - Weather conditions

9. **Submit Form**:
   - Review all scores for accuracy
   - Verify tries count is correct
   - Click submit button
   - System validates entries
   - Calculates league points and bonus points
   - Updates league tables
   - Redirects to matches page
   - Result now visible on match listing

### Validation Rules

**Match**:
- Must select from dropdown
- Cannot be "----------"
- Must be existing fixture

**Scores**:
- Must be numeric
- Cannot be negative
- Typically 0-100 range
- Both home and away scores required

**Tries**:
- Must be numeric
- Cannot be negative
- Must be realistic (typically 0-15)
- Used for bonus points calculation

### Rugby Scoring Reference

**Points Values**:
- Try: 5 points
- Conversion: 2 points
- Penalty kick: 3 points
- Drop goal: 3 points

**Example Score Calculation**:
- 5 tries = 25 points
- 4 conversions = 8 points
- 1 penalty = 3 points
- Total = 36 points

### Bonus Points System

**Typical Rugby Union Bonus Points**:
- **Win**: 4 points
- **Draw**: 2 points each
- **Loss**: 0 points
- **Bonus Point (Attack)**: +1 point for scoring 4+ tries
- **Bonus Point (Losing)**: +1 point for losing by 7 points or less

**System Calculations**:
- Automatically calculated based on result
- Tries field used to determine try bonus
- Score difference determines losing bonus point
- Updates league table standings

### Result Entry Best Practices

**Accuracy Checks**:
- Verify final score from match report
- Double-check try count
- Ensure home/away teams are correct
- Confirm match date

**Timing**:
- Enter results within 24-48 hours of match
- Allows for league table updates
- Players/parents check results regularly
- Delays can affect league standings

**Score Verification**:
- Match total points with breakdown
- 5 tries + 4 conversions + 1 penalty = 28 points
- Ensure math adds up
- Check against referee report if available

### After Result Entered

**Automatic Updates**:
- Match status changes to "Match Played"
- League table recalculated
- Team statistics updated
- Points awarded to teams
- Result visible on dashboards

**Result Visibility**:
- Home Dashboard → Matches section
- Club Admin Dashboard → Club Matches
- Team details pages show results
- League tables updated
- Public results page (if available)

### Common Use Cases

**When to Add Results**:
- Immediately after match completion
- Within 24 hours for league matches
- After referee confirmation
- Cup/playoff results for progression

**Result Types**:
- Regular league matches
- Cup competition matches
- Friendly/exhibition matches
- Playoff/championship matches

### Troubleshooting

**Form won't submit**:
- Verify all required fields completed
- Check Match dropdown is selected (not "----------")
- Ensure all scores are numeric
- Verify tries count is entered
- Check scores are not negative

**Match doesn't appear in dropdown**:
- Fixture may not exist yet (create fixture first)
- Result may already be entered
- Match may be in different season
- Refresh page and try again

**Wrong match selected**:
- Cannot edit after submission in some systems
- May need to delete result and re-enter
- Contact administrator if needed
- Use Edit Result function if available

**Scores don't match**:
- Verify from official match report
- Check referee's score sheet
- Confirm with both teams
- Edit result if error found

### Navigation

**To Access Form**:
- Home Dashboard → Club Management menu → Add Result
- Club Admin Dashboard → Add New Result button
- Match listing → Add Result link
- Direct URL: `/accounts/new_result/`

**To Cancel**:
- Click browser back button
- Navigate to Dashboard
- Result not saved if form not submitted

### Related Functions

**After Result Entry**:
- Use Edit Result to modify if errors found
- View Match Details to see full result
- Check League Table for updated standings
- View team statistics
