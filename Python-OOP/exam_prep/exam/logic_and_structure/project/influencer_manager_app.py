from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer,
                              "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGN_TYPES = {"HighBudgetCampaign": HighBudgetCampaign,
                            "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def find_influencer_by_username(self, username: str):
        try:
            return [i for i in self.influencers if i.username == username][0]
        except IndexError:
            return None

    def find_campaign_by_id(self, id_: int):
        try:
            return [c for c in self.campaigns if c.campaign_id == id_][0]
        except IndexError:
            return None

    def register_influencer(self, influencer_type: str, username: str,
                            followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        if self.find_influencer_by_username(username):
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username,
                                                                      followers,
                                                                      engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str,
                        required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        if self.find_campaign_by_id(campaign_id):
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id,
                                                                brand,
                                                                required_engagement)
        self.campaigns.append(new_campaign)
        return (f"Campaign ID {campaign_id} for {brand} is "
                f"successfully created as a {campaign_type}.")

    def participate_in_campaign(self, influencer_username: str,
                                campaign_id: int):
        influencer = self.find_influencer_by_username(influencer_username)
        campaign = self.find_campaign_by_id(campaign_id)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the "
                    f"eligibility criteria for the campaign "
                    f"with ID {campaign_id}.")

        payment_for_influencer = influencer.calculate_payment(campaign)
        if payment_for_influencer > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment_for_influencer
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}' has successfully "
                    f"participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        result = {}
        for campaign in self.campaigns:
            total_followers_reached = 0
            campaign_type = campaign.__class__.__name__
            if not campaign.approved_influencers:
                continue
            for influencer in campaign.approved_influencers:
                total_followers_reached += influencer.reached_followers(
                    campaign_type)
            result[campaign] = total_followers_reached
        return result

    def influencer_campaign_report(self, username: str):
        influencer = self.find_influencer_by_username(username)

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        total_followers = self.calculate_total_reached_followers()
        sorted_campaigns = sorted(self.campaigns, key=lambda x:
        (len(x.approved_influencers), -x.budget))
        result = "$$ Campaign Statistics $$"
        for campaign in sorted_campaigns:
            result += (f"\n  * Brand: {campaign.brand}, Total influencers: "
                       f"{len(campaign.approved_influencers)}, Total budget: "
                       f"${campaign.budget:.2f}, "
                       f"Total reached followers: {total_followers[campaign]}")
        return result
