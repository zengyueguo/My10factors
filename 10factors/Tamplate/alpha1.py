def run_formula(dv):
    alpha1=dv.add_formula('alpha1','-Ts_Mean(turnover_ratio,20)/StdDev(Log(close_adj/Delay(close_adj,1)),20)',is_quarterly=False,add_data=True)
    return alpha1
