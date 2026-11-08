from typing import Callable
import re

def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    for match in re.finditer(pattern, text):    #finditer finds iters by pattern 
        yield float(match.group())              #with group method we get nums from iters to yield in sum_profit func

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text, generator_numbers))
