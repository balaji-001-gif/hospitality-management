import frappe
from hospitality_erp.scripts.setup_demo_data import setup_demo_data

def run_all():
	"""Main entry point for bench execute."""
	setup_demo_data()

if __name__ == "__main__":
	run_all()
