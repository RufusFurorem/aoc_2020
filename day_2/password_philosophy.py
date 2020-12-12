def count_valid_passwords(pwds_and_policies):
    valid_passwords = 0

    for pwd_policy in pwds_and_policies:
        sep_pwd_policy = pwd_policy.split(' ')
        # Minimum characters idx = 0, maximum character idx = 1
        min_and_max_char = list(map(int, sep_pwd_policy[0].split('-')))
        policy_char_cnt = 0

        # Second split is "Letter:", 0 idx is the letter
        policy_char = sep_pwd_policy[1][0]

        # The password is contained in the last split
        pwd = sep_pwd_policy[2]

        # Count the number of times the character appears in the password
        for char in pwd:
            if char == policy_char:
                policy_char_cnt += 1

        # Verify that the character appears at least the minimum and not above the maximum
        if policy_char_cnt < min_and_max_char[0] or policy_char_cnt > min_and_max_char[1]:
            continue
        else:
            valid_passwords += 1

    return valid_passwords

def count_valid_passwords_new_policy(pwds_and_policies):
    valid_passwords = 0

    for pwd_policy in pwds_and_policies:
        sep_pwd_policy = pwd_policy.split(' ')
        # first index is located at idx = 0, second index is idx = 1
        first_and_sec_idx = list(map(int, sep_pwd_policy[0].split('-')))

        # Account for 1 starting idx
        first_and_sec_idx[0] = first_and_sec_idx[0] - 1
        first_and_sec_idx[1] = first_and_sec_idx[1] - 1

        policy_char_cnt = 0

        # Second split is "Letter:", 0 idx is the letter
        policy_char = sep_pwd_policy[1][0]

        # The password is contained in the last split
        pwd = sep_pwd_policy[2]

        # Count the number of times the character appears in the password

        try:
            first_and_not_second_idx = pwd[first_and_sec_idx[0]] == policy_char \
            and pwd[first_and_sec_idx[1]] != policy_char
            second_and_not_first_idx = pwd[first_and_sec_idx[1]] == policy_char \
            and pwd[first_and_sec_idx[0]] != policy_char
            if first_and_not_second_idx or second_and_not_first_idx:
                valid_passwords += 1
            else:
                continue
        except IndexError:
            # Index for password does not exist
            continue

    return valid_passwords


if __name__ == '__main__':

    with open('input.txt', 'r') as fd:
        passwords_and_policy = fd.read().split('\n')
    print(count_valid_passwords(passwords_and_policy))
    print(count_valid_passwords_new_policy(passwords_and_policy))
