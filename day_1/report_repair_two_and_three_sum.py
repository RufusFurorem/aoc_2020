def two_sum(expense_report, target):
    compl_dict = {}
    for val in expense_report:
        compl = target - val
        if val in compl_dict:
            return (val * compl_dict[val])
        compl_dict[compl] = val

def three_sum(expense_report, target):
    compl_dict = {}
    two_vals = []
    for i, val in enumerate(expense_report):
        two_vals.append([(val, num) for j, num in enumerate(expense_report) if j != i])

    for sums in two_vals:
        for value in sums:
            for exp_val in expense_report:
                if (value[0] + value[1] + exp_val) == target:
                    print(value[0], value[1], exp_val)
                    return (value[0] * value[1] * exp_val)


if __name__ == "__main__":
    with open('..\\input.csv', 'r') as fd:
        lines = fd.read().strip()
        expense_values = lines.split('\n')
        expense_values = list(map(int, expense_values))
    target_value = 2020
    print(two_sum(expense_values, target_value))
    print(three_sum(expense_values, target_value))
