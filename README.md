<div align="center">
  <h1>🏨 Hospitality ERP</h1>
  <p><strong>A Comprehensive Hospitality Management Suite for ERPNext v15+</strong></p>
  <p>
    <em>Hotels · Resorts · Cruises · Theme Parks · Golf Courses · Marinas · Cinemas · Sports Complexes · Campsites · Spas</em>
  </p>
  <br>
</div>

---

## 📋 Table of Contents

1. [Introduction](#-introduction)
2. [System Requirements](#-system-requirements)
3. [Installation Guide](#-installation-guide)
4. [Getting Started](#-getting-started)
5. [Module Guide](#-module-guide)
   - [Hotel Masters](#1-hotel-masters)
   - [Reservations](#2-reservations)
   - [Property Management](#3-property-management)
   - [Guest CRM](#4-guest-crm)
   - [Revenue Management](#5-revenue-management)
   - [Housekeeping](#6-housekeeping)
   - [Hotel Maintenance](#7-hotel-maintenance)
   - [Food & Beverage (F&B)](#8-food--beverage-fb)
   - [Events Management](#9-events-management)
   - [Spa & Recreation](#10-spa--recreation)
   - [Golf Management](#11-golf-management)
   - [Theme Park Management](#12-theme-park-management)
   - [Cinema Management](#13-cinema-management)
   - [Marina Management](#14-marina-management)
   - [Cruise Management](#15-cruise-management)
   - [Campsite Management](#16-campsite-management)
   - [Sports Complex](#17-sports-complex)
   - [Finance](#18-finance)
   - [HR & Staffing](#19-hr--staffing)
   - [Membership Management](#20-membership-management)
   - [Concierge Services](#21-concierge-services)
   - [Security Management](#22-security-management)
   - [Sustainability](#23-sustainability)
   - [Notification System](#24-notification-system)
6. [Reports & Analytics](#-reports--analytics)
7. [Automated Tasks & Schedules](#-automated-tasks--schedules)
8. [Demo Data Setup](#-demo-data-setup)
9. [Troubleshooting & FAQ](#-troubleshooting--faq)
10. [Support](#-support)

---

## 🏆 Introduction

**Hospitality ERP** is a comprehensive, all-in-one hospitality management extension built for **ERPNext v15+**. It transforms ERPNext into a complete Property Management System (PMS) and Enterprise Resource Planning solution purpose-built for the hospitality industry.

Whether you run a single boutique hotel, a sprawling resort with multiple amenities, a cruise line, a theme park, or a multi-property hospitality group — this system provides all the tools you need to manage:

- **Front Office** — Reservations, check-in/out, room assignments, guest folios
- **Operations** — Housekeeping, maintenance, concierge, security
- **Revenue** — Dynamic pricing, yield management, channel management
- **Ancillary Services** — F&B, spa, golf, theme park, cinema, marina, cruise, campsite, sports
- **Back Office** — Finance, night audit, HR, payroll, procurement, inventory
- **Guest Experience** — CRM, loyalty, feedback, membership programs
- **Compliance & Sustainability** — Environmental impact tracking, incident reporting

All modules are fully integrated, sharing a single database, so a guest's restaurant charges flow automatically to their folio, and housekeeping is notified the moment a room is checked out.

---

## 💻 System Requirements

| Component | Requirement |
|-----------|-------------|
| **ERP Version** | ERPNext v15+ / Frappe v15+ |
| **Python** | ≥ 3.10 |
| **Node.js** | ≥ 18.x |
| **Database** | MariaDB 10.6+ or PostgreSQL 13+ |
| **Redis** | 6.x+ (required by Frappe) |
| **File System** | 500 MB+ free space for the app |
| **Browser** | Chrome 90+, Firefox 90+, Edge 90+ |

---

## 📥 Installation Guide

### Step 1: Set Up the Frappe Bench

If you do not already have a Frappe Bench, install it:

```bash
# Install the bench CLI
pip install frappe-bench

# Create a new bench directory
bench init --frappe-branch version-15 hospitality-bench
cd hospitality-bench
```

### Step 2: Install ERPNext

```bash
bench get-app --branch version-15 erpnext
bench --site your-site install-app erpnext
```

### Step 3: Install Hospitality ERP

```bash
# Download the app into your bench
bench get-app https://github.com/balaji-001-gif/hospitality-management.git

# Install on your site
bench --site your-site install-app hospitality_erp
```

### Step 4: Build & Migrate

```bash
bench build
bench --site your-site migrate
```

> **Note**: The module name in ERPNext will appear as **"Hospitality Management"** under the Modules list.

### Step 5: Verify Installation

1. Log in to your ERPNext site
2. You should see the "Hospitality Management" module in the Awesome Bar / Module list
3. Check that the following workspaces are available:
   - Reservations
   - Property Management
   - Guest CRM
   - Revenue Management
   - F&B
   - Events
   - Spa & Recreation
   - Housekeeping
   - Hotel Maintenance
   - Finance
   - HR Staffing
   - Hotel Masters
   - Membership Management
   - Security Management
   - Concierge Services
   - Sustainability
   - Theme Park
   - Cinema
   - Marina
   - Cruise
   - Sports Complex

---

## 🚀 Getting Started

### Initial Setup

After installation, follow these steps to configure your property:

1. **Create a Company** — Navigate to `Home > Settings > Company` and create your hospitality company.
2. **Set Up Hotel Masters** — Go to the **Hotel Masters** workspace and configure:
   - **Property Type** (Hotel, Resort, Villa, etc.)
   - **Room Categories** (Standard, Deluxe, Suite, Penthouse)
   - **Rate Categories** (BAR, Corporate, Group, Promotional)
   - **Channels** (Direct, Booking.com, Expedia, Airbnb)
   - **Meal Plans** (Room Only, Bed & Breakfast, Half Board, Full Board, All Inclusive)
   - **Amenity Types** (WiFi, Pool, Gym, Spa, Parking)
   - **Tax Categories** (VAT, Service Tax, Tourism Tax)
3. **Define Properties** — Add your properties with address, contact details, and classification.
4. **Add Rooms** — Go to **Property Management** and add all rooms with categories and base rates.
5. **Set Rate Plans** — Configure pricing rules for different seasons and rate categories.
6. **Load Fixtures** — If needed, run the fixture loading script for predefined reference data.

### Fixtures (Pre-loaded Reference Data)

The following fixture data is automatically installed with the module:

| Fixture | Purpose |
|---------|---------|
| **Property Type** | Classification of properties (Hotel, Resort, Guest House, etc.) |
| **Room Category** | Room classifications (Standard, Deluxe, Suite, etc.) |
| **Rate Category** | Pricing categories (BAR, Corporate, Group, Promotional, etc.) |
| **Channel** | Distribution channels (Direct, OTA, GDS, etc.) |
| **Meal Plan** | Meal options (Room Only, Bed & Breakfast, Half Board, Full Board) |
| **Tax Category** | Tax configurations (VAT, Service Charge, Tourism Tax, etc.) |
| **Amenity Type** | Facility amenities (WiFi, Pool, Gym, Spa, Parking, etc.) |

### Demo Data

To quickly populate your system with sample data for evaluation:

```bash
bench --site your-site console
```

In the console:

```python
from hospitality_erp.scripts.setup_demo_data import setup_demo_data
setup_demo_data()
```

This will create:
- Properties and rooms
- Sample guest profiles
- Reservations (past, current, and future)
- F&B menu items
- Spa treatments
- Housekeeping schedules
- And more across all modules

---

## 📦 Module Guide

### 1. Hotel Masters

**Purpose**: The foundation of your hospitality system — all master data is defined here before any operational module can function.

**Key Doctypes**:
- **Property** — Define your properties (hotels, resorts, villas) with addresses, contact info, and branding
- **Room Category** — Classify rooms (e.g., Standard, Deluxe, Suite, Penthouse)
- **Rate Category** — Define pricing categories (BAR, Corporate, Group, Promotional, Long Stay)
- **Channel** — Manage distribution channels (Direct Booking, OTAs like Booking.com/Expedia, GDS)
- **Meal Plan** — Set up meal inclusions (Room Only, Bed & Breakfast, Half Board, Full Board, All Inclusive)
- **Amenity Type** — Define amenities (WiFi, Pool, Gym, Spa, Parking, Airport Shuttle)
- **Tax Category** — Configure applicable taxes
- **Night Audit** — Automate end-of-day processes

**Workflow**:
1. Set up all master records before creating reservations or transactions
2. Rate Plans link room categories with rate categories and seasonal pricing
3. Channel configurations feed into revenue management

---

### 2. Reservations

**Purpose**: Central booking engine for managing all room reservations — the heart of your front office operations.

**Features**:
- **New Reservations** — Create bookings for individuals, groups, and corporate clients
- **Booking Sources** — Accept bookings from direct channels, OTAs, travel agents, and corporate accounts
- **Guest Information** — Capture guest details, special requests, and preferences
- **Room Assignment** — Auto-assign or manually select rooms based on availability
- **Date Management** — Flexible check-in/check-out dates with early check-in and late check-out support
- **Status Tracking** — Track reservation status (Draft, Confirmed, Checked In, Checked Out, Cancelled, No Show)
- **Group Bookings** — Manage block bookings for events, weddings, and tour groups
- **Rate Application** — Apply rate plans, discounts, and promotions
- **Deposit Management** — Accept and track advance payments and deposits
- **Online Sync** — Integration with channel managers for OTA bookings

**Automated Triggers**:
- `after_insert` — Send confirmation email/SMS upon reservation creation
- `on_submit` — Check-in triggers housekeeping notification, check-out triggers folio settlement

**Daily Scheduled Tasks**:
- Send check-in reminders to upcoming guests
- Send check-out reminders to departing guests

**Key Reports**:
- **Occupancy Report** — View occupancy rates by date, room type, or property
- **No Show & Cancellation Report** — Track booking losses and patterns
- **Guest Folio Summary** — Itemized statement of all guest charges

---

### 3. Property Management

**Purpose**: Manage the physical inventory of rooms, suites, and villas across all properties.

**Features**:
- **Room Inventory** — Add, edit, and manage all rooms with details:
  - Room number, floor, wing/building
  - Room category and bed type (King, Twin, Queen, Double, Suite)
  - Maximum occupancy (adults, children)
  - Base rate and dynamic pricing
  - Amenities and facilities
  - Room status (Vacant, Occupied, Dirty, Cleaning, Out of Order, Out of Service)
- **Room Status Dashboard** — Real-time view of room availability
- **Room Maintenance** — Flag rooms as Out of Order/Out of Service for repairs
- **Block Management** — Block rooms for VIP bookings or maintenance
- **Room Transfer** — Move guests between rooms and track history

**Events**:
- `on_update` — Triggers recalculations when room details change

---

### 4. Guest CRM

**Purpose**: Build and maintain a 360-degree view of every guest to deliver personalized experiences.

**Features**:
- **Guest Profiles** — Comprehensive guest records including:
  - Personal details (name, DOB, nationality, language)
  - Contact information (email, phone, address)
  - Identification (passport, driver's license, national ID)
  - Preferences (room type, floor, amenities, dietary restrictions)
  - Communication history and feedback
  - Special dates (birthday, anniversary)
- **Guest History** — Complete stay history including past bookings, spend, and service usage
- **Preferences Tracking** — Capture and apply guest preferences on future bookings
- **Feedback Management** — Record and analyze guest feedback and satisfaction scores
- **Blacklist/Whitelist** — Manage guest blacklists and VIP/whitelist designations
- **Loyalty Integration** — Link to membership and loyalty programs

---

### 5. Revenue Management

**Purpose**: Maximize revenue through dynamic pricing, yield management, and channel optimization.

**Features**:
- **Dynamic Pricing** — Set rates based on demand, seasonality, and events
- **Rate Plans** — Create multiple rate plans per room category:
  - BAR (Best Available Rate)
  - Corporate rates
  - Group rates
  - Promotional/discounted rates
  - Long-stay and early-bird rates
- **Seasonal Pricing** — Define peak, shoulder, and off-peak seasons with different rates
- **Length of Stay Restrictions** — Set minimum/maximum stay requirements
- **Close to Arrival/Departure** — Restrict arrivals or departures on specific dates
- **Channel Management** — Configure different rates and restrictions per channel
- **Revenue Forecasting** — Predict revenue based on current bookings and historical data

**Key Reports**:
- **RevPAR Report** — Revenue Per Available Room
- **Channel Performance** — Compare revenue and bookings by channel

---

### 6. Housekeeping

**Purpose**: Streamline room cleaning operations and ensure rooms are ready for guests on time.

**Features**:
- **Room Status Management** — Track room statuses:
  - Vacant Clean / Vacant Dirty
  - Occupied Clean / Occupied Dirty
  - Inspected / Out of Order
  - Do Not Disturb
- **Task Assignment** — Assign housekeepers to specific rooms or floors
- **Cleaning Schedules** — Schedule daily, checkout, and deep cleaning tasks
- **Amenity Restocking** — Track and replenish room amenities and supplies
- **Lost & Found** — Record and manage lost items found in rooms
- **Inspection Tracking** — Supervisors can inspect rooms and mark them as ready
- **Housekeeping Status Report** — Real-time dashboard of all room statuses

**Workspace**: Dedicated Housekeeping workspace for daily operations

---

### 7. Hotel Maintenance

**Purpose**: Track, manage, and resolve maintenance issues across the property.

**Features**:
- **Maintenance Requests** — Log requests from guests and staff:
  - Issue type (Plumbing, Electrical, HVAC, Carpentry, Painting, etc.)
  - Priority (Low, Medium, High, Critical)
  - Location (room number, public area, facility)
  - Description and photos
- **Work Orders** — Convert requests into assignable work orders
- **Staff Assignment** — Assign maintenance staff and track completion
- **Scheduled Maintenance** — Plan preventive maintenance for equipment and facilities
- **Inventory Tracking** — Track spare parts and maintenance supplies
- **Cost Tracking** — Record labor and material costs per task

**Events**:
- `on_update` — Triggers notifications when maintenance status changes

---

### 8. Food & Beverage (F&B)

**Purpose**: Manage all food and beverage operations including restaurants, bars, room service, and banquets.

**Features**:
- **Restaurant Management** — Manage multiple outlets (Restaurants, Bars, Cafes, Pool Bars)
- **Menu Management** — Create and manage menu items with:
  - Item categories (Appetizers, Mains, Desserts, Beverages)
  - Pricing and tax configurations
  - Dietary tags (Vegetarian, Vegan, Gluten-Free)
  - Availability schedules
- **Table Management** — Floor plan with table statuses (Available, Reserved, Occupied, Billed)
- **Order Management** — Take orders with item modifiers and special instructions
- **KOT (Kitchen Order Ticket)** — Auto-print orders to designated kitchen printers
- **Billing** — Generate bills, split bills, and post charges to room folios
- **Room Service** — Handle in-room dining orders linked to reservations
- **Inventory Integration** — Link menu items to inventory for cost tracking

**Key Reports**:
- **F&B Cost vs Revenue** — Analyze food cost percentages and profitability

---

### 9. Events Management

**Purpose**: Manage event venues, bookings, and catering for conferences, weddings, banquets, and meetings.

**Features**:
- **Event Venues** — Manage bookable spaces (Ballrooms, Conference Rooms, Banquet Halls, Outdoor Spaces)
- **Venue Details** — Capacity, layout options, equipment, pricing
- **Event Bookings** — Create and manage event reservations with:
  - Event type (Wedding, Conference, Birthday, Corporate Event)
  - Guest count and seating arrangements
  - Catering and menu selection
  - Audio/visual equipment requirements
  - Timeline and schedule
- **Catering Management** — Select menus and beverage packages for events
- **Billing & Invoicing** — Generate invoices with deposits, payments, and balances
- **Calendar View** — Visual overview of venue bookings
- **Event Reports** — Summaries of upcoming events and revenue

**Workspace**: Dedicated Events workspace with calendar and booking tools

---

### 10. Spa & Recreation

**Purpose**: Manage spa services, treatment rooms, therapists, and recreational activities.

**Features**:
- **Spa Rooms** — Define treatment rooms with capacity and amenities
- **Treatment Packages** — Create treatment menus:
  - Categories (Massage, Facial, Body Treatment, Manicure/Pedicure)
  - Duration and pricing
  - Required therapist skills
  - Products used
- **Therapist Management** — Manage therapist profiles, specialties, and schedules
- **Booking & Scheduling** — Book appointments with calendar-based scheduling
- **Retail Products** — Sell spa products and retail items
- **Recreation Activities** — Manage activities (Yoga, Pilates, Fitness Classes, Guided Tours)
- **Guest Posting** — Post charges to guest folios or accept POS payments

---

### 11. Golf Management

**Purpose**: Complete management of golf course operations from tee times to caddies.

**DocTypes**:
- **Golf Course** — Define courses with hole count, par, difficulty rating, and amenities
- **Tee Time** — Schedule and manage tee time bookings with player limits
- **Caddy** — Manage caddy profiles, availability, and assignments

**Features**:
- Tee time booking with time-slot management
- Caddy assignment and tracking
- Green fee management with dynamic pricing
- Golf cart rental tracking
- Tournament management
- Player handicap tracking
- Post charges to guest folio or direct billing

---

### 12. Theme Park Management

**Purpose**: Manage theme park attractions, ticketing, and visitor experiences.

**Features**:
- **Attraction Management** — Define rides, shows, and attractions with:
  - Capacity and height/age restrictions
  - Operating hours and maintenance schedules
  - Queue management
- **Ticketing** — Create ticket types (Single Day, Multi-Day, Season Pass, VIP Express)
- **Entry Management** — Track park entries and capacity
- **Fast Pass / Queue Management** — Manage virtual queue systems
- **Concessions & Retail** — Link to F&B and retail modules

---

### 13. Cinema Management

**Purpose**: Manage movie scheduling, ticketing, and concessions for in-house or standalone cinemas.

**Features**:
- **Screen Management** — Define screens with seating capacity and technical specs
- **Movie Scheduling** — Schedule movies with showtimes
- **Ticket Sales** — Sell tickets with seat selection
- **Concessions** — Link to F&B module for snack and beverage sales
- **Loyalty Integration** — Offer discounts to members and guests

---

### 14. Marina Management

**Purpose**: Manage marina operations including berth/slip booking and boat services.

**Features**:
- **Berth/Slip Management** — Define berths with boat size, power, and water hookups
- **Boat Registration** — Register guest and member boats
- **Berth Booking** — Reserve berths with arrival/departure dates
- **Fuel & Pump Out** — Track fuel sales and waste pump-out services
- **Storage** — Winter storage and dry dock management
- **Billing** — Charges for berth rental, utilities, and services

---

### 15. Cruise Management

**Purpose**: Manage cruise itinerary, cabin bookings, and onboard services.

**Features**:
- **Cruise Ships** — Define ships with cabin categories and capacities
- **Itineraries** — Create cruise routes with ports of call and durations
- **Cabin Booking** — Manage cabin assignments and categories
- **Onboard Services** — Manage excursions, dining, and entertainment bookings
- **Shore Excursions** — Offer and book port activities
- **Guest Manifest** — Track all passengers and crew

---

### 16. Campsite Management

**Purpose**: Manage campsite pitches, outdoor activities, and camping reservations.

**DocTypes**:
- **Campsite Pitch** — Define pitches with size, utilities (electric/water), and capacity
- **Activity** — Manage outdoor activities (Hiking, Kayaking, Fishing, etc.)

**Features**:
- Pitch booking with dates and guest count
- Equipment rental (tents, camping gear, kayaks)
- Activity scheduling with guide assignment
- Group camping and event bookings
- Utility usage tracking (electricity, water)

---

### 17. Sports Complex

**Purpose**: Manage sports facilities, bookings, and equipment rental.

**Features**:
- **Facility Management** — Courts (Tennis, Basketball, Squash), Fields, Pools, Gyms
- **Time Slot Booking** — Reserve facilities by time slot
- **Equipment Rental** — Rent sports equipment and gear
- **Membership Access** — Restrict access by membership plan
- **Coaching/Training** — Book personal trainers and coaching sessions
- **Tournaments** — Organize and manage tournaments and events

---

### 18. Finance

**Purpose**: Comprehensive financial management tailored for hospitality operations.

**Features**:
- **Guest Folios** — Manage guest accounts with:
  - Room charges
  - F&B charges posted from outlets
  - Spa and recreation charges
  - Telephone and mini-bar charges
  - Laundry and other incidentals
- **Night Audit** — Automated end-of-day process that:
  - Posts daily room charges to folios
  - Reconciles payments and adjustments
  - Generates the Night Audit Report
  - Updates room statuses
  - Closes the business day
- **Invoice Management** — Generate invoices for guests, groups, and corporate accounts
- **Payment Reconciliation** — Match payments from OTA and direct bookings
- **Overdue Tracking** — Automatic flagging of overdue invoices (daily scheduled task)
- **Multi-Property** — Consolidate financial data across multiple properties

**Key Reports**:
- **Night Audit Report** — End-of-day financial summary
- **Revenue by Department** — Revenue breakdown across all departments
- **Guest Folio Summary** — Detailed guest billing statements

**Automated Tasks**:
- `flag_overdue_invoices` — Daily check for overdue payments

---

### 19. HR & Staffing

**Purpose**: Manage hospitality workforce including scheduling, attendance, and performance.

**Features**:
- **Staff Profiles** — Employee records with department, role, and skills
- **Shift Scheduling** — Create and manage shifts across all departments
- **Attendance** — Track attendance and time-off
- **Department Management** — Organize staff by department (Front Office, Housekeeping, F&B, Maintenance, etc.)
- **Training Records** — Track certifications and training completion
- **Performance Reviews** — Conduct and record staff evaluations

---

### 20. Membership Management

**Purpose**: Manage membership plans, loyalty programs, and member benefits.

**Features**:
- **Membership Plans** — Define tiers (Silver, Gold, Platinum, Diamond) with benefits:
  - Room upgrade eligibility
  - Discount percentages
  - Free nights and services
  - Priority check-in/check-out
  - Lounge access
- **Member Management** — Enroll, renew, upgrade, and downgrade members
- **Points System** — Award and redeem loyalty points
- **Benefits Tracking** — Track usage of member benefits
- **Expiry Alerts** — Automatic notifications for upcoming expirations

**Key Reports**:
- **Membership Expiry Report** — Track upcoming and past expirations

---

### 21. Concierge Services

**Purpose**: Provide personalized guest services and arrange external experiences.

**Features**:
- **Service Requests** — Manage guest requests for:
  - Restaurant reservations (external)
  - Tour bookings (city tours, cultural experiences)
  - Transportation (taxis, limousines, rentals)
  - Event tickets (theatre, concerts, sports)
  - Special arrangements (flowers, gifts, decorations)
- **Vendor Management** — Coordinate with external service providers
- **Booking Calendar** — Visual overview of all concierge bookings
- **Charges & Commissions** — Track service charges and vendor commissions

---

### 22. Security Management

**Purpose**: Manage property security, access control, and incident reporting.

**Features**:
- **Access Control** — Manage key cards, digital keys, and restricted areas
- **Incident Reporting** — Log and track security incidents:
  - Incident type (Theft, Disturbance, Medical, Fire, Accident)
  - Location, time, and persons involved
  - Resolution and follow-up actions
- **Visitor Management** — Register and track property visitors
- **Lost & Found** — Track lost items reported and found
- **Patrol Management** — Log security patrols and checkpoints
- **Surveillance Integration** — Log CCTV footage references for incidents

**Key Reports**:
- **Incident Summary Report** — Security incident analysis and trends

---

### 23. Sustainability

**Purpose**: Track and report environmental impact to support green hospitality initiatives.

**Features**:
- **Energy Tracking** — Monitor electricity, gas, and water consumption
- **Waste Management** — Track waste generation and recycling rates
- **Carbon Footprint** — Calculate and report carbon emissions
- **Green Initiatives** — Log sustainability projects (solar panels, water conservation, waste reduction)
- **Goal Setting** — Set and track environmental targets
- **Compliance Reporting** — Generate reports for environmental certifications (LEED, Green Key, Green Globe)

**Key Reports**:
- **Monthly Environmental Impact Report** — Period-over-period environmental metrics

---

### 24. Notification System

**Purpose**: Central notification engine that powers alerts across all modules.

**Features**:
- **In-App Notifications** — Real-time alerts within ERPNext
- **Email Notifications** — Automated email alerts for key events
- **SMS Alerts** — Text message notifications (with gateway integration)
- **Notification Triggers** — Configurable events:
  - Reservation confirmations and reminders
  - Check-in/out alerts
  - Housekeeping task assignments
  - Maintenance request updates
  - Payment confirmations
  - Membership expiry warnings
  - Security alerts
  - Overdue invoice notifications

---

## 📊 Reports & Analytics

The system includes a comprehensive reporting suite across all modules:

| Report Name | Module | Description |
|-------------|--------|-------------|
| **Occupancy Report** | Reservations | Occupancy rates by date, room type, property |
| **RevPAR Report** | Revenue Management | Revenue Per Available Room analysis |
| **Night Audit Report** | Finance | End-of-day financial summary |
| **Revenue by Department** | Finance | Revenue breakdown across all departments |
| **Guest Folio Summary** | Finance | Detailed guest billing statements |
| **F&B Cost vs Revenue** | F&B | Food cost percentages and profitability |
| **Housekeeping Status** | Housekeeping | Real-time room cleanliness status |
| **No Show & Cancellation Report** | Reservations | Booking loss patterns and analysis |
| **Membership Expiry Report** | Membership | Upcoming and expired memberships |
| **Channel Performance** | Revenue Management | Revenue/bookings by distribution channel |
| **Daily Visitor Log** | Security | Daily visitor entries and exits |
| **Guest Feedback Summary** | Guest CRM | Guest satisfaction scores and trends |
| **Facility Usage Summary** | Sports/Events | Utilization rates of facilities |
| **Incident Summary Report** | Security | Incident analysis and trends |
| **Monthly Environmental Impact** | Sustainability | Environmental metrics period-over-period |
| **Transport Schedule** | Concierge | Vehicle and transport bookings |
| **Valet Occupancy** | Property/Security | Parking occupancy and usage |

---

## ⏰ Automated Tasks & Schedules

The following tasks run automatically via the scheduler:

| Task | Schedule | Module | Purpose |
|------|----------|--------|---------|
| **Night Audit** | Daily | Revenue Management | Close business day, post charges, reconcile |
| **Check-in Reminders** | Daily | Reservations | Notify upcoming guests of arrival |
| **Check-out Reminders** | Daily | Reservations | Remind departing guests of checkout |
| **Overdue Invoice Flagging** | Daily | Finance | Flag accounts with overdue payments |

---

## 🧪 Demo Data Setup

To quickly populate the system with sample data for demonstration or testing:

### Using the Setup Script

Open the Frappe Console on your site:

```bash
bench --site your-site console
```

Then run:

```python
from hospitality_erp.scripts.setup_demo_data import setup_demo_data
setup_demo_data()
```

This interactive script will guide you through creating demo data for all modules, including:
- Properties, rooms, and rate plans
- Guest profiles with varied demographics
- Reservations (past, current, future, and cancelled)
- F&B menu items and restaurant setups
- Housekeeping schedules and tasks
- Maintenance requests
- And more

### Verification

After setup, you can verify by navigating to any workspace and checking that records exist.

---

## ❓ Troubleshooting & FAQ

### Installation Issues

**Q: The app doesn't appear after installation.**
> Run `bench --site your-site migrate` followed by `bench clear-cache` and refresh.

**Q: "Module Not Found" error for hospitality_erp.**
> Ensure the app is installed on your site: `bench --site your-site install-app hospitality_erp`

**Q: Workspace icons are not showing.**
> Run `bench build` to rebuild the assets, then clear your browser cache.

### Operational Issues

**Q: Night audit is not running automatically.**
> Check that the scheduler is enabled: `bench --site your-site enable-scheduler` and that the nightly jobs are active.

**Q: Reservation confirmation emails are not sending.**
> Verify your email domain is configured in ERPNext under `Settings > Email Domain`.

**Q: Room status is not updating after checkout.**
> This typically happens if the reservation was cancelled instead of properly checked out. Ensure the checkout process is followed.

**Q: F&B charges are not posting to guest folio.**
> Verify the guest's reservation is linked correctly in the POS/order screen.

### Reporting Issues

**Q: Reports show no data.**
> Ensure the site has been migrated and that the scheduler has run at least once. You may need to run the Night Audit manually for the first time.

**Q: Demo data script fails.**
> Ensure no existing data conflicts exist. Run with `--force` flag if available, or clear existing demo data first.

---

## 📞 Support

For issues, feature requests, and contributions:

- **GitHub Repository**: [github.com/balaji-001-gif/hospitality-management](https://github.com/balaji-001-gif/hospitality-management)
- **Issue Tracker**: Open an issue on the GitHub repository
- **Documentation**: See individual module JSON files in each module folder for field-level details

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License.

---

<div align="center">
  <br>
  <p><strong>Built with ❤️ for the Hospitality Industry</strong></p>
  <p><em>Powered by ERPNext v15+</em></p>
  <br>
</div>
