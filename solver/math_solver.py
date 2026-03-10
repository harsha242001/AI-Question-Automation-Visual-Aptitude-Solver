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

        tpl = {
            "top_line": "Let the original CP be = rs x",
            "b1_top": f"MP at {m}%",
            "b1_bot": f"= {1+m/100:.2f} x",
            "b2_top": "CP",
            "b2_bot": "= x",
            "b3_top": f"SP (at {d}% D)",
            "b3_bot": f"= {factor:.2f} x",
            "b4_top": "P",
            "b4_bot": f"rs {profit}",
            "b4_frac_num": "",
            "b4_frac_den": "",
            "form_top": f"{factor:.2f} x - x",
            "form_bot": "",
            "cross": f"{factor-1:.2f} x = {profit}",
            "x_num": f"{profit}",
            "x_den": f"{factor-1:.2f}",
            "x_ans": f"rs {round(cp,2)}"
        }

        return round(cp,2), tpl


    # --------------------------------
    # marked price + discount + profit %
    # --------------------------------

    if "marked_price" in v and "discount_percent" in v and "profit_percents" in v:

        mp = v["marked_price"]
        d = v["discount_percent"]
        p = v["profit_percents"][0]

        sp = mp*(1-d/100)

        cp = sp/(1+p/100)

        tpl = {
            "top_line": "Let the original CP be = rs x",
            "b1_top": "MP",
            "b1_bot": f"= {mp}",
            "b2_top": f"SP (at {d}% D)",
            "b2_bot": f"= {mp} × {1-d/100:.2f} = {sp:.2f}",
            "b3_top": "CP",
            "b3_bot": "= x",
            "b4_top": "P",
            "b4_bot": f"{p}%",
            "b4_frac_num": f"{p}",
            "b4_frac_den": "100",
            "form_top": f"{sp:.2f} - x",
            "form_bot": "x",
            "cross": f"100 × ({sp:.2f} - x) = {p} × x",
            "x_num": f"{sp:.2f} × 100",
            "x_den": f"{100 + p}",
            "x_ans": f"rs {round(cp,2)}"
        }

        return round(cp,2), tpl


    # --------------------------------
    # chain selling
    # --------------------------------

    if "profit_percents" in v and "loss_percents" in v and "final_price" in v:

        p = v["profit_percents"][0]
        l = v["loss_percents"][0]
        fp = v["final_price"]

        factor = (1+p/100)*(1-l/100)

        cp = fp/factor

        tpl = {
            "top_line": "Let A's CP be = rs x",
            "b1_top": "A's SP / B's CP",
            "b1_bot": f"= {1+p/100:.2f} x",
            "b2_top": "B's SP (C's CP)",
            "b2_bot": f"= {factor:.2f} x",
            "b3_top": "Final Price",
            "b3_bot": f"= {fp}",
            "b4_top": "Difference",
            "b4_bot": f"= {(factor-1)*100:.1f}%",
            "b4_frac_num": "",
            "b4_frac_den": "",
            "form_top": f"{factor:.2f} x",
            "form_bot": "",
            "cross": f"{factor:.2f} x = {fp}",
            "x_num": f"{fp}",
            "x_den": f"{factor:.2f}",
            "x_ans": f"rs {round(cp,2)}"
        }

        return round(cp,2), tpl


    # --------------------------------
    # direct loss
    # --------------------------------

    if "cost_price" in v and "loss_percents" in v:

        cp = v["cost_price"]
        loss = v["loss_percents"][0]

        sp = cp*(1-loss/100)

        tpl = {
            "top_line": f"Given CP = rs {cp}",
            "b1_top": "CP",
            "b1_bot": f"= {cp}",
            "b2_top": f"Loss %",
            "b2_bot": f"= {loss}%",
            "b3_top": "Loss Amt",
            "b3_bot": f"= {cp * loss / 100}",
            "b4_top": "SP",
            "b4_bot": "= x",
            "b4_frac_num": "",
            "b4_frac_den": "",
            "form_top": f"{cp} - {cp * loss / 100}",
            "form_bot": "",
            "cross": f"x = {cp} - {cp * loss / 100}",
            "x_num": f"{sp}",
            "x_den": "",
            "x_ans": f"rs {round(sp,2)}"
        }

        return round(sp,2), tpl


    # --------------------------------
    # profit change case
    # --------------------------------

    if "profit_percents" in v and "price_change" in v:

        p1 = v["profit_percents"][0]
        p2 = v["profit_percents"][1]

        delta = v["price_change"]

        cp = delta/((1+p2/100)-(1+p1/100))

        tpl = {
            "top_line": "Let the original CP be = rs x",
            "b1_top": f"SP1 (at {p1}% P)",
            "b1_bot": f"= {1+p1/100:.2f} x",
            "b2_top": f"SP2 (at {p2}% P)",
            "b2_bot": f"= {1+p2/100:.2f} x",
            "b3_top": "Difference in SP",
            "b3_bot": f"= {delta}",
            "b4_top": "Difference %",
            "b4_bot": f"{(p2-p1)}%",
            "b4_frac_num": f"{p2-p1}",
            "b4_frac_den": "100",
            "form_top": f"{1+p2/100:.2f} x - {1+p1/100:.2f} x",
            "form_bot": "",
            "cross": f"{(p2-p1)/100:.2f} x = {delta}",
            "x_num": f"{delta}",
            "x_den": f"{(p2-p1)/100:.2f}",
            "x_ans": f"rs {round(cp,2)}"
        }

        return round(cp,2), tpl


    # --------------------------------
    # false weight
    # --------------------------------

    if "profit_percents" in v and "false_weight_percent" in v:

        p = v["profit_percents"][0]
        w = v["false_weight_percent"]

        profit = ((1+p/100)/(1-w/100)-1)*100

        tpl = {
            "top_line": "Let CP of 1kg = rs x",
            "b1_top": "Actual CP",
            "b1_bot": f"= {1-w/100:.2f} x",
            "b2_top": "Billed SP",
            "b2_bot": f"= {1+p/100:.2f} x",
            "b3_top": "Profit Amt",
            "b3_bot": f"= {(1+p/100)-(1-w/100):.2f} x",
            "b4_top": "Profit %",
            "b4_bot": "= y",
            "b4_frac_num": "",
            "b4_frac_den": "",
            "form_top": f"{(1+p/100)-(1-w/100):.2f} x",
            "form_bot": f"{1-w/100:.2f} x",
            "cross": f"y = ( {(1+p/100)-(1-w/100):.2f} x / {1-w/100:.2f} x ) × 100",
            "x_num": f"{(1+p/100)-(1-w/100):.2f} × 100",
            "x_den": f"{1-w/100:.2f}",
            "x_ans": f"{round(profit,2)}%"
        }

        return round(profit,2), tpl


    return None