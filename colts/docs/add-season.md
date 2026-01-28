# Devon RFU Colts Administration Portal - Add New Season

## 8. ADD NEW SEASON FORM

**URL**: `/accounts/new_season/`

### Overview
The Add New Season form allows administrators to create new rugby seasons in the system.

### Page Layout
- Left panel: Green branded area with Devon RFU Colts information
- Right panel: White form area with Devon RFU shield logo
- Split-screen design

### Form Header
- Title: "Add New Season"
- Devon RFU Colts logo displayed at top

### Form Fields

**Field 1: Season Year**
- Type: Text input
- Required: Yes
- Format: YYYY/YYYY (e.g., "2024/2025")
- Purpose: Define the season's year designation
- Example: "2025/2026"

**Field 2: Start Date**
- Type: Date picker
- Required: Yes
- Format: dd/mm/yyyy
- Input method: Click to open calendar picker
- Purpose: Set season start date
- Example: "01/09/2025"

**Field 3: End Date**
- Type: Date picker
- Required: Yes
- Format: dd/mm/yyyy
- Input method: Click to open calendar picker
- Purpose: Set season end date
- Example: "31/05/2026"

**Field 4: Archived**
- Type: Checkbox
- Required: No
- Default: Unchecked
- Purpose: Mark season as archived (typically left unchecked for new seasons)

### Form Actions

**Submit Button**: "Add Season"
- Saves new season to database
- Redirects to Manage Seasons page

### Instructions for Adding a Season

**Step-by-Step Process**:

1. **Navigate to Form**:
   - From Home Dashboard → Click **New** under TOTAL SEASONS
   - OR go directly to `/accounts/new_season/`

2. **Enter Season Year**:
   - Click in Season Year field
   - Type year range in format: YYYY/YYYY
   - Example: "2025/2026"

3. **Select Start Date**:
   - Click Start Date field
   - Calendar picker opens
   - Select September 1st (or desired start date)
   - Date populates in dd/mm/yyyy format

4. **Select End Date**:
   - Click End Date field
   - Calendar picker opens
   - Select May 31st (or desired end date)
   - Date populates in dd/mm/yyyy format

5. **Set Archived Status** (Optional):
   - Leave unchecked for new/active seasons
   - Check only if creating historical/archived season

6. **Submit Form**:
   - Click "Add Season" button
   - System validates entries
   - Redirects to Manage Seasons page
   - New season appears in list

### Validation Rules

**Season Year**:
- Must be in YYYY/YYYY format
- Years should be consecutive (e.g., 2025/2026, not 2025/2027)

**Dates**:
- End date must be after start date
- Typical season runs September to May
- Date format must be dd/mm/yyyy

### Common Season Date Ranges

**Standard Rugby Season**:
- Start: September 1st
- End: May 31st
- Duration: 9 months

**Tips**:
- Use consistent date ranges across seasons
- Align with official rugby calendar
- Consider pre-season and post-season needs

### After Creation

**Next Steps**:
- Season appears in Manage Seasons list
- Available in dropdown selectors for leagues
- Can be assigned to fixtures and matches
- Can be edited or archived later

### Troubleshooting

**Form won't submit**:
- Verify all required fields completed
- Check date format is correct
- Ensure end date is after start date
- Verify browser allows form submission

**Season doesn't appear in dropdowns**:
- Refresh the page
- Check season was saved successfully
- Verify you have proper permissions

### Navigation

**To Access Form**:
- Home Dashboard → New button (TOTAL SEASONS panel)
- Direct URL: `/accounts/new_season/`

**To Cancel**:
- Click browser back button
- Navigate to Home via top menu
