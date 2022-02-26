import arithmetic.Div_mod as div
import arithmetic.Mult_mod as mult
import arithmetic.Sub_mod as sub
import arithmetic.Sum_mod as sum

# Модуль для вызова метода соответствующего выбранной операции. 
dict_ar = {'/': div, '*': mult, '-': sub, '+': sum}
dict_log = {'/': 'division', '*': 'multiplication', '-': 'subtraction', '+': 'addition'}