import view
import operator

def button_click():
    value_a = view.get_value()
    oper = view.get_operator()
    value_b = view.get_value()
    func = operator.dict_ar[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.view_data(result)
    

