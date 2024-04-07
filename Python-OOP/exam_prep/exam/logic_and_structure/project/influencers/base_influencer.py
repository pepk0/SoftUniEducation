from abc import ABC, abstractmethod


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int,
                 engagement_rate: float) -> None:
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        if not value.strip():
            raise ValueError(
                "Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self) -> int:
        return self.__followers

    @followers.setter
    def followers(self, value: int) -> None:
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self) -> float:
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value: float) -> None:
        if not 0 < value <= 5:
            raise ValueError("Engagement rate should be between 0 and 5.")
        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign) -> float:
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str) -> int:
        pass

    def display_campaigns_participated(self) -> str:
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        influencer_type = self.__class__.__name__
        result = (f"{influencer_type} :) {self.username} :) "
                  f"participated in the following campaigns:")
        for campaign in self.campaigns_participated:
            campaign_type = campaign.__class__.__name__
            result += (f"\n  - Campaign ID: {campaign.campaign_id}, "
                       f"Brand: {campaign.brand}, Reached followers: "
                       f"{self.reached_followers(campaign_type)}")
        return result
