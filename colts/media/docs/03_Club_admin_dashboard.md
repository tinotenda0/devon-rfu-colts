# 3. Club Admin Dashboard

**URL:** `/accounts/dash/`

## Overview
The Club Admin Dashboard is a centralized hub specifically for managing a single club's operations. It allows admins to manage their specific players, view their specific leagues, and record results for their matches.



## Club Information
Located at the top of the dashboard.
* **Header:** Club Name (e.g., BARNSTAPLE) and Crest.
* **Details:**
    * **Bio:** Brief description of the squad.
    * **Gender:** e.g., Male.
    * **Age Group:** e.g., U18.
* **Action:** Click the **Edit** button to update these details.

## Quick Status Sections

### Your Players
* **Display:** Total count of players and a preview list.
* **Action:** Click **VIEW PLAYERS** to manage the full roster (`/accounts/manage_players/`).

### Your Leagues
* **Display:** Count of leagues the club is currently participating in.
* **Actions:**
    * **VIEW LEAGUES:** See current league standings.
    * **JOIN LEAGUE:** Register the club for a new league.

## Match Management
This is the primary workspace for handling fixtures.

### Quick Actions
* **Add New Fixture:** Create a scheduled match.
* **Add New Result:** Input scores for a played match.

### Club Matches Table
A history and schedule of matches specific to your club.

| Date | Status | Match Details | Score | Actions |
| :--- | :--- | :--- | :--- | :--- |
| 15/09 | Match Played | Barnstaple vs Bideford | 32 - 5 | View / Edit / Delete |
| 08/09 | Match Played | Barnstaple vs Bideford | 7 - 17 | View / Edit / Delete |

## Player Roster
A card-style view of the current squad.



**Card Details:**
* Avatar (Default or Custom)
* Name
* Position (e.g., PROP, HOOKER, LOCK, FLANKER)
* **Profile Button:** Click to view full player history and stats.

## Key Operational Workflows

### How to Add a Match Fixture
1.  Locate the **MANAGE MATCHES** section.
2.  Click the **Add New Fixture** button.
3.  Fill in the League, Season, Date, Time, and Venue.
4.  Submit the form.

### How to Record a Match Result
1.  Locate the **MANAGE MATCHES** section.
2.  Click the **Add New Result** button.
3.  Select the match from the dropdown list.
4.  Enter the Home Score, Away Score, and Try counts.
5.  Submit the form.

### How to Add a New Player
1.  Scroll to the **PLAYERS** section.
2.  Click the **Add Player** link.
3.  Enter player details (Name, Age, Position, Bio).
4.  Submit to add them to the roster.

### How to Edit a Result
1.  Find the specific match in the **[CLUB NAME] MATCHES** table.
2.  Click **Edit Result**.
3.  Modify the scores or tries as necessary.
4.  Save changes.