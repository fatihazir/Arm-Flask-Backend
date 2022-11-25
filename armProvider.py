from Apriori.apyori import apriori
import numpy as np
import pandas as pd


def AprioriRulesToList(rules, elementAmount, maxLength, minLength):
    products = []
    for i in range(maxLength):
        products.append([])

    support = []
    confidence = []
    lift = []

    for rule in rules:

        content = rule[0]
        items = [x for x in content]

        for i in range(maxLength):
            try:
                if (items[i]):
                    products[i].append(items[i])
            except:
                products[i].append(np.nan)

        support.append(float(rule[1]))
        confidence.append(float(rule[2][0][2]))
        lift.append(float(rule[2][0][3]))

    aprioriDf = {}

    for i in range(maxLength):
        aprioriDf[f"{i}"] = products[i]

    aprioriDf['Support'] = support
    aprioriDf['Confidence'] = confidence
    aprioriDf['Lift'] = lift

    aprioriDf = pd.DataFrame(data=aprioriDf)
    return aprioriDf[~aprioriDf[f"{minLength}"].isnull()].sort_values(by="Confidence", ascending=False).head(elementAmount).values.tolist()


def RunApriori(data, minSupport, maxLength, minLength, elementAmount):
    rulesForApriori = apriori(
        data,
        min_support=minSupport,
        max_length=maxLength)  # , min_confidence=0.8, min_lift = 2
    listedRulesForApriori = list(rulesForApriori)
    return AprioriRulesToList(listedRulesForApriori, elementAmount, maxLength, minLength)
