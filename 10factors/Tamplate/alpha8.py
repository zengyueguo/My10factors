def run_formula(dv):
    alpha8=dv.add_formula('alpha8','-Ts_Mean(close/vwap,10)',is_quarterly=False,add_data=True)
    return alpha8
