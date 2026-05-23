HOW TO RUN THIS PROJECT
=======================


REQUIREMENTS
------------

- Python 3.10 or higher
- pip (comes with Python)
- Internet connection (only needed if you want to re-fetch data from the
  World Bank API; the cached CSV is already in the repo)

Python packages:
    wbgapi
    pandas
    numpy
    scikit-learn
    statsmodels
    linearmodels
    matplotlib
    seaborn
    jupyter


SETUP
-----

1. Clone the repository:

       git clone https://github.com/quamaraziz/healthcare-financing-econometrics.git
       cd healthcare-financing-econometrics

2. (Recommended) Create and activate a virtual environment:

       python -m venv venv

       # macOS / Linux:
       source venv/bin/activate

       # Windows:
       venv\Scripts\activate

3. Install the dependencies:

       pip install wbgapi pandas numpy scikit-learn statsmodels linearmodels matplotlib seaborn jupyter


RUNNING THE PROJECT
-------------------

There are two ways to run this, depending on whether you want to re-fetch
the raw data or just analyse the cached panel.


Option A: Analyse the cached data (faster)
------------------------------------------

The repo already includes world_bank_panel_data.csv. Just open the notebook:

       jupyter notebook EDA.ipynb

Then run all cells (Cell > Run All, or Shift+Enter through each cell).


Option B: Re-fetch the data, then analyse (full pipeline)
---------------------------------------------------------

1. Run the data extraction pipeline. This calls the World Bank API,
   cleans the data, and overwrites world_bank_panel_data.csv:

       python main.py

   This usually takes 30 to 60 seconds.

2. Open the notebook and run all cells:

       jupyter notebook EDA.ipynb


FILE OVERVIEW
-------------

    main.py                     Entry point for the data pipeline
    config.py                   Indicator codes, timeframe, entities to drop
    data_api.py                 World Bank API extraction (wbgapi)
    functions.py                Preprocessing logic
    EDA.ipynb                   Exploratory analysis and regression models
    world_bank_panel_data.csv   Cached output panel (4,700 observations)


TROUBLESHOOTING
---------------

Problem: "ModuleNotFoundError: No module named 'wbgapi'" (or any other
         package)
Fix:     The package isn't installed in your active environment. Run
         the pip install command from the Setup section again. If you
         created a virtual environment, make sure it's activated.

Problem: World Bank API call hangs or times out when running main.py
Fix:     The API can be flaky. Wait a minute and re-run. If it still
         fails, you can skip main.py entirely and just open the
         notebook (Option A above) since the CSV is already cached.

Problem: Jupyter notebook won't open / "command not found: jupyter"
Fix:     Make sure jupyter is installed:
             pip install jupyter
         If you're using a virtual environment, make sure it's activated
         before running the jupyter command.

Problem: Regression cells fail with "PanelOLS not found" or similar
Fix:     linearmodels is missing. Install it:
             pip install linearmodels

Problem: KNN imputer cell fails with "sklearn not found"
Fix:     Install scikit-learn (note the package name has a hyphen but
         imports as sklearn):
             pip install scikit-learn

Problem: Pandas raises a "performance warning" or "future warning" when
         running the notebook
Fix:     These are warnings, not errors. The notebook will still run
         correctly. Safe to ignore.

Problem: Plots don't display in the notebook
Fix:     Add this line near the top of the notebook (before any plotting
         cell):
             %matplotlib inline

Problem: Different results than reported in the README
Fix:     If you re-fetched the data with main.py, the World Bank may
         have revised historical figures since this project was last run
         (May 2026). Small numerical differences are expected; the
         qualitative conclusions should still hold.
