#data_bundle_advisor.py
budget = float(input("Enter your budget (in Rands): "))

while budget <= 0:
    budget = float(input("Invalid budget.\nEnter your budget (in Rands): "))

usage_type = input("Enter your usage type (light, moderate, or heavy): ")
while usage_type != "light" and usage_type != "moderate" and usage_type != "heavy":
    usage_type = input("Invalid usage type.\nEnter your usage type (light, moderate, or heavy): ")

if usage_type == "light":
    if budget < 50:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\nNo suitable bundle")
    elif budget < 100:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\n500MB Bundle")
    else:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\n1GB Bundle")
        
elif usage_type == "moderate":
    if budget < 100:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\nNo suitable bundle")
    elif budget < 200:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\n2GB Bundle")
    else:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\n5GB Bundle")
else:
    if budget < 200:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\nNo suitable bundle")
    elif budget < 400:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\n10GB Bundle")
    else:
        print(f"\nFor R {budget:.0f} and {usage_type} usage type:\nUnlimited Bundle")

