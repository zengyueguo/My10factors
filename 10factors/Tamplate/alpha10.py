def run_formula(dv):
    alpha10=dv.add_formula('alpha10','-Correlation(close_adj,volume,10)',is_quarterly=False,add_data=True)
    return alpha10
 