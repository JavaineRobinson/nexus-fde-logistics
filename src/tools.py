from langchain_core.tools import tool
from pydantic import BaseModel, Field

class InventoryCheckInput(BaseModel):
    sku_id: str = Field(description='Unique SKU identifier, e.g. SKU-9921')
    facility: str = Field(description='Target warehouse location, e.g. WH-EAST')

@tool(args_schema=InventoryCheckInput)
def check_inventory(sku_id: str, facility: str) -> str:
    """
    Query inventory balance and reorder threshold for a specific SKU."""
    return f"Inventory check for SKU {sku_id}: 42 units available. Reorder point: 50 units. Facility: {facility}."

@tool
def trigger_warehouse_reroute(shipment_id: str, destination_hub: str) -> str:
    """
    Reroute an urgent freight shipment to a different warehouse hub."""
    return f"Shipment {shipment_id} has been rerouted to {destination_hub}. Code: ROUTE-OK."