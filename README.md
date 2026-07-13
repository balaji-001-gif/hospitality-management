# 🏨 Hospitality & Leisure ERP — Customer User Guide
> **Your all-in-one management platform for Hotels, Restaurants, Spas, Gyms, Events, and more — built on ERPNext v15 / Frappe v15.**
---
## 📋 Table of Contents
1. [Getting Started](#-getting-started)
2. [Hotel Management](#-hotel-management)
3. [Restaurant & Dining](#-restaurant--dining)
4. [Spa & Wellness](#-spa--wellness)
5. [Gym & Fitness](#-gym--fitness)
6. [Events & Venues](#-events--venues)
7. [Attractions](#-attractions)
8. [Entertainment](#-entertainment)
9. [Campsite Management](#-campsite-management)
10. [Marina Management](#-marina-management)
11. [Cruise Management](#-cruise-management)
12. [Sports & Recreation](#-sports--recreation)
13. [Finance & Billing](#-finance--billing)
14. [Hospitality Setup](#-hospitality-setup)
15. [Notifications & Alerts](#-notifications--alerts)
16. [Frequently Asked Questions](#-frequently-asked-questions)
17. [Support](#-support)
---
## 🚀 Getting Started
### What is Hospitality & Leisure ERP?
The **Hospitality & Leisure ERP** is a comprehensive, integrated management system designed specifically for hospitality and leisure businesses. Whether you operate a boutique hotel, a full-service resort, a day spa, or a multi-venue entertainment complex, this solution centralises all your operations into a single, user-friendly platform.
### System Requirements
| Requirement | Details |
|---|---|
| **Platform** | Frappe v15 / ERPNext v15 |
| **Browser** | Chrome 90+, Firefox 88+, Edge 90+, Safari 14+ |
| **Internet** | Stable broadband connection recommended |
### First-Time Login
1. Open your browser and navigate to your ERP URL (e.g., `https://yourcompany.erpnext.com`)
2. Enter your **Username** (usually your work email) and **Password** provided by your administrator
3. On first login, you will be prompted to change your password — choose a strong, unique password
4. Select your **Hospitality & Leisure** workspace from the home dashboard
> 💡 **Tip:** Bookmark your ERP URL for quick access. You can also add it to your mobile home screen for a near-app experience.
---
## 🏨 Hotel Management
The **Hotel** module handles everything from property setup to guest checkout.
### Key Features at a Glance
| Feature | What You Can Do |
|---|---|
| **Properties** | Define and manage your hotel properties, floors, and wings |
| **Room Types** | Configure room categories (Standard, Deluxe, Suite, etc.) with amenities and rates |
| **Rooms** | Set up individual rooms, assign room types, and track housekeeping status |
| **Guest Profiles** | Maintain a rich database of guest preferences, history, and contact details |
| **Reservations** | Create, modify, and cancel bookings with real-time availability checks |
| **Guest Folio** | Track all charges (room, F&B, spa, etc.) on a single consolidated bill |
---
### 1. Setting Up a Property
1. Navigate to **Hotel → Property**
2. Click **New**
3. Fill in:
   - **Property Name** — Your hotel/resort name
   - **Address** — Full postal address
   - **Contact Details** — Phone, email, website
4. Click **Save**
---
### 2. Creating Room Types
1. Go to **Hotel → Room Type**
2. Click **New**
3. Enter:
   - **Room Type Name** (e.g., *Deluxe King*, *Ocean Suite*)
   - **Base Rate** — Default nightly rate
   - **Capacity** — Max occupancy (adults + children)
   - **Amenities** — Select applicable amenities (Wi-Fi, minibar, balcony, etc.)
4. **Save** the record
---
### 3. Adding Rooms
1. Navigate to **Hotel → Room**
2. Click **New**
3. Specify:
   - **Room Number**
   - **Floor / Wing**
   - **Room Type** — links to your Room Type record
   - **Status** — Available / Occupied / Maintenance
4. **Save**
---
### 4. Creating a Reservation
1. Go to **Hotel → Reservation**
2. Click **New**
3. Fill in the reservation form:
   - **Guest** — Select an existing guest profile or create a new one
   - **Check-In Date** and **Check-Out Date**
   - **Room Type** — The system will automatically show available rooms
   - **Room** — Select a specific room
   - **Number of Adults / Children**
   - **Special Requests** — Dietary needs, accessibility, early check-in, etc.
4. Click **Save**, then **Confirm Reservation**
5. The system will send an automated confirmation email to the guest
> ⚠️ **Note:** Room availability is checked in real-time. If a room is already booked for the selected dates, it will not appear in the dropdown.
---
### 5. Managing the Guest Folio
The **Guest Folio** consolidates all charges for a guest during their stay.
1. Navigate to **Hotel → Guest Folio**
2. Locate the folio by **Guest Name** or **Reservation ID**
3. You can:
   - **Add Charges** — Post restaurant bills, spa appointments, or miscellaneous charges
   - **Apply Discounts** — Add promotional or loyalty discounts
   - **View Balance** — See real-time outstanding amount
   - **Settle Bill** — Choose payment method (Cash, Card, Bank Transfer, Company Account)
4. On checkout, click **Close Folio** to generate the final invoice
---
### 6. Guest Profile Management
1. Go to **Hotel → Guest Profile**
2. Use the **Search** bar to find existing guests or click **New** to add one
3. Key fields:
   - **Full Name**, **Date of Birth**, **Nationality**
   - **ID / Passport Number** (for compliance)
   - **Contact** — Email and phone
   - **Preferences** — Room preferences, dietary requirements, loyalty tier
4. All future reservations will auto-link to this profile, building a complete stay history
---
## 🍽️ Restaurant & Dining
The **Restaurant** module manages your dining outlets, menus, table orders, and kitchen workflow.
### Key Features
| Feature | What You Can Do |
|---|---|
| **Restaurant Outlets** | Define multiple dining outlets (main restaurant, pool bar, room service, etc.) |
| **Restaurant Tables** | Set up table layouts with seating capacity |
| **Menu Items** | Create and manage your menu with categories, prices, and allergen info |
| **Recipes** | Link menu items to standard recipes for cost control |
| **Food Orders** | Take dine-in, takeaway, or room-service orders |
---
### 1. Setting Up an Outlet
1. Navigate to **Restaurant → Restaurant Outlet**
2. Click **New** and enter:
   - **Outlet Name** (e.g., *The Terrace*, *Poolside Bar*)
   - **Outlet Type** — Fine Dining / Casual / Bar / Room Service
   - **Operating Hours**
3. **Save**
---
### 2. Creating a Food Order
1. Go to **Restaurant → Food Order**
2. Click **New**
3. Select:
   - **Outlet** — Choose the restaurant or bar
   - **Table** — For dine-in orders
   - **Guest / Customer** — Link to a hotel guest folio if applicable
4. Click **Add Items** and search your menu
5. Specify **Quantity** and any **Special Instructions** (e.g., *no nuts*, *extra spicy*)
6. Click **Place Order** — the Kitchen Display System (KDS) / printer will receive the order automatically
7. Once served, click **Mark as Served**
8. To settle: click **Settle**, choose payment method, and generate the receipt
---
### 3. Managing the Menu
1. Navigate to **Restaurant → Menu Item**
2. Click **New** to add a dish:
   - **Item Name**, **Category** (Starter, Main, Dessert, Beverage)
   - **Price** and **Tax Rate**
   - **Allergens** — Flag common allergens
   - **Available** toggle — Quickly 86 an item when out of stock
3. **Save**
---
## 💆 Spa & Wellness
The **Spa** module handles appointments, treatments, therapists, and spa room scheduling.
### Key Features
| Feature | What You Can Do |
|---|---|
| **Treatment Packages** | Define services (massages, facials, body wraps, packages) with duration and pricing |
| **Therapists** | Manage therapist profiles, specialisations, and schedules |
| **Spa Rooms** | Configure treatment rooms with equipment and availability |
| **Spa Appointments** | Book, reschedule, and cancel guest appointments |
---
### Booking a Spa Appointment
1. Go to **Spa → Spa Appointment**
2. Click **New**
3. Fill in:
   - **Guest** — Select guest profile
   - **Treatment Package** — Choose the service
   - **Therapist** — Select preferred therapist (optional)
   - **Spa Room** — Select an available room
   - **Date & Time** — The system checks therapist and room availability
4. Click **Save**, then **Confirm Appointment**
5. An automated reminder will be sent to the guest before the appointment
---
## 🏋️ Gym & Fitness
The **Gym** module manages memberships, fitness classes, and member activity.
### Key Features
| Feature | What You Can Do |
|---|---|
| **Membership Plans** | Create Daily, Monthly, Annual, and Corporate plans |
| **Gym Memberships** | Enrol members, track start/end dates, and manage renewals |
| **Fitness Classes** | Schedule group classes (yoga, HIIT, aqua aerobics, etc.) |
---
### Enrolling a New Member
1. Navigate to **Gym → Gym Membership**
2. Click **New**
3. Select:
   - **Member** — Link to guest profile or create a new contact
   - **Membership Plan** — Choose plan type and duration
   - **Start Date** — The system auto-calculates the expiry date
4. Click **Save** and then **Activate Membership**
5. The member will receive a welcome email with their membership details
> 💡 **Tip:** The system sends automatic expiry alerts 7 days before a membership expires, giving members time to renew.
---
### Scheduling a Fitness Class
1. Go to **Gym → Fitness Class**
2. Click **New**
3. Enter:
   - **Class Name** (e.g., *Morning Yoga*, *Power HIIT*)
   - **Instructor**
   - **Schedule** — Day(s) and time
   - **Max Capacity** — Maximum participants
4. **Save** — Members can be registered against class sessions
---
## 🎉 Events & Venues
The **Events** module manages venue bookings, corporate events, weddings, and private functions.
### Key Features
| Feature | What You Can Do |
|---|---|
| **Event Venues** | Configure ballrooms, conference rooms, outdoor spaces with capacity and rates |
| **Event Bookings** | Create bookings with event type, setup requirements, and billing |
---
### Creating an Event Booking
1. Navigate to **Events → Event Booking**
2. Click **New**
3. Fill in:
   - **Event Name** (e.g., *Johnson Wedding Reception*)
   - **Event Type** — Wedding / Corporate / Birthday / Conference
   - **Venue** — Select the configured venue
   - **Date & Time** — Start and end times
   - **Expected Attendance**
   - **Setup Requirements** — Theatre / Classroom / Banquet / Cocktail style
   - **Client** — Link to guest profile or company
4. Add **Services** (catering, A/V, décor) as line items
5. **Save** and generate a quotation for the client
6. On client confirmation, click **Confirm Booking**
---
## 🎡 Attractions
The **Attractions** module manages ticketed attractions, entry passes, and visitor experience.
- Create and manage **attraction listings** with descriptions, operating hours, and pricing
- Issue **entry tickets** to guests (linked to their folio for seamless billing)
- Track **daily visitor counts** and revenue
---
## 🎭 Entertainment
The **Entertainment** module handles shows, performances, and in-house entertainment programming.
- Schedule **entertainment events** (live music, shows, cultural performances)
- Manage **performer / vendor contracts**
- Sell **advance tickets** and track attendance
---
## ⛺ Campsite Management
The **Campsite** module manages pitches, glamping sites, and outdoor accommodation.
- Set up **Pitches** (tent, caravan, glamping pod) with amenities and pricing
- Accept **campsite reservations** with check-in/out management
- Track **pitch availability** in real time
---
## ⛵ Marina Management
The **Marina** module handles berth management, boat storage, and marine services.
- Manage **berths** with size, type, and daily/monthly rates
- Record **boat registrations** linked to guest profiles
- Process **marina bills** including fuel, maintenance, and storage charges
---
## 🚢 Cruise Management
The **Cruise** module manages cruise bookings, cabin allocation, and itinerary scheduling.
- Configure **cruise itineraries** with port schedules
- Create **cabin types** with deck, class, and pricing
- Process **cruise bookings** and generate boarding passes
---
## 🏸 Sports & Recreation
The **Sports** module manages court and facility bookings for tennis, squash, padel, and other sports.
- Set up **Sport Courts** with surface type, lighting options, and hourly rates
- Accept **court bookings** with time-slot management
- Track **utilisation reports** to optimise scheduling
### Booking a Sport Court
1. Go to **Sports → Sport Court**
2. Select the desired court
3. Click **New Booking**
4. Choose **Date**, **Start Time**, and **Duration**
5. Link to a **Guest** or walk-in customer
6. **Confirm** and issue a booking receipt
---
## 💰 Finance & Billing
The **Finance** module consolidates revenue across all departments and integrates with ERPNext accounting.
### Key Capabilities
- **Centralised Billing** — All charges (hotel, restaurant, spa, gym, events) roll up into a unified guest folio
- **Revenue Reports** — Daily, weekly, and monthly revenue breakdown by department
- **Invoice Generation** — Professional PDF invoices sent automatically via email
- **Payment Processing** — Cash, credit/debit card, bank transfer, and corporate accounts
- **Night Audit** — Automated daily audit run every night to post room charges and reconcile accounts
### Viewing Finance Reports
1. Navigate to **Finance → Reports**
2. Select a report type:
   - **Daily Revenue Summary**
   - **Departmental P&L**
   - **Outstanding Folios**
   - **Payment Collection Report**
3. Set your **Date Range** and click **Generate**
4. Export to **PDF** or **Excel** as needed
---
## ⚙️ Hospitality Setup
The **Hospitality Setup** module is where administrators configure the system for first use.
> ⚠️ **Admin Only:** This section is typically managed by your system administrator during initial setup.
Key setup tasks include:
- Defining **Property Types** and **Rate Plans**
- Configuring **Room Amenities**
- Setting up **Roles & Permissions** (Front Desk, Restaurant Manager, Spa Manager, Finance, etc.)
- Configuring **Email Notifications** and SMS alerts
---
## 🔔 Notifications & Alerts
The system sends automated notifications for key events:
| Trigger | Who Gets Notified |
|---|---|
| Reservation confirmed | Guest (email) |
| Reservation reminder | Guest (email), 24 hrs before check-in |
| Spa appointment reminder | Guest (email/SMS) |
| Gym membership expiring | Member (email), 7 days before expiry |
| Night audit completed | Finance team (email) |
| Room availability cache updated | System (internal, hourly) |
Notifications are configured in each module under the **Notification** sub-section. Contact your administrator to customise templates or add SMS/WhatsApp delivery channels.
---
## ❓ Frequently Asked Questions
**Q: Can I make a reservation for a guest without an existing profile?**
> Yes. When creating a Reservation, you can create a new Guest Profile on the fly using the **Quick Create** option in the Guest field.
**Q: How do I transfer charges from a restaurant bill to a guest's room folio?**
> When creating a Food Order, link the order to the **Guest** field. The charge will automatically be posted to the guest's active folio. Alternatively, use the **Transfer to Folio** button on a settled food order.
**Q: Can multiple guests share one room folio?**
> Yes. A folio can include charges for all guests in the same reservation. Additional guests can also be added from the Reservation record.
**Q: How do I apply a corporate or group discount?**
> On the Guest Folio, click **Add Discount**, select the type (Percentage / Fixed Amount / Complimentary), enter the value, and add a reason/approval reference.
**Q: What happens if a guest wants to extend their stay?**
> Open the **Reservation** record, update the **Check-Out Date**, and click **Save**. The system will check room availability for the extended period and update charges automatically.
**Q: How do I generate an end-of-day report?**
> Navigate to **Finance → Reports → Daily Revenue Summary**, set today's date, and click **Generate Report**.
**Q: Can I cancel a reservation?**
> Yes. Open the Reservation, click **Cancel**, and select a **Cancellation Reason**. Any applicable cancellation charges can be posted to the folio before cancellation.
**Q: Where do I configure tax rates for services?**
> Tax rates are managed in ERPNext's core **Tax Templates** section. Contact your administrator to set or adjust applicable taxes for each service type.
---
## 🆘 Support
If you encounter any issues or need assistance:
| Channel | Details |
|---|---|
| 📧 **Email Support** | info@yourorg.com |
| 📖 **ERPNext Docs** | [docs.erpnext.com](https://docs.erpnext.com) |
| 💬 **Frappe Community** | [discuss.frappe.io](https://discuss.frappe.io) |
| 🐛 **Bug Reports** | Open an issue on the [GitHub Repository](https://github.com/balaji-001-gif/hospitality-management) |
---
## 📌 Quick Reference — Module Map
```
Hospitality & Leisure ERP
├── 🏨 Hotel          → Property · Room Type · Room · Guest Profile · Reservation · Guest Folio
├── 🍽️  Restaurant     → Outlet · Table · Menu Item · Recipe · Food Order
├── 💆 Spa            → Treatment Package · Therapist · Spa Room · Spa Appointment
├── 🏋️  Gym            → Membership Plan · Gym Membership · Fitness Class
├── 🎉 Events         → Event Venue · Event Booking
├── 🎡 Attractions    → Attraction · Entry Tickets
├── 🎭 Entertainment  → Shows · Performances · Ticketing
├── ⛺ Campsite        → Pitch · Campsite Reservation
├── ⛵ Marina          → Berth · Boat Registration · Marina Billing
├── 🚢 Cruise          → Cabin Type · Cruise Itinerary · Cruise Booking
├── 🏸 Sports          → Sport Court · Court Booking
├── 💰 Finance         → Guest Folio · Invoices · Revenue Reports
└── ⚙️  Setup          → Property Types · Rate Plans · Roles · Notifications
```
---
> **Version:** 1.0.0 &nbsp;|&nbsp; **Platform:** Frappe v15 / ERPNext v15 &nbsp;|&nbsp; **License:** MIT
>
> *This user guide covers the standard features of the Hospitality & Leisure ERP. Some features may vary based on your organisation's configuration and installed modules.*
