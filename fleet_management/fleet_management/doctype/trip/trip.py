# Copyright (c) 2026, anoj and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document

class Trip(Document):
    def validate(self):
        if self.end_odometer and self.start_odometer:
            self.distance = self.end_odometer - self.start_odometer