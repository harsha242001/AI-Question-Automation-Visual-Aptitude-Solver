def solve(v):

    # --------------------------------
    # markup + discount + profit amount
    # --------------------------------

    if "markup_percent" in v and "discount_percent" in v and "profit_amount" in v:

        m = v["markup_percent"]
        d = v["discount_percent"]
        profit = v["profit_amount"]

        factor = (1+m/100)*(1-d/100)

        cp = profit/(factor-1)

        steps = [
            "Let CP = x",
            f"MP = (1+{m}/100)x",
            f"SP = MP × (1-{d}/100)",
            f"{round(factor,4)}x - x = {profit}",
            f"x = {round(cp,2)}"
        ]

        return round(cp,2), steps


    # --------------------------------
    # marked price + discount + profit %
    # --------------------------------

    if "marked_price" in v and "discount_percent" in v and "profit_percents" in v:

        mp = v["marked_price"]
        d = v["discount_percent"]
        p = v["profit_percents"][0]

        sp = mp*(1-d/100)

        cp = sp/(1+p/100)

        steps = [
            f"SP = {mp} × (1-{d}/100)",
            f"SP = {sp}",
            f"SP = (1+{p}/100)CP",
            f"CP = {round(cp,2)}"
        ]

        return round(cp,2), steps


    # --------------------------------
    # chain selling
    # --------------------------------

    if "profit_percents" in v and "loss_percents" in v and "final_price" in v:

        p = v["profit_percents"][0]
        l = v["loss_percents"][0]
        fp = v["final_price"]

        factor = (1+p/100)*(1-l/100)

        cp = fp/factor

        steps = [
            f"A sells at {p}% profit",
            f"B sells at {l}% loss",
            f"{round(factor,3)}CP = {fp}",
            f"CP = {round(cp,2)}"
        ]

        return round(cp,2), steps


    # --------------------------------
    # direct loss
    # --------------------------------

    if "cost_price" in v and "loss_percents" in v:

        cp = v["cost_price"]
        loss = v["loss_percents"][0]

        sp = cp*(1-loss/100)

        steps = [
            f"SP = {cp} × (1-{loss}/100)",
            f"SP = {round(sp,2)}"
        ]

        return round(sp,2), steps


    # --------------------------------
    # profit change case
    # --------------------------------

    if "profit_percents" in v and "price_change" in v:

        p1 = v["profit_percents"][0]
        p2 = v["profit_percents"][1]

        delta = v["price_change"]

        cp = delta/((1+p2/100)-(1+p1/100))

        steps = [
            f"SP1 = (1+{p1}/100)CP",
            f"SP2 = (1+{p2}/100)CP",
            f"SP difference = {delta}",
            f"CP = {round(cp,2)}"
        ]

        return round(cp,2), steps


    # --------------------------------
    # false weight
    # --------------------------------

    if "profit_percents" in v and "false_weight_percent" in v:

        p = v["profit_percents"][0]
        w = v["false_weight_percent"]

        profit = ((1+p/100)/(1-w/100)-1)*100

        steps = [
            f"SP factor = {1+p/100}",
            f"Weight factor = {1-w/100}",
            f"Profit % = {round(profit,2)}"
        ]

        return round(profit,2), steps


    return None