# 🚚 Fleet Management System

[![License](https://img.shields.io/github/license/AnojToppo/Fleet-Management)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![Frappe Version](https://img.shields.io/badge/frappe-14-green)](https://frappeframework.com/)

A **Fleet Management application** built on the **Frappe Framework** to manage drivers, vehicles, trips, and maintenance.  
This app provides a **fleet dashboard**, **number cards**, **charts**, and **API endpoints** for integration.

---

## 💡 Features

- **Driver Management** – Manage active/inactive drivers with custom statuses  
- **Vehicle Management** – Track vehicle availability and status  
- **Trip Management** – Record trips with drivers, distance, and timestamps  
- **Maintenance Management** – Track vehicle maintenance schedules  
- **Fleet Dashboard** – Visualize data with number cards and charts  
- **API Endpoints** – Access vehicle and trip data programmatically

---

## 📂 Doctypes and Relationships

| Doctype      | Key Purpose                               | Relationships                    |
|-------------|------------------------------------------|---------------------------------|
| Vehicle     | Vehicle details and status                | Linked to Trip and Maintenance  |
| Driver      | Driver details and active/inactive status | Linked to Trip                  |
| Trip        | Vehicle trips                             | Linked to Vehicle and Driver    |
| Maintenance | Vehicle maintenance logs                  | Linked to Vehicle               |

- Vehicles ↔ Trips (one-to-many)  
- Drivers ↔ Trips (one-to-many)  
- Vehicles ↔ Maintenance (one-to-many)  

---

## 📊 Fleet Dashboard

- **Number Cards:** Show totals for vehicles, drivers, trips, and maintenance  
- **Charts:**
  - Vehicle by status (Available vs In Service vs In Maintenance)  
  - Driver status (Active vs Inactive)  
  - Vehicle fuel type (Petrol vs Diesel vs Electric)  

---

## 🔌 API Endpoints

- **Get Available Vehicles**

```python
import frappe

@frappe.whitelist()
def get_available_vehicles():
    return frappe.get_all("Vehicle", filters={"status": "Available"})
```
```
@frappe.whitelist()
def get_trips_by_vehicle(vehicle):
    return frappe.get_all(
        "Trip",
        filters={"vehicle": vehicle},
        fields=["driver", "distance", "start_date_time", "end_date_time"]
    )
```

## Get the app from github
```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/AnojToppo/Fleet-Management.git --branch develop
bench --site motovehicle.localhost install-app fleet_management
bench --site motovehicle.localhost migrate 
```

## 🧩 Development

- Make changes in the `apps/fleet_management` folder  
- Export fixtures for Dashboard Charts, Custom Fields, and Property Setters:

```bash
bench --site motovehicle.localhost export-fixtures
```


### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/fleet_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
