def run_formula(dv):
    alpha9=dv.add_formula('alpha9','Ts_Mean((open_adj/Delay(close_adj,1))/(close/open),10)',is_quarterly=False,add_data=True)
    return alpha9