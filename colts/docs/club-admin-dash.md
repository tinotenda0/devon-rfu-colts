# Devon RFU Colts Administration Portal - Club Admin Dashboard

## 3. CLUB ADMIN DASHBOARD

**URL**: `/accounts/dash/`

### Overview
The Club Admin Dashboard displays club-specific information and management tools for the logged-in user's assigned club. This is a centralized hub for team management and match administration.

### Page Header
- Welcome message: "WELCOME BACK, [USERNAME]"
- Current date display

### Club Information Section

**Club Header**:
- Club name (e.g., "BARNSTAPLE")
- Club crest/logo image
- Club designation (e.g., "BARNSTAPLE")

**Club Details**:
- **Bio**: Club description (e.g., "Barnstaple Colts side for the 2024/25 season.")
- **Gender**: Male
- **Age Group**: U18

**Edit Button**: Click to edit club details

### Your Players Section

**Section Title**: YOUR PLAYERS

**Display**:
- Player count (e.g., "5 PLAYERS")
- Player avatar/image
- Player name
- Player position
- Player profile link

**Quick Actions**:
- **VIEW PLAYERS** button → Navigate to `/accounts/manage_players/`
- Add Player link (if scrolling to bottom)

### Your Leagues Section

**Section Title**: YOUR LEAGUES

**Display**:
- League count (e.g., "1 LEAGUE")

**Quick Actions**:
- **VIEW LEAGUES** button → Navigate to `/accounts/my_leagues/`
- **JOIN LEAGUE** button → Navigate to `/accounts/join_league/`

### Manage Matches Section

**Section Title**: MANAGE MATCHES

**Quick Action Buttons**:
- **Add New Fixture** button → Navigate to `/accounts/new_fixture/`
- **Add New Result** button → Navigate to `/accounts/new_result/`

### Club Matches Section

**Section Title**: [CLUB NAME] MATCHES

**Content**: Table displaying all matches for the club with columns:
- Date (DD/MM format)
- Match Status (e.g., "Match Played")
- Home Team (link)
- Home Score
- Away Score
- Away Team (link)
- Action buttons:
  - **View Match** → View match details
  - **Edit Result** → Modify match result
  - **Delete** → Remove match

**Example Match Entry**:
| Date | Status | Teams | Score | Actions |
|------|--------|-------|-------|---------|
| 15/09 | Match Played | Barnstaple vs Bideford | 32-5 | View / Edit / Delete |
| 08/09 | Match Played | Barnstaple vs Bideford | 7-17 | View / Edit / Delete |
| 01/09 | Match Played | Barnstaple vs Bideford | 15-15 | View / Edit / Delete |

**View All Link**: "View All Matches" → Navigate to `/matches`

### Players Section

**Section Title**: PLAYERS

**Player Cards Display**:
- Player avatar (default image)
- Player name
- Player position (e.g., PROP, HOOKER, LOCK, FLANKER, NUMBER 8)
- **Player Profile** button → Navigate to `/accounts/player_details/{id}/`

**Example Players**:
1. BARNSTAPLE PLAYER 1 - PROP
2. BARNSTAPLE PLAYER 2 - HOOKER
3. BARNSTAPLE PLAYER 3 - LOCK
4. BARNSTAPLE PLAYER 4 - FLANKER
5. BARNSTAPLE PLAYER 5 - NUMBER 8

**Quick Actions**:
- **Add Player** link → Navigate to `/accounts/new_player/`
- **View All** link → Navigate to `/accounts/manage_players/`

### Key Actions From Club Dashboard

**To Add a Match Fixture**:
1. Locate "MANAGE MATCHES" section
2. Click **Add New Fixture** button
3. Fill in league, season, date, time, venue
4. Submit form

**To Record Match Result**:
1. Locate "MANAGE MATCHES" section
2. Click **Add New Result** button
3. Select match, enter scores and tries
4. Submit form

**To Add a Player**:
1. Scroll to "PLAYERS" section
2. Click **Add Player** link
3. Enter player details (name, age, position, bio)
4. Submit form

**To View Player Profile**:
1. Locate player in "PLAYERS" section
2. Click **Player Profile** button
3. View full player details

**To Edit Match Result**:
1. Find match in "[CLUB NAME] MATCHES" table
2. Click **Edit Result** button
3. Modify score or tries
4. Save changes

**To Delete a Match**:
1. Find match in "[CLUB NAME] MATCHES" table
2. Click **Delete** button
3. Confirm deletion

**To View All Players**:
1. Click **VIEW PLAYERS** button in "YOUR PLAYERS" section
2. See complete roster

**To View League Information**:
1. Click **VIEW LEAGUES** button in "YOUR LEAGUES" section
2. See league details

**To Join a League**:
1. Click **JOIN LEAGUE** button in "YOUR LEAGUES" section
2. Select available league
3. Submit

### Account Menu

**From Page**:
- Click **Edit Profile** link in My Account section
- Click **Logout** to exit system
