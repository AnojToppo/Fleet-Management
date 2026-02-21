# Copyright (c) 2026, anoj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Vehicle(Document):
    def validate(self):
        if not self.vehicle_no:
            frappe.throw("Vehicle Number is required!")