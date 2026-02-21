import frappe

@frappe.whitelist()
def get_available_vehicles():
    return frappe.get_all("Vehicle", filters={"status": "Available"})

@frappe.whitelist()
def get_trips_by_vehicle(vehicle):
    return frappe.get_all(
        "Trip",
        filters={"vehicle": vehicle},
        fields=["driver", "distance", "start_date_time", "end_date_time"]
    )