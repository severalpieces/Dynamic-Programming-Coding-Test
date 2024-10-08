# create a function to check if the inputs are valid
def check_raw_input(raw_input):
    # try separating the raw input
    try:
        inputs = raw_input.split()
    except Exception:
        raise ValueError("Sorry! Input could not be split. Please enter two values separated by space.")
    
    # check if there are indeed two input values
    if len(inputs) !=2:
        raise ValueError("Sorry! You must enter exactly two values.")
    
    # check if the inputs are digits
    if not all(item.isdigit() and int(item)>=1 for item in inputs):
        raise ValueError("Sorry! Inputs must be positive integers.")
    
    return map(int, inputs)
    

        
    
def main():
    try:
        # read and check the first line of input for n_cargo and max_mass
        raw_input = input()
        n_cargo, max_mass = check_raw_input(raw_input)
        
        # check if the inputs for n_cargo and max_mass satisfy their constraints
        if not (n_cargo <= 1000):
            raise ValueError("Oops! Bocek ship can only take less than 1000 samples.")
        if not (max_mass <= 10000):
            raise ValueError("Oops! The maximum capacity of Bocek ship is 10000.")
        
        
        # read and check every line of inputs for the mass and value of each sample
        masses = []
        values = []
        for _ in range(n_cargo):
            raw_input = input()
            mass, value = check_raw_input(raw_input)
            
            # check if the mass and value of each sample match their constraints
            if not (mass <= max_mass):
                raise ValueError(f"Oops! This sample is even heavier than the maximum mass {max_mass}.")
            if not (value <= 1000):
                raise ValueError("Oops! I think the value of sample cannot exceed 1000.")
            
            masses.append(mass)
            values.append(value)
        
        # create a 2D list for memoization
        memo = [[-1 for _ in range(max_mass + 1)] for _ in range(n_cargo + 1)]
        
        # using memoization to improve time complexity
        def KS(i, C):
            if memo[i][C] >= 0:
                return memo[i][C]
            if i == n_cargo:
                result = 0
            elif C < masses[i]:
                result = KS(i+1, C)
            else:
                result = max(
                    KS(i+1,C),
                    KS(i+1, C-masses[i]) + values[i]
                )
            memo[i][C] = result
            return result
        
        print(KS(0,max_mass))
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

if __name__ == "__main__":
    main()
    

# time complexity: O(n_cargo * max_mass)
# space complexity: O(n_cargo * max_mass)
# the memoization drastically enhanced time complexity