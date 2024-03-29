from argparse import ArgumentParser
from copy import deepcopy as copy
from yaml import load, CLoader


class Taxes:
    brackets = {
        2021: {
            10: (0, 19900),
            12: (19900, 81050),
            22: (81050, 172750),
            24: (172750, 329850),
            32: (329850, 418850),
            35: (418850, 628300)
        },
        2022: {
            10: (0, 20550),
            12: (20551, 83550),
            22: (83551, 178150),
            24: (178151, 340100),
            32: (340101, 431900),
            35: (431901, 647850)
        },
        2023: {
            10: (0, 22000),
            12: (22001, 89450),
            22: (89451, 190750),
            24: (190751, 364200),
            32: (364201, 462500),
            35: (462501, 693750)
        }
    }

    oasdi = {
        2021: 142800,
        2022: 147000,
        2023: 160200
    }

    standard_deduction = {
        2021: 25100,
        2022: 25900,
        2023: 27700
    }

    # 2021, 2022 https://www.irs.gov/newsroom/irs-announces-401k-limit-increases-to-20500
    limits_401 = {2021: 19500,
                  2022: 20500}

    profiles = None
    pay_period = 0
    v2 = dict()
    v3 = dict()

    nice_output_key = 0
    nice_output_value1 = 0
    nice_output_value2 = 0
    nice_output_separator = 0

    def __init__(self, year):
        self.year = year

    def _adjust_profiles(self):
        for profile in self.profiles:
            if profile['income']['pay_frequency'] != 'annually':
                exit(1)
            else:
                profile['income'] = profile['income']['value']

            if '401k' in profile:
                if not isinstance(profile['401k']['value'], str):
                    if profile['401k']['pay_frequency'] == 'annually':
                        profile['401k'] = profile['401k']['value']
                    elif profile['401k']['pay_frequency'] == 'semi-monthly':
                        profile['401k'] = profile['401k']['value'] * 24
                elif '%' in profile['401k']['value']:
                    profile['401k'] = profile['income'] * int(profile['401k']['value'][:-1]) / 100
                elif profile['401k']['value'] == 'max':
                    profile['401k'] = self.limits_401[self.year]

            if 'fsa' in profile:
                if profile['fsa']['pay_frequency'] == 'semi-monthly':
                    profile['fsa'] = profile['fsa']['value'] * 24
                elif profile['fsa']['pay_frequency'] == 'monthly':
                    profile['fsa'] = profile['fsa']['value'] * 12
                elif profile['fsa']['pay_frequency'] == 'annually':
                    profile['fsa'] = profile['fsa']['value']
                else:
                    exit(1)

            if 'insurance' in profile:
                tmp = 0
                for k, v in profile['insurance']['value'].items():
                    if k in [
                        'dental',
                        'medical',
                        'vision'
                    ]:
                        if 'insurance_required' not in profile:
                            profile['insurance_required'] = 0

                        profile['insurance_required'] += v
                    else:
                        if 'insurance_user' not in profile:
                            profile['insurance_user'] = 0

                        profile['insurance_user'] += v

                    tmp += v

                for k in ['insurance_required', 'insurance_user']:
                    if k in profile:
                        if profile['insurance']['pay_frequency'] == 'semi-monthly':
                            profile[k] *= 24
                        elif profile['insurance']['pay_frequency'] == 'monthly':
                            profile[k] *= 12
                        elif profile['insurance']['pay_frequency'] == 'annually':
                            pass
                if profile['insurance']['pay_frequency'] == 'semi-monthly':
                    tmp *= 24
                elif profile['insurance']['pay_frequency'] == 'monthly':
                    tmp *=12
                elif profile['insurance']['pay_frequency'] == 'annually':
                    pass
                else:
                    exit(1)

                profile['insurance'] = tmp

            if 'w4_4c' in profile:
                if profile['w4_4c']['pay_frequency'] == 'semi-monthly':
                    profile['w4_4c'] = int(profile['w4_4c']['value']) * 24
                elif profile['w4_4c']['pay_frequency'] == 'annually':
                    profile['w4_4c'] = int(profile['w4_4c']['value'])
                else:
                    exit(1)

            if 'income_limit' in profile:
                average_per_period = profile['income'] / profile['income_limit']['period']
                if profile['income_limit']['pay_frequency'] == 'semi-monthly':
                    profile['part_income'] = average_per_period * 24
                    profile['income_factor'] = profile['income_limit']['period'] / 24
                elif profile['income_limit']['pay_frequency'] == 'bi-weekly':
                    profile['part_income'] = average_per_period * 26
                    profile['income_factor'] = profile['income_limit']['period'] / 26
                else:
                    exit(1)

        self.pay_period = 24

    def _deduction(self):
        itemized_deductions = 0
        for profile in self.profiles:
            if 'itemized_deductions' in profile:
                for deduction in profile['itemized_deductions']:
                    itemized_deductions += deduction

        return self.standard_deduction[self.year] if self.standard_deduction[self.year] > itemized_deductions else \
            itemized_deductions

    def _federal(self):
        deduction_base = self._deduction()
        deduction_custom = 0
        agi = 0
        tax = 0

        for profile in self.profiles:
            agi += profile['income']

            if 'self_employment' in profile and profile['self_employment'] is True:
                social_security, medicare = self._fica(profile)
                agi = agi - social_security - medicare
                tax = tax + social_security + medicare
                deduction_custom = 3165

            if 'fsa' in profile:
                agi -= profile['fsa']

            if 'insurance' in profile:
                agi -= profile['insurance']

            if '401k' in profile:
                agi -= profile['401k']

        tax_base = agi - deduction_base - deduction_custom
        for percent, bracket in self.brackets[self.year].items():
            if tax_base < bracket[1]:
                step = (tax_base - bracket[0]) * percent / 100
            else:
                step = (bracket[1] - bracket[0]) * percent / 100
            tax += step
            if tax_base < bracket[1]:
                break

        return round(tax, 2)

    def _federal_per_paycheck(self, profile):
        deduction_base = self._deduction()
        deduction_custom = 0
        agi = 0
        tax = 0

        if 'part_income' in profile:
            agi += profile['part_income']
        else:
            agi += profile['income']

        if 'self_employment' in profile and profile['self_employment'] is True:
            social_security, medicare = self._fica(profile)
            agi = agi - social_security - medicare
            tax = tax + social_security + medicare
            deduction_custom = 3165

        if 'insurance_required' in profile:
            agi -= profile['insurance_required']

        if '401k' in profile:
            agi -= profile['401k']

        if agi < deduction_base:
            tax_base = agi
        else:
            tax_base = agi - deduction_base - deduction_custom

        for percent, bracket in self.brackets[self.year].items():
            if tax_base < bracket[1]:
                step = (tax_base - bracket[0]) * percent / 100
            else:
                step = (bracket[1] - bracket[0]) * percent / 100
            tax += step
            if tax_base < bracket[1]:
                break

        if 'w4_4c' in profile:
            tax += profile['w4_4c']

        if 'income_limit' in profile:
            tax *= profile['income_factor']

        return round(tax, 2)

    def _fica(self, profile):
        if profile['income'] == 0:
            return 0, 0

        if 'self_employment' in profile and profile['self_employment'] is True:
            return profile['income'] * 12.4 / 100, profile['income'] * 2.9 / 100

        payment = profile['income'] / 24
        tax_base = payment if 'insurance_required' not in profile else payment - profile['insurance_required'] / 24
        if 'fsa' in profile:
            tax_base -= profile['fsa'] / 24

        ytd_payment = 0

        social_security = 0
        medicare = 0
        for period in range(1, 25):
            ytd_payment += payment
            if ytd_payment < self.oasdi[self.year]:
                social_security += tax_base * 6.2 / 100
                medicare = medicare + tax_base * 1.45 / 100
            else:
                medicare = medicare + tax_base * 1.45 / 100

        return round(social_security, 2), round(medicare, 2)

    def _nice_print(self, output):
        for k, v in output.items():
            if v in ['']:
                continue

            self.v2[k] = str(round(v / self.pay_period, 2))
            self.v3[k] = f"{str(round(100 * v / output['Gross income'], 2))}%"
            v1 = len(str(v))
            v2 = len(self.v2[k])

            k = len(str(k))

            self.nice_output_key = self.nice_output_key if self.nice_output_key > k else k

            self.nice_output_value1 = self.nice_output_value1 if self.nice_output_value1 > v1 else v1
            self.nice_output_value2 = self.nice_output_value2 if self.nice_output_value2 > v2 else v2
            self.nice_output_separator = self.nice_output_key + self.nice_output_value1 + self.nice_output_value2 + 10

    @staticmethod
    def _w2_income_per_paycheck(profile):
        result = profile['income']
        for k in ['401k', 'insurance_required', 'fsa']:
            if k in profile:
                result -= profile[k]

        return result

    def calculate(self, profiles):
        with open(profiles, mode='r') as fl:
            self.profiles = [v for _, v in load(fl.read(), Loader=CLoader)[self.year].items()]

        self._adjust_profiles()

        output = {'Gross income': 0,
                  'W2 income': 0,
                  'Deductions': 0,
                  '401k': 0,
                  'Insurance': 0,
                  'Taxes': 0,
                  'Federal': 0,
                  'Fica': 0,
                  'Withholding': 0,
                  'Take home': 0,
                  'W2': self._federal(),
                  'Refund': -1 * self._federal()
                  }

        i = 1
        for profile in self.profiles:
            output[f"Profile {i}"] = ''
            income = profile['income']
            social_security, medicare = self._fica(profile)

            # Gross income
            output[f'gross income {i}'] = income
            output['Gross income'] += output[f'gross income {i}']

            # W2 income
            output[f'w2 income {i}'] = self._w2_income_per_paycheck(profile)
            output['W2 income'] += output[f'w2 income {i}']

            # Deductions
            output[f'deductions {i}'] = 0
            for k in ['401k', 'insurance']:
                if k in profile and k == '401k':
                    output[f'{k} {i}'] = profile[k] if profile[k] != 'max' else self.limits_401[self.year]
                elif k in profile:
                    output[f'{k} {i}'] = profile[k]

                if k in profile:
                    output[k.capitalize()] += output[f'{k} {i}']
                    output[f'deductions {i}'] += output[f'{k} {i}']
                    output['Deductions'] += output[f'{k} {i}']
                    income -= output[f'{k} {i}']

            # Taxes
            output[f'taxes {i}'] = 0

            if 'withholding' in profile:
                output[f'withholding {i}'] = profile['withholding']
                income -= profile['withholding']
                output[f'taxes {i}'] += profile['withholding']
                output['Taxes'] += profile['withholding']
                output['Withholding'] += profile['withholding']

            if 'self_employment' not in profile or profile['self_employment'] is False:
                social_security, medicare = self._fica(profile)
                income -= social_security
                income -= medicare

            output[f'federal {i}'] = self._federal_per_paycheck(profile)
            output['Federal'] += output[f'federal {i}']

            output[f'taxes {i}'] += output[f'federal {i}']
            output['Taxes'] += output[f'federal {i}']

            output['Refund'] += output[f'federal {i}']

            income -= output[f'federal {i}']

            output[f'fica {i}'] = round(social_security + medicare, 2)
            output[f'taxes {i}'] += output[f'fica {i}']
            output['Fica'] += output[f'fica {i}']
            output['Taxes'] += output[f'fica {i}']

            output[f"  social security {i}"] = round(social_security, 2)
            output[f"  medicare {i}"] = round(medicare, 2)

            # Take home
            output[f'take home {i}'] = round(income, 2)
            output['Take home'] += output[f'take home {i}']

            # round and filter
            if output[f'taxes {i}'] < 0:
                del(output[f'taxes {i}'])

            i += 1

        # round and filter
        for k, v in copy(output).items():
            if not isinstance(v, str):
                output[k] = round(output[k], 2)
                if output[k] == 0:
                    del(output[k])

        self._nice_print(output)

        block = True
        for k, v in output.items():
            add_1 = 1 + self.nice_output_key - len(k)
            add_2 = 1 + self.nice_output_value1 - len(str(v))
            add_3 = 0
            try:
                add_3 = 1 + self.nice_output_value2 - len(str(self.v2[k]))
            except KeyError:
                pass

            if k.startswith('Deductions') or k.startswith('Taxes'):
                print(f"\n{k}{' ' * add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}")
                print(f"{'-' * self.nice_output_separator}")
            elif k.startswith('Take home'):
                print(f"\n{k}{' ' * add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}")
            elif k.startswith('W2'):
                print(f"\n{'+' * self.nice_output_separator}")
                print(f"\n{k}{' ' * add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}")
            elif k.startswith('deductions') or k.startswith('taxes'):
                print(f"\n{k[:-1]}{' ' * add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}")
                print(f"{'-' * self.nice_output_separator}")
            elif k.startswith('take home'):
                print(f"\n{k[:-1]}{' ' * add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}")
            elif not k[-1].isdigit():
                line = f"{k}{' '* add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}"
                if block:
                    line = f"\n{line}"
                if block:
                    block = False
                print(line)
            elif k.startswith('Profile'):
                print(f"\n{'='* self.nice_output_separator} \n{k} \n")
            elif k[-1].isdigit():
                print(f"{k[:-1]}{' '* add_1}{v}{' ' * add_2}{self.v2[k]}{' ' * add_3}{self.v3[k]}")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--profiles', default='private.yml', type=str, action='store')
    parser.add_argument('--year', default=2023, type=int, action='store')
    args = parser.parse_args()

    taxes = Taxes(args.year)
    taxes.calculate(args.profiles)
