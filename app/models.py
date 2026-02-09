from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field, field_validator

class WorkflowStatus(StrEnum):
    received = "received"
    doc_requested = "doc_requested"
    doc_received = "doc_received"
    underwriting = "underwriting"
    approved = "approved"
    closing_scheduled = "closing_scheduled"
    closed = "closed"

class EventIn(BaseModel):
    event_id: str = Field(min_length=1)
    loan_id: str = Field(min_length=1)
    status: WorkflowStatus
    timestamp: datetime
    actor: Optional[str] = None
    notes: Optional[str] = None

    @field_validator("timestamp")
    @classmethod
    def ensure_timezone_aware(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError("timestamp must include timezone info (e.g. 'Z' or '-05:00')")
        return v.astimezone(timezone.utc)
    
    class IngestResult(BaseModel):
        stored: bool
