# USA Taxes (Experimental)

This tool roughly calculates federal taxes, net income and other interesting things. 

Limitations:
  * Supports only 2021 and 2022
  * Supports only W2
  * Supports only federal taxes, so local should be added as withholding in section w4_4c.
  * Ony for families filling jointly without dependencies.


Simple usage:
```console
python3 run.py --profiles ${PATH_TO_PROFILE} --year ${TAX_YEAR}
```

Example profile with all settings is in this [file](example.yml)

P.S. made for my private usage. So result is not guaranteed. No warranty. You're welcome to extend functionality, 
just open PR with suggestions or fixes.

P.S.S For 2022 federal taxes requires paying w4_4c for Profile1. Use IRS worksheets to calculate exact amount.
