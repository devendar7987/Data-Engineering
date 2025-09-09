import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("bank_marketing.csv")

# --------------------------------------------------
# 1. CLIENT DATAFRAME
# --------------------------------------------------
client = df[[
    "client_id", "age", "job", "marital", 
    "education", "credit_default", "mortgage"
]].copy()

# Cleaning job: replace "." with "_"
client["job"] = client["job"].str.replace(".", "_")

# Cleaning education: replace "." with "_", change "unknown" -> NaN
client["education"] = client["education"].str.replace(".", "_")
client["education"] = client["education"].replace("unknown", np.NAN)

# Convert credit_default: "yes" → True, otherwise False
client["credit_default"] = client["credit_default"].apply(lambda x: True if x == "yes" else False)

# Convert mortgage: "yes" → True, otherwise False
client["mortgage"] = client["mortgage"].apply(lambda x: True if x == "yes" else False)

# --------------------------------------------------
# 2. CAMPAIGN DATAFRAME
# --------------------------------------------------
campaign = df[[
    "client_id", "number_contacts", "contact_duration",
    "previous_campaign_contacts", "previous_outcome",
    "campaign_outcome", "month", "day"
]].copy()

# Convert previous_outcome: "success" → True, otherwise False
campaign["previous_outcome"] = campaign["previous_outcome"].apply(lambda x: True if x == "success" else False)

# Convert campaign_outcome: "yes" → True, otherwise False
campaign["campaign_outcome"] = campaign["campaign_outcome"].apply(lambda x: True if x == "yes" else False)

# Create last_contact_date: combine year=2022 + month + day
campaign["year"] = "2022"
campaign["day"] = campaign["day"].astype("str")
campaign["last_contact_date"] = campaign["year"] + "-" + campaign["month"] + "-" + campaign["day"]
campaign["last_contact_date"] = pd.to_datetime(campaign["last_contact_date"], format="%Y-%b-%d")

# Drop unnecessary columns
campaign.drop(columns=["month", "day", "year"], inplace=True)

# --------------------------------------------------
# 3. ECONOMICS DATAFRAME
# --------------------------------------------------
economics = df[[
    "client_id", "cons_price_idx", "euribor_three_months"
]].copy()

# --------------------------------------------------
# SAVE TO CSV
# --------------------------------------------------
client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)
