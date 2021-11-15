# FYS1035 climlab project
 Using climlab's 1D EBM model to simulate the ice-albedo feedback and turning points

Some sort of review of the scripts:
climlib.py contains some functions and classes that help structuring the data and keeping the scripts tidy.
Scripts starting with "make_", run the climlab package and do the actual work. They generate a list of "prediction"-objects, that will be saved in a .npy file. This allow us to just make the datasets from imported data and climlab, and save them to disk. This takes some time, and it's nice to just do it once, and plot the stuff in other scripts.
Scripts starting with "plot_" load the .npy files, and plot the data saved in them.

Example of run:
Run make_datasets_vanilla.py
After it finishes running, a "predictions_vanilla.npy file will be written in the same folder.
Run plot_4scenarios_years-co2_icelat.py to plot the unmodified prediction models for the co2e levels, and the ice latidute as calculated by climlab.
