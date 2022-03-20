===SSI Name data

This repo contains a distillation of the SSI Baby Name database (available at https://www.ssa.gov/oact/babynames/names.zip), with a gender ratio column.  This allows you to view gender-related name statistics.

For example, I can look up the name "Jessica" and find that 99.66% of people named that are female. Or I can find that the most feminine name in the database is 'Delilah', with 46490 women named that and 0 men (or at least less than five per year, see limitations below), followed by Athena, Brielle, Helena, and Lyla.

Conversely, the most popular 100% masc names are Jakob, Tobias, Jefferson, Rodger, and Romeo. Having such a narrow range often results in uncommon names, so if you want something more typical a range of 5-10% can be more useful: The most popular > 95% masc or more names are James, John, Robert, Michael, and William.

More interestingly, I can get a list of names that are between 65% and 75% masculine, sorted by popularity. The top 5 names in that range are Jordan, Angel, Johnnie, Dakota, and Rene.

This data is descriptive, not proscriptive! You can be a guy and decide to call yourself Jessica (or Delilah!), and that's valid! But these numbers reflect how the public will perceive the name, and what they'll infer about your gender based on it.

===Files

====ratios.csv

This is a csv file containing four columns:

* name - The name in question
* men - Total number of men with that name
* women - Total number of women with that name
* fem - Percent of people with that name who are listed as female

It was generated from allyears.csv using the process described in history.py, including only name data from 1970-present.  To use other date ranges, regenerate ratios as described in history.py

====allyears.py

This contains un-distilled name data.  It was generated from the yob????.txt files extracted from names.zip (as downloaded from ssi.gov url above), using the following bash command:

```grep , yob*.txt | sed 's/^yob\(....\).txt:/\1,/' >allyears.csv```

====history.py

This file contains Python commands for loading and analyzing the data, as well as how to regenerate it if desired.

====README.md

That's this file.

===Usage

history.py has rudimentary instructions for loading the data with Pandas and running various queries on it, as well as rebuilding the ratios for a specific year range if you want a name that's typical for your people your age, or using a 'masc' column instead of a 'fem' column if you prefer (it works either way, since they're negatively related).

If you don't have access to Python 3 and Pandas you can just load ratios.csv into Excel and sort/filter/search as desired.  This limits you to name data from 1970-2020.



===Limitations

There are some limitations to the data:

* The current ratios spreadsheet is based off of data from 1970 to current (although you can redo it with whatever year range you like if you can follow the Python commands)
* For privacy reasons SSI does not include entries with less than 5 examples in a given year, so extremely rare name/gender combos are absent
* As far as I can tell, SSI includes only a person's legally-given name and gender assigned at birth. So some names that are common nicknames (e.g. Alex) are underrepresented because many people who go by that have a legal name like "Alexander" or "Alexandria".
* I suspect name or gender changes for trans people aren't included in the data.
* SSI does not include any data for intersex or non-binary people

