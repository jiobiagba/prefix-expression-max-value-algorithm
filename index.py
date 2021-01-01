from helpers import solve_prefix, generate_graph, generate_array
import ast

def max_prefix(expression, variable): # Supply {} as variable if no variable exists
    var_dict = ast.literal_eval(variable)
    dict_length = len(var_dict)

    if dict_length == 0:
        max_value = solve_prefix(expression)
        return max_value

    range_provided = list(var_dict.values())
    keys_provided = list(var_dict.keys())
    all_results = []

    if dict_length == 1:
        val_array = generate_array(*range_provided)
        for j in range(len(val_array)):
            new_exp = expression.replace(*keys_provided, str(val_array[j]))
            all_results.append(solve_prefix(new_exp))
        all_results.sort()
        return all_results[len(all_results) - 1]
    
    if dict_length == 2:
        val_graph = generate_graph(*range_provided)
        for k in range(len(val_graph)):
            new_exp = expression.replace(keys_provided[0], str(val_graph[k][0]))
            new_exp = new_exp.replace(keys_provided[1], str(val_graph[k][1]))
            all_results.append(solve_prefix(new_exp))
        all_results.sort()
        return all_results[len(all_results) - 1]




if __name__ == "__main__":
    import sys
    expression = input("Prefix Expression: ")
    variable = input("Variable(s) Dictionary: ")
    print(max_prefix(expression, variable))
