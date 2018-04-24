def run_formula(dv):
    alpha2=dv.add_formula('alpha2','-(close_adj-Ts_Mean(close_adj,30))/StdDev(close_adj,30)',is_quarterly=False,add_data=True)
    return alpha2