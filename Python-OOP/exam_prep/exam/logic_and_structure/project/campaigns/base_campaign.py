from abc import ABC, abstractmethod
from typing import List

from project.influencers.base_influencer import BaseInfluencer


class BaseCampaign(ABC):
    USED_IDS = set()

    def __init__(self, campaign_id: int, brand: str, budget: float,
                 required_engagement: float) -> None:
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers: List[BaseInfluencer] = []

    @property
    def campaign_id(self) -> int:
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value: int) -> None:
        if value <= 0:
            raise ValueError(
                "Campaign ID must be a positive integer greater than zero.")
        elif value in self.USED_IDS:
            raise ValueError(f"Campaign with ID {value} already exists."
                             f" Campaign IDs must be unique.")
        self.USED_IDS.add(value)
        self.__campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float) -> bool:
        pass
