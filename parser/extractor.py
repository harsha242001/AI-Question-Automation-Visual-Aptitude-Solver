import re

def extract_variables(question):

    q = question.lower()

    # remove symbols
    q = q.replace("₹","").replace("rs.","").replace("rs","").replace("â‚¹","")

    variables = {}

    # -------------------------
    # profit amount
    # -------------------------

    profit_amt = re.search(r'profit\s*(?:of)?\s*(\d+)(?!\s*%)', q)

    if profit_amt:
        variables["profit_amount"] = int(profit_amt.group(1))


    # -------------------------
    # profit %
    # -------------------------

    profits = re.findall(r'(\d+)\s*%\s*profit|profit\s*of\s*(\d+)%', q)

    profit_list = []

    for p in profits:
        if p[0]:
            profit_list.append(int(p[0]))
        elif p[1]:
            profit_list.append(int(p[1]))

    if profit_list:
        variables["profit_percents"] = profit_list


    # -------------------------
    # loss %
    # -------------------------

    losses = re.findall(r'(\d+)\s*%\s*loss|loss\s*(?:of|equal\s*to)?\s*(\d+)%', q)

    loss_list = []

    for l in losses:
        if l[0]:
            loss_list.append(int(l[0]))
        elif l[1]:
            loss_list.append(int(l[1]))

    if loss_list:
        variables["loss_percents"] = loss_list


    # -------------------------
    # markup %
    # -------------------------

    markup = re.search(r'(\d+)%\s*above', q)

    if markup:
        variables["markup_percent"] = int(markup.group(1))


    # -------------------------
    # discount %
    # -------------------------

    discount = re.search(r'(\d+)%\s*discount|discount\s*(?:of)?\s*(\d+)%', q)

    if discount:
        variables["discount_percent"] = int(discount.group(1) or discount.group(2))


    # -------------------------
    # marked price
    # -------------------------

    mp = re.search(r'marked\s*price\s*(?:of)?\s*(\d+)', q)

    if mp:
        variables["marked_price"] = int(mp.group(1))


    # -------------------------
    # price change
    # -------------------------

    change = re.search(r'(\d+)\s*(more|extra|less)', q)

    if change:
        variables["price_change"] = int(change.group(1))


    # -------------------------
    # final selling price
    # -------------------------

    final = re.search(r'pays\s*(\d+)', q)

    if final:
        variables["final_price"] = int(final.group(1))


    # -------------------------
    # false weight
    # -------------------------

    weight = re.search(r'(\d+)%\s*less\s*than\s*the\s*actual\s*weight', q)

    if weight:
        variables["false_weight_percent"] = int(weight.group(1))


    # -------------------------
    # direct cost price
    # -------------------------

    cp = re.search(r'article\s*at\s*(\d+)', q)

    if cp:
        variables["cost_price"] = int(cp.group(1))


    return variables