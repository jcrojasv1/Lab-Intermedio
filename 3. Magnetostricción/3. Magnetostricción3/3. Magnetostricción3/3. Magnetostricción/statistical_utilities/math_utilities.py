import numpy as np
import sympy as sym

def linear_w_regression(x_data: np.array,y_data: np.array,sigma_x:np.array,sigma_y:np.array):
    w = (1/sigma_y)**2
    delta = np.sum(w)*np.sum(w*x_data**2) - (np.sum(w*x_data))**2
    
    m = (np.sum(w)*np.sum(w*y_data*x_data) - np.sum(w*x_data)*np.sum(w*y_data))/delta
    b = (np.sum(w*x_data**2)*np.sum(w*y_data) - np.sum(w*x_data)*np.sum(w*y_data*x_data))/delta
    
    uncer_m = np.sqrt(np.sum(w)/delta)
    uncer_b = np.sqrt(np.sum(w*x_data**2)/delta)
    

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

def VerifyMax(x:list,y:list) :
    """
    La función tiene como entrada dos listas con los valores de espectro de una estrella y retorna una lista de tuplas,
    siendo estas las posiciones de los puntos máximos.

    Args:
        x (list): Valores de espectro
        y (list): Valores de intensidad

    Returns:
        list: Lista de tuplas con los máximos locales de los datos.
    """
    
    xmax_points = []
    ymax_points = []
    
    for i in range(2, len(x)-1):
        left_handed_slope = (y[i]-y[i-1])/(x[i] - x[i-1])
        right_handed_slope = (y[i+1]-y[i])/(x[i+1] - x[i])
        if right_handed_slope < 0 and left_handed_slope > 0:
            xmax_points.append(x[i])
            ymax_points.append(y[i])
        
    return xmax_points, ymax_points