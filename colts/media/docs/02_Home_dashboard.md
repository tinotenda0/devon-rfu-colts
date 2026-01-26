# 2. Home Dashboard

**URL:** `/accounts/`

## Overview
The Home Dashboard is the main landing page for authenticated users. It provides a high-level overview of key statistics and offers "Quick Action" shortcuts to major management functions.



## Page Header
* **Welcome Message:** Displays "WELCOME BACK, [USERNAME]".
* **Date:** Current date displayed in the top-right corner.
* **Navigation:** Main menu bar for system-wide navigation.

## Main Statistics Panels

### 1. TOTAL SEASONS (Trophy Icon)
* **Current Count:** Displays total active seasons (e.g., 1).
* **Quick Actions:**
    * **New:** Navigate to `/accounts/new_season/` to create a season.
    * **Manage:** Navigate to `/accounts/manage_seasons/` to view all.

### 2. ACTIVE LEAGUES (List Icon)
* **Current Count:** Displays total active leagues (e.g., 2).
* **Quick Actions:**
    * **New:** Navigate to `/accounts/new_league/` to create a league.
    * **Manage:** Navigate to `/accounts/manage_leagues/` to view all.

### 3. TEAMS (Shield Icon)
* **Current Count:** Displays total registered teams (e.g., 40).
* **Quick Actions:**
    * **New:** Navigate to `/accounts/new_team/` to add a team.
    * **Manage:** Navigate to `/accounts/manage_teams/` to view the roster.

## Matches Section
A table displaying recent and upcoming matches.

| Date | Home Team | vs | Away Team | Action |
| :--- | :--- | :-: | :--- | :--- |
| 22/09 | [Paignton] | - | [Plymouth Albion] | **View Match** |
| 22/09 | [Plymouth Argaum] | - | [Plymouth Dolphins] | **View Match** |
| 22/09 | [Old Plymothian] | - | [Old Technicians] | **View Match** |

## Club Admins Management
This section allows Super Admins to manage club-level users.

* **Add New Admin:** Click the **Add** button to navigate to `/accounts/add_new/`.

**Existing Admins Table:**
| User | Club | Actions |
| :--- | :--- | :--- |
| `admin` (admin@crediton.co.uk) | Crediton | Edit / Delete |
| `Tino` (admin@tinotenda.co) | Barnstaple | Edit / Delete |

## Navigation & Menus

### Top Navigation Bar
* **Devon RFU Colts Logo:** Returns to Home.
* **Home:** Link to `/accounts/`.
* **Club Admin Dashboard:** Link to `/accounts/dash/`.
* **Logout:** Securely exit the session.

### Dropdown Menus
* **Club Management:**
    * Add Fixture
    * Add Result
    * Add Player
    * Manage Players
* **Browse:**
    * Archive

## Summary of Main Workflows

| Task | Steps | Destination Form |
| :--- | :--- | :--- |
| **Create Season** | Home → New (Seasons Panel) | New Season Form |
| **Create League** | Home → New (Leagues Panel) | New League Form |
| **Create Team** | Home → New (Teams Panel) | New Team Form |
| **Add Player** | Club Management → Add Player | New Player Form |
| **Add Fixture** | Club Management → Add Fixture | New Fixture Form |
| **Add Result** | Club Management → Add Result | New Result Form |