# Devon RFU Colts Administration Portal - Add New Player

## 11. ADD NEW PLAYER FORM

**URL**: `/accounts/new_player/`

### Overview
The Add New Player form allows club administrators to register new players to their team roster.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts branding
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add New Player"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: Player Name**
- Type: Text input
- Required: Yes
- Purpose: Player's full name
- Format: First Name Last Name
- Example: "John Smith", "Tom Williams"
- Character limit: Typically 100 characters

**Field 2: Age**
- Type: Numeric input
- Required: Yes
- Purpose: Player's current age
- Format: Number only
- Valid range: Typically 12-18 for colts
- Example: "17"

**Field 3: Position**
- Type: Text input or dropdown
- Required: Yes
- Purpose: Player's primary playing position
- Options: PROP, HOOKER, LOCK, FLANKER, NUMBER 8, SCRUM-HALF, FLY-HALF, CENTRE, WING, FULLBACK
- Example: "FLANKER"

**Field 4: Bio**
- Type: Textarea (multi-line text)
- Required: No
- Purpose: Additional player information
- Content ideas:
  - Playing experience
  - Previous clubs
  - Achievements
  - Playing style
- Character limit: Typically 500 characters
- Example: "Experienced flanker with strong tackling ability. Previously played for U16s."

**Field 5: Privacy Consent**
- Type: Checkbox
- Required: May be required depending on configuration
- Purpose: GDPR compliance and data protection consent
- Label: Typically confirms parent/guardian consent for player data
- Must be checked to proceed (if required)

### Additional Fields (may exist)

**Player Photo**:
- Type: File upload or URL
- Required: No
- Purpose: Player profile picture
- Formats: JPG, PNG
- Default: System uses placeholder avatar if not provided

**Jersey Number**:
- Type: Numeric input
- Required: No
- Range: 1-99
- Example: "7"

**Contact Information**:
- Email
- Phone
- Emergency contact (parent/guardian)

### Form Actions

**Submit Button**: "Add Player" or "Register Player"
- Saves new player to team roster
- Redirects to Manage Players page

### Instructions for Adding a Player

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Club Admin Dashboard → Click **Add Player**
   - OR from Manage Players → Click **Add Player**
   - OR from navigation → Club Management → Add Player
   - OR go directly to `/accounts/new_player/`

2. **Enter Player Name**:
   - Click in Player Name field
   - Type player's full name
   - Use proper capitalization
   - Example: "Thomas Anderson"

3. **Enter Age**:
   - Click in Age field
   - Type player's current age (numbers only)
   - Must be appropriate for colts rugby (typically 12-18)
   - Example: "17"

4. **Select Position**:
   - Click in Position field
   - Type or select from dropdown
   - Choose primary playing position
   - Use standard position names
   - Example: "FLANKER"

5. **Write Player Bio** (Optional):
   - Click in Bio field
   - Enter relevant information:
     - Playing experience
     - Strengths and skills
     - Previous teams
     - Notable achievements
   - Example: "Strong ball carrier with excellent defensive skills. Joined from U16 squad."

6. **Accept Privacy Consent** (If Required):
   - Check the Privacy Consent checkbox
   - Confirms consent for data processing
   - Required for GDPR compliance
   - Typically requires parent/guardian consent for minors

7. **Submit Form**:
   - Review all entries
   - Click submit button
   - System validates entries
   - Redirects to Manage Players page
   - New player appears in roster

### Validation Rules

**Player Name**:
- Cannot be empty
- Should contain first and last name
- Use proper capitalization

**Age**:
- Must be numeric
- Should be within colts age range (typically 12-18)
- Cannot be empty

**Position**:
- Must be valid rugby position
- Required field
- Use standard position names

**Privacy Consent**:
- Must be checked if required
- Ensures GDPR compliance
- Typically requires parent/guardian consent for minors

### Rugby Positions Reference

**Forwards (1-8)**:
- PROP (1, 3) - Front row
- HOOKER (2) - Front row
- LOCK (4, 5) - Second row
- FLANKER (6, 7) - Back row
- NUMBER 8 (8) - Back row

**Backs (9-15)**:
- SCRUM-HALF (9) - Half-back
- FLY-HALF (10) - Half-back
- CENTRE (12, 13) - Midfield
- WING (11, 14) - Outside backs
- FULLBACK (15) - Outside backs

### Player Information Best Practices

**Name Entry**:
- Use full legal name or playing name
- Consistent formatting across all players
- Proper capitalization
- Include middle initials if needed for identification

**Bio Content Ideas**:
- Previous playing experience
- Current school/club
- Playing strengths
- Career highlights
- Position versatility
- Leadership roles

### After Creation

**Next Steps**:
- Player appears in Manage Players roster
- Player card displays with default avatar
- Can view full player profile
- Can select player for match squads
- Can update player information anytime
- Can upload player photo (if supported)

### Common Use Cases

**When to Add Players**:
- Start of new season (bulk registration)
- New player joining mid-season
- Player transferring from another club
- Youth player moving up from younger age group

### Data Protection & Privacy

**GDPR Compliance**:
- Parent/guardian consent required for minors (under 16)
- Data used only for rugby administration
- Player information kept confidential
- Can request data deletion
- Privacy policy should be available

**Consent Requirements**:
- Playing registration
- Photography/media consent
- Contact information usage
- Medical information (if collected)

### Troubleshooting

**Form won't submit**:
- Verify all required fields completed
- Check age is numeric value
- Ensure position is valid
- Check privacy consent is accepted (if required)
- Verify name field is not empty

**Player doesn't appear in roster**:
- Refresh the Manage Players page
- Verify form was submitted successfully
- Check you're viewing correct team
- Ensure you have proper permissions

**Position dropdown empty**:
- Type position manually if dropdown fails
- Use standard position names
- Contact administrator if issue persists

### Navigation

**To Access Form**:
- Club Admin Dashboard → Add Player link
- Manage Players → Add Player button
- Club Management menu → Add Player
- Direct URL: `/accounts/new_player/`

**To Cancel**:
- Click browser back button
- Navigate to Manage Players or Dashboard
- Player data not saved if form not submitted

