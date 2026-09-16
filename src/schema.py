from pydantic import BaseModel, Field
from typing import List

class ActionItem(BaseModel):
    action_type: str = Field(description='Action type: REROUTE, REORDER, or FLAG_DELAY.')
    target: str = Field(description= 'Associated SKU or Shipment ID')
    priority: str = Field(description='Priority level: HIGH, MEDIUM, LOW')

class LogisticsDispatchReport(BaseModel):
    summary: str = Field(description= 'Executive operational summary of status')
    confidence_score: float = Field(description='Confidence score between 0.0 and 1.0')
    actions: List[ActionItem]= Field(description='Reccomended operational dispatches')