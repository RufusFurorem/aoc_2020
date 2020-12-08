
def two_sum(expense_report, target):
    compl_dict = {}
    for val in expense_report:
        val = int(val)
        compl = target - val
        if val in compl_dict:
            return (val * compl_dict[val])
        compl_dict[compl] = val

if __name__ == "__main__":
    with open('input.csv', 'r') as fd:
        lines = fd.read().strip()
        expense_values = lines.split('\n')
    target_value = 2020
    print(two_sum(expense_values, target_value))