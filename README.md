# poscnvtr

Convert APRS/UI-View POS overlay files to either JSON styled for [RadarScope](https://www.radarscope.app) or [Xastir](http://xastir.org/) object log format.

## System Requirements

_Should_ run on anything with Python 3.8.1 or later. A quick internet search should point you in the right direction for installing Python on your OS of choice. On MacOS I recommend using [Homebrew](https://brew.sh).

## Usage

Once you have Python installed, you can either clone this repository or download _location.py_ and _posconvtr.py_ to your system. Then make sure they are available on your command line path.

    > posconvtr.py -j overlay.pos

Convert input file _overlay.pos_ to RadarScope style JSON and write it to standard output

    > posconvtr.py -x overlay.pos

Convert input file _overlay.pos_ to Xastir log format using `000000z` for timestamp and write it to standard out.

    > posconvtr.py --xastir --current_time overlay.pos

Convert input file _overlay.pos_ to Xastir log format using current UTC time for timestamp and write it to standard out.

    > posconvtr.py -x --current_time overlay.pos > object.log

Convert input file _overlay.pos_ to Xastir log format using current UTC time for timestamp and write it to to the file _object.log_.

## Details

### UI View POS Input

Input should be in standard [APRS overlay format](https://www.ve3kbr.com/aprs/aprs_overlay_format.htm).

### Xastir Timestamps

The default for Xastir timestamps is 00:00:00 UTC. Specifying the `--current_time` option uses the current zulu time for the timestamps.
