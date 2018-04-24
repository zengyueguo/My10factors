def run_formula(dv):
    alpha7=dv.add_formula('alpha7',"-close/(Ts_Sum(vwap*turnover_ratio,100)/Ts_Sum(turnover_ratio,100))",is_quarterly=False,add_data=True)
    return alpha7
