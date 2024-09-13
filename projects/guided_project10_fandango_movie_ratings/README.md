# Investigating Fandango Movie Ratings

In October 2015, a data journalist named Walt Hickey analyzed movie ratings data and found strong evidence to suggest that Fandango's rating system was biased and dishonest (Fandango is an online movie ratings aggregator). He published his analysis in this [article](https://fivethirtyeight.com/features/fandango-movies-ratings/).

Hickey found that there's a significant discrepancy between the number of stars displayed to users and the actual rating, which he was able to find in the HTML of the page. He was able to find that:

- The actual rating was almost always rounded up to the nearest half-star. For instance, a 4.1 movie would be rounded off to 4.5 stars, not to 4 stars, as you may expect.
- In the case of 8% of the ratings analyzed, the rounding up was done to the nearest whole star. For instance, a 4.5 rating wd be rounded off to 5 stars.
- For one movie rating, the rounding off was completely bizarre: from a rating of 4 in the HTML of the page to a displayed rating of 5 stars.

Fandango's officials replied that the biased rounding off was caused by a bug in their system rather than being intentional, and they promised to fix the bug as soon as possible. Presumably, this has already happened, although we can't tell for sure since the actual rating value doesn't seem to be displayed anymore in the pages' HTML.

In this project, we'll analyze more recent movie ratings data to determine whether there has been any change in Fandango's rating system after Hickey's analysis.


## Data Files

This project includes the following data files:

- `fandango_score_comparison.csv`: 2016 Dataset from Walt Hickey
- `movie_ratings_16_17.csv`: 2016/2017 Rating Data

### Instructions

1. Download or clone this repository.
2. Ensure that the data files are located in the `Data/` directory.
3. Open the Jupyter Notebook `Guided_project10 - Fandango movie ratings.ipynb` and run the cells to reproduce the analysis.

### Project Notebook

You can also directly view or run the analysis in the [Jupyter Notebook](https://github.com/timmueller0/data_projects_misc/blob/main/projects/guided_project8_star_wars_survey/Guided_project%208%20-%20Star%20Wars%20Survey.ipynb).


