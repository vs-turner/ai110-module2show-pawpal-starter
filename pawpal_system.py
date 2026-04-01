from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Dict, Optional

@dataclass
class CareTask:
    task_id: str
    pet_id: str
    type: str
    duration: int  # minutes
    priority: int
    deadline: Optional[datetime] = None
    status: str = "planned"

    def reschedule(self, new_time: datetime) -> None:
        pass

    def change_priority(self, new_priority: int) -> None:
        pass

    def mark_complete(self) -> None:
        pass

    def is_urgent(self) -> bool:
        pass

@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    health_conditions: List[str] = field(default_factory=list)
    routine: Dict[str, str] = field(default_factory=dict)

    def add_routine_task(self, task: CareTask) -> None:
        pass

    def update_health(self, condition: str) -> None:
        pass

    def get_daily_needs(self) -> List[CareTask]:
        pass

@dataclass
class Owner:
    owner_id: str
    name: str
    contact_info: str
    availability: Dict[str, List[str]] = field(default_factory=dict)
    preferences: Dict[str, str] = field(default_factory=dict)
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: str) -> None:
        pass

    def update_availability(self, blocks: Dict[str, List[str]]) -> None:
        pass

    def update_preferences(self, settings: Dict[str, str]) -> None:
        pass

class Scheduler:
    def __init__(self, owner: Owner, plan_date: date):
        self.owner = owner
        self.date = plan_date
        self.tasks: List[CareTask] = []
        self.time_slots: List[Dict[str, str]] = []
        self.explanation_log: List[str] = []

    def load_tasks(self, date: date) -> None:
        pass

    def generate_plan(self, constraints: Optional[Dict[str, str]] = None) -> None:
        pass

    def optimize_task_order(self) -> None:
        pass

    def explain_plan(self) -> str:
        pass

    def validate(self) -> bool:
        pass
