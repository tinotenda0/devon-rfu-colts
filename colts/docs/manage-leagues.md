# Devon RFU Colts Administration Portal - Manage Leagues

## 5. MANAGE LEAGUES

**URL**: `/accounts/manage_leagues/`

### Overview
The Manage Leagues page displays all rugby leagues/competitions in the system with tools to create, edit, or delete leagues.

### Page Header
- Title: "MANAGE LEAGUES"

### All Leagues Section

**Section Title**: ALL LEAGUES

**Add League Button**:
- **ADD NEW LEAGUE** button → Navigate to `/accounts/new_league/`
- Located at top of leagues list

### League List Display

**Each League Shows**:
- League name (e.g., "DEVON COLTS NORTH", "DEVON COLTS SOUTH")
- Category details (e.g., "Male - U18 (2024/2025)")
- Description/notes (e.g., "Demo league for northern clubs")

**Action Buttons Per League**:
| Button | Color | Function | Destination |
|--------|-------|----------|-------------|
| EDIT | Green | Modify league details | `/accounts/edit_league/{id}/` |
| DELETE | Red | Remove league | Confirmation dialog |


### Key Actions From Manage Leagues Page

**To Create a New League**:
1. Click **ADD NEW LEAGUE** button at top
2. Fill in league form (see Add New League form)
3. Enter league name, age group, gender, season, notes
4. Submit

**To Edit an Existing League**:
1. Locate league in list
2. Click **EDIT** button
3. Modify details in form
4. Save changes

**To Delete a League**:
1. Locate league in list
2. Click **DELETE** button
3. Confirm deletion
4. League removed from system

**Warning**: Deleting a league may affect teams and matches associated with it

### League Information Fields

**Standard League Data**:
- League Name (text)
- Age Group (e.g., U18, U16, U14)
- Gender (Male/Female/Mixed)
- Season (linked to season year)
- Notes/Description (additional info)

### Navigation

**To Access Manage Leagues**:
- From Home Dashboard → Click **Manage** under ACTIVE LEAGUES
- From navigation bar → (not directly accessible, use Home)

**To Return to Dashboard**:
- Click **Home** in navigation bar
- Click **Devon RFU Colts** logo

### Use Cases

**When to Create a League**:
- New competition starting
- Different age groups or genders
- Regional divisions (North/South)
- Cup competitions vs league play

**When to Edit a League**:
- Correct league name typos
- Update notes/descriptions
- Change associated season

**When to Delete a League**:
- League was created in error
- Competition cancelled before any matches played
- Duplicate entry created by mistake
