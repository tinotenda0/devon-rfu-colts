# Devon RFU Colts Administration Portal - Manage Seasons

## 4. MANAGE SEASONS

**URL**: `/accounts/manage_seasons/`

### Overview
The Manage Seasons page displays all rugby seasons in the system and provides tools to create, edit, delete, or archive seasons.

### Page Header
- Title: "MANAGE SEASONS"
- Navigation breadcrumb available via top nav

### All Seasons Section

**Section Title**: ALL SEASONS

**Add Season Button**:
- **ADD NEW SEASON** button → Navigate to `/accounts/new_season/`
- Located at top of seasons list

### Season List Display

**Season Information Shown**:
- Season year (e.g., "2024/2025")
- Date range (e.g., "Sept. 1, 2024 - May 31, 2025")

**Action Buttons Per Season**:
| Button | Color | Function | Destination |
|--------|-------|----------|-------------|
| EDIT | Blue | Modify season details | `/accounts/edit_season/{id}/` |
| DELETE | Red | Remove season | Confirmation dialog |
| ARCHIVE | Yellow/Orange | Archive old season | `/accounts/archive_season/{id}/` |


### Key Actions From Manage Seasons Page

**To Create a New Season**:
1. Click **ADD NEW SEASON** button at top
2. Fill in season form (see Add New Season form)
3. Submit

**To Edit an Existing Season**:
1. Locate season in list
2. Click **EDIT** button
3. Modify details in form
4. Save changes

**To Delete a Season**:
1. Locate season in list
2. Click **DELETE** button
3. Confirm deletion in dialog
4. Season removed from system

**To Archive a Season**:
1. Locate season in list
2. Click **ARCHIVE** button
3. Season moved to archive
4. No longer appears in active lists

### Navigation

**To Access Manage Seasons**:
- From Home Dashboard → Click **Manage** under TOTAL SEASONS
- From navigation bar → (not directly accessible, use Home)

**To Return to Dashboard**:
- Click **Home** in navigation bar
- Click **Devon RFU Colts** logo

### Best Practices

**Season Management Tips**:
- Archive old seasons rather than deleting them to preserve historical data
- Keep season date ranges accurate for reporting
- Only delete seasons if they were created in error
- Edit seasons to correct typos or date errors
