def run_formula(dv):
    alpha3=dv.add_formula('alpha3','-Ts_Mean(turnover_ratio,10)',is_quarterly=False,add_data=True)
    return alpha3