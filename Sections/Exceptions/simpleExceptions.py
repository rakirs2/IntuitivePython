def validate_inputs(unvalidated):
    split_values= unvalidated.split("/")
    ## Validations
    if len(split_values) != 2:
        return []
    try:
        split_values[0]= int(split_values[0])
        split_values[1]= int(split_values[1])
        if split_values[1] == 0:
            return []
        if split_values[0] > split_values[1]:
            return []
        if split_values[0] < 0 and split_values[1] < 0:
            return []
    except ValueError:
        return []
    
    return split_values
    
def calculate_inputs(inputs):
    percentage = round(inputs[0]/inputs[1] * 100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")    



validated = []
while(len(validated)!=2):
    unvalidated = input("Fraction:")
    validated = validate_inputs(unvalidated)

calculate_inputs(validated)
