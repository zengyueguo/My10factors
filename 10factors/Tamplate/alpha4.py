def run_formula(dv):
    alpha4=dv.add_formula('alpha4','-Ts_Mean(turnover,20)/Ts_Mean(turnover,60)',is_quarterly=False,add_data=True)
    return alpha4