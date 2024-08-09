import numpy as np
import sympy as sym

def linear_w_regression(x_data: np.array,y_data: np.array,sigma_x:np.array,sigma_y:np.array):
    w = (1/sigma_y)**2
    delta = np.sum(w)*np.sum(w*x_data**2) - (np.sum(w*x_data))**2
    
    m = (np.sum(w)*np.sum(w*y_data*x_data) - np.sum(w*x_data)*np.sum(w*y_data))/delta
    b = (np.sum(w*x_data**2)*np.sum(w*y_data) - np.sum(w*x_data)*np.sum(w*y_data*x_data))/delta
    
    uncer_m = np.sqrt(np.sum(w)/delta)
    uncer_b = np.sqrt(np.sum(w*x_data**2)/delta)
    
    print(r"m: %s"%(m) + " uncertanty m: %s"%(uncer_m))
    print(r"b: %s"%(b) + " uncertanty b: %s"%(uncer_b))
    return np.array([m,uncer_m,b,uncer_b])

def error_propagation(vars_,expr,vars_data,uncer_vars):
    if not len(vars_) == len(vars_data):
        print("No hay mismo número de series de datos que de variables.")
        print("Hay %s variables y %s series de datos.")
        return None
    
    for i in range(len(vars_)):
        dfdvar = sym.diff(expr,vars_[i])
        """
        TODO Hay que terminar esta implementación de la propagación de errores para una
        expresión general que dependa de las variables que vienen en una lista vars_ sobre 
        una expresión sympy que viene por expr
        """
        print("No implementado aún.")
        return  None