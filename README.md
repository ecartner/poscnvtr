# poscnvtr

Convert APRS/UI-View POS overlay files to either JSON styled for [RadarScope], or Xastir object log format.

## System Requirements

_should_ run on anything with Python 3.8.1 or later

## Usage

    > posconvtr.py -j overlay.pos

Convert input file _overlay.pos_ to RadarScope style JSON and write it to standard output

    > posconvtr.py -x overlay.pos

Convert input file _overlay.pos_ to Xastir log format using `000000z` for timestamp and write it to standard out.

    > posconvtr.py --xastir --current_time overlay.pos

Convert input file _overlay.pos_ to Xastir log format using current UTC time for timestamp and write it to standard out.

[RadarScope]: https://www.radarscope.app/
