# Devon RFU Colts Administration Portal - Home Dashboard

## 2. HOME DASHBOARD

**URL**: `/accounts/`

### Overview
The Home Dashboard is the main landing page for authenticated users. It provides a quick overview of all key information and quick-access shortcuts to major management functions.

### Page Header
- Welcome message: "WELCOME BACK, [USERNAME]"
- Current date display (top-right)
- Navigation bar with main menu items

### Main Statistics Panels

**Panel 1: TOTAL SEASONS**
- Displays: `1`
- Quick Actions:
  - **New** button → Navigate to `/accounts/new_season/`
  - **Manage** button → Navigate to `/accounts/manage_seasons/`
- Icon: Trophy icon

**Panel 2: ACTIVE LEAGUES**
- Displays: `2`
- Quick Actions:
  - **New** button → Navigate to `/accounts/new_league/`
  - **Manage** button → Navigate to `/accounts/manage_leagues/`
- Icon: List icon

**Panel 3: TEAMS**
- Displays: `40`
- Quick Actions:
  - **New** button → Navigate to `/accounts/new_team/`
  - **Manage** button → Navigate to `/accounts/manage_teams/`
- Icon: Shield icon

### Matches Section

**Section Title**: MATCHES

**Content**: Table displaying recent upcoming matches with columns:
- Date (e.g., 22/09)
- Home Team (clickable link to team details)
- Versus separator (-)
- Away Team (clickable link to team details)
- **View Match** button

**Example Matches Listed**:
1. Paignton vs Plymouth Albion
2. Plymouth Argaum vs Plymouth Dolphins
3. Old Plymothian vs Old Technicians
4. Plymstock Oaks vs Salcombe

### Club Admins Section

**Section Title**: CLUB ADMINS

**Features**:
- **Add** button → Navigate to `/accounts/add_new/`
- Admin table with columns:
  - USER (username and email)
  - CLUB (assigned club)
  - ACTIONS (Edit and Delete buttons)

**Existing Admins**:
| User | Email | Club | Actions |
|------|-------|------|---------|
| Admin | admin@crediton.co.uk | Crediton | Edit / Delete |
| Tino | admin@tinotenda.co | Barnstaple | Edit / Delete |

### My Account Section

**Section Title**: MY ACCOUNT

**Content**:
- Account avatar/initial (letter)
- Username display
- Email address
- Role label
- Club assignment

**Quick Actions**:
- **Edit Profile** button → Navigate to `/accounts/edit_user/{id}/`
- **Logout** button → Navigate to `/accounts/logout/`

### Navigation Bar

**Top Navigation Menu**:
| Item | Type | Destination |
|------|------|-------------|
| Devon RFU Colts | Logo/Home | `/accounts/` |
| Home | Link | `/accounts/` |
| Club Admin Dashboard | Link | `/accounts/dash/` |
| Club Management | Dropdown | See below |
| Browse | Dropdown | See below |
| Welcome, [Username] | User Profile | `/accounts/` |
| Logout | Link | `/accounts/logout/` |

**Club Management Dropdown**:
- Add Fixture → `/accounts/new_fixture/`
- Add Result → `/accounts/new_result/`
- Add Player → `/accounts/new_player/`
- Manage Players → `/accounts/manage_players/`

**Browse Dropdown**:
- Archive → `/accounts/archive/`

### Key Actions From Home Dashboard

**To Create New Season**:
1. Click **New** button under TOTAL SEASONS panel
2. Fill form and submit

**To View All Seasons**:
1. Click **Manage** button under TOTAL SEASONS panel
2. View complete list with edit/delete/archive options

**To View Recent Matches**:
1. Scroll to MATCHES section
2. Click **View Match** on any match to see details

**To Add Club Admin**:
1. Click **Add** button in CLUB ADMINS section
2. Fill in admin details
3. Submit form

**To Manage Club Admins**:
1. View admin table in CLUB ADMINS section
2. Click **Edit** to modify admin details
3. Click **Delete** to remove admin

**To Access Club-Specific Dashboard**:
1. Click **Club Admin Dashboard** in navigation
2. View your club's specific information

### User Profile Options

**From My Account Section**:
- Click **Edit Profile** to modify your account details
- Click **Logout** to exit the system

### Summary of Main Workflows

| Task | Steps | Destination |
|------|-------|-------------|
| Create Season | Home → New (Seasons) | New Season Form |
| Create League | Home → New (Leagues) | New League Form |
| Create Team | Home → New (Teams) | New Team Form |
| Add Player | Club Management → Add Player | New Player Form |
| Add Fixture | Club Management → Add Fixture | New Fixture Form |
| Add Result | Club Management → Add Result | New Result Form |
| View All Teams | Home → Manage (Teams) | Manage Teams Page |
| View All Leagues | Home → Manage (Leagues) | Manage Leagues Page |
| View Seasons | Home → Manage (Seasons) | Manage Seasons Page |
| Manage Players | Club Management → Manage Players | Manage Players Page |
