import numpy_financial as npf


def ask_float(question):
    return float(input(question).replace(",", "."))


def main():
    print("Business Case Tool\n")

    project_name = input("Naam business case: ")
    investment = ask_float("Initiële investering (€): ")
    annual_savings = ask_float("Jaarlijkse besparing (€): ")
    annual_extra_costs = ask_float("Jaarlijkse extra kosten (€): ")
    years = int(ask_float("Looptijd (jaren): "))
    discount_rate = ask_float("Discontovoet (%): ") / 100

    annual_net_savings = annual_savings - annual_extra_costs

    if investment != 0:
        total_benefit = annual_net_savings * years
        roi = (total_benefit - investment) / investment
    else:
        roi = None

    cashflows = [-investment] + [annual_net_savings] * years
    npv = npf.npv(discount_rate, cashflows)

    if annual_net_savings > 0:
        payback_period = investment / annual_net_savings
    else:
        payback_period = None

    fcp_savings_year1 = annual_net_savings - investment
    
    # Business conclusie
    if npv > 0 and (roi is not None and roi > 0):
        conclusion = "POSITIEVE BUSINESS CASE ✅"
    elif npv > 0:
        conclusion = "TWEEDE CHECK AANBEVOLEN ⚠️ (NPV positief, ROI zwakker)"
    else:
        conclusion = "NEGATIEVE BUSINESS CASE ❌"
    
    print("\n--- Samenvatting business case ---")
    print(f"Project: {project_name}")
    print(f"Netto jaarlijkse besparing: € {annual_net_savings:,.2f}")

    if roi is not None:
        print(f"ROI: {roi:.2%}")
    else:
        print("ROI: niet berekenbaar")

    print(f"NPV: € {npv:,.2f}")

    if payback_period is not None:
        print(f"Terugverdientijd: {payback_period:.2f} jaar")
    else:
        print("Terugverdientijd: niet berekenbaar")

    print(f"FCP Savings 1e jaar: € {fcp_savings_year1:,.2f}")

    print(f"\nConclusie: {conclusion}")


if __name__ == "__main__":
    main()