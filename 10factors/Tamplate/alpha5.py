def run_formula(dv):
    alpha5=dv.add_formula('alpha5','-Correlation(Pow(Log(close_adj/Delay(close_adj,1)),2),vwap_adj,20)',is_quarterly=False,add_data=True)
    return alpha5