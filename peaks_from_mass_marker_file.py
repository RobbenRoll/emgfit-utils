### Convenience functions to initialize peaks from a MAc mass marker file
### Author: Stefan Paul

def add_peaks_from_mass_marker_file(spec, marker_fname, sep=""):
    """Add peaks stored in a mass-marker file to spectrum

    Parameters
    ----------
    spec : :class:`emgfit.spectrum.spectrum`
        Spectrum object to add peaks to.
    marker_fname : str
        Mass-marker file name.
    sep : str
        Column separator within mass-marker file. 
    """
    markers = pd.read_csv(marker_fname, sep=sep, usecols=[0,1,2], names=["species", "index", "x_pos"])
    markers.sort_values("x_pos", ascending=True, axis=0, inplace=True)
    print(f"### Adding peaks from mass-marker file '{marker_fname}' ###")
    for index, row in markers.iterrows():
        try:
            spec.add_peak(row['x_pos'], species=row['species'])
        except Exception as ex:
            print(f"\nAdding peak at {row['x_pos']:.6f} u failed due to exception:")
            print('"'+str(ex)+'"\n')

### Usage example:
# mass_data_fname = "mass_data.txt"
# spec = emg.spectrum(mass_data_fname, skiprows=27)
# marker_fname = "marker_file.dat"
# add_peaks_from_mass_marker_file(spec, marker_fname)
# spec.show_peak_properties()
