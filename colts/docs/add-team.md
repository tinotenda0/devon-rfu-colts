# Devon RFU Colts Administration Portal - Add New Team

## 10. ADD NEW TEAM FORM

**URL**: `/accounts/new_team/`

### Overview
The Add New Team form allows administrators to register new club teams in the system.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts information
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add New Team"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: Team Name**
- Type: Text input
- Required: Yes
- Purpose: Official team/club name
- Example: "Barnstaple", "Exeter Athletic", "Plymouth Albion"
- Character limit: Typically 100 characters

**Field 2: Team Crest**
- Type: URL input
- Required: No (typically uses placeholder if not provided)
- Format: Valid image URL
- Placeholder: "https://placehold.co/400x"
- Purpose: Link to team logo/crest image
- Recommended: 400x400 pixels, square format
- Supported formats: JPG, PNG, SVG

**Field 3: Team Bio**
- Type: Textarea (multi-line text)
- Required: No
- Purpose: Team description and information
- Example: "Barnstaple Colts side for the 2024/25 season."
- Character limit: Typically 500 characters
- Include: Team history, home ground, club colors

### Additional Fields (may require scrolling)

**Field 4: Gender**
- Type: Dropdown
- Required: Yes
- Options: Male, Female, Mixed
- Example: "Male"

**Field 5: Age Group**
- Type: Text input or dropdown
- Required: Yes
- Options: U18, U16, U15, U14, etc.
- Example: "U18"

### Form Actions

**Submit Button**: "Add Team" or "Create Team"
- Saves new team to database
- Redirects to Manage Teams page

### Instructions for Adding a Team

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Home Dashboard → Click **New** under TEAMS
   - OR from Manage Teams → Click **ADD NEW TEAM**
   - OR go directly to `/accounts/new_team/`

2. **Enter Team Name**:
   - Click in Team Name field
   - Type official club/team name
   - Use proper capitalization
   - Example: "Exeter Athletic" (not "exeter athletic")

3. **Enter Team Crest URL** (Optional):
   - Click in Team Crest field
   - Paste full URL to team logo image
   - Ensure URL is publicly accessible
   - Example: "https://example.com/crests/barnstaple.png"
   - Leave placeholder if no crest available

4. **Write Team Bio** (Optional):
   - Click in Team Bio field
   - Enter descriptive information about team
   - Include relevant details:
     - Club location
     - Season/year
     - Brief history
     - Home ground
   - Example: "Exeter Athletic Colts side for the 2024/25 season. Based at the Athletic Ground in Exeter."

5. **Select Gender**:
   - Click Gender dropdown
   - Select appropriate category
   - Options: Male, Female, Mixed

6. **Enter Age Group**:
   - Click Age Group field
   - Enter or select age category
   - Example: "U18"

7. **Submit Form**:
   - Review all entries
   - Click submit button
   - System validates entries
   - Redirects to Manage Teams page
   - New team appears in alphabetical list

### Validation Rules

**Team Name**:
- Cannot be empty
- Should be unique (avoid exact duplicates)
- Use official club names

**Team Crest**:
- Must be valid URL format if provided
- Image should be accessible
- Optional field - placeholder used if empty

**Gender & Age Group**:
- Both required fields
- Must match standard formats

### Team Naming Best Practices

**Good Team Names**:
- Use official club names: "Barnstaple", "Exeter Saracens"
- Avoid abbreviations unless official
- Use consistent capitalization
- Include full club name, not shortened versions

**Avoid**:
- "Team 1", "Team A" (too generic)
- All caps: "BARNSTAPLE" (unless official)
- Inconsistent naming across teams

### Team Crest Guidelines

**Image Requirements**:
- Square format recommended (400x400px)
- Clear, high-quality image
- PNG format with transparent background preferred
- File size: Under 500KB for fast loading
- Accessible via HTTPS URL

**Where to Host Images**:
- Club website
- Image hosting services (Imgur, Cloudinary)
- Social media profile images
- Direct file uploads (if system supports)

**If No Crest Available**:
- Leave placeholder URL
- System displays default image
- Can update crest URL later via Edit Team

### After Creation

**Next Steps**:
- Team appears in Manage Teams list (alphabetically)
- Team available in match fixture dropdowns
- Can assign players to team
- Can create fixtures involving team
- Can edit team details anytime

### Common Use Cases

**When to Create New Team**:
- New club joining the colts system
- New age group team within existing club
- Merged clubs creating new entity
- Club rebranding with new name

### Troubleshooting

**Form won't submit**:
- Verify Team Name is filled in
- Check Gender dropdown is selected
- Ensure Age Group is entered
- Validate Team Crest URL format if provided

**Team crest not displaying**:
- Verify URL is publicly accessible
- Check image URL is direct link to image file
- Ensure URL uses HTTPS (not HTTP)
- Try placeholder URL first, update later

**Team doesn't appear in fixture dropdowns**:
- Refresh the page
- Verify team was saved successfully
- Check team has correct gender/age group
- Ensure you have proper permissions

### Navigation

**To Access Form**:
- Home Dashboard → New button (TEAMS panel)
- Manage Teams → ADD NEW TEAM button
- Direct URL: `/accounts/new_team/`

**To Cancel**:
- Click browser back button
- Navigate to Manage Teams or Home
