import pandas as pd
import pathlib

def main():
    path = pathlib.Path(__file__)
    data_path = path.parents[1] / "data" / "kontinuitetsfil_1971_2019_27april2021.dta"

    reader = pd.io.stata.StataReader(data_path)

    # chose var
    chosen_var = "v17"

    print(f"[INFO:] PRINTING INFORMATION ABOUT VARIABLE: {chosen_var}")
    # get var names (actual variable name) from reader
    var_names = reader.variable_labels()
    
    print(var_names[chosen_var])

    # get what the integer values code for in the variable
    value_codes = reader.value_labels()

    # format, lower case keys to match var names (e.g., go from V17 to v17)
    value_codes = {k.lower(): v for k, v in value_codes.items()} 

    print(value_codes[chosen_var]) 


if __name__ == "__main__":
    main()
