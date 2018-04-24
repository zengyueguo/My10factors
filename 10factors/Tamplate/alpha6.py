def run_formula(dv):
    alpha6=dv.add_formula('alpha6','-Ts_Mean(Log(high/low),20)',is_quarterly=False,add_data=True)
    return alpha6