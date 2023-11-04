# Subtitle-Shens
Something something .ass subtitles
___
# Subdig.py

Split .ass subtitles into Dialogue and signs and songs tracks using certain keywords present in lines. The Dialogue track is saved as track_3.ass and the signs track as track_4.ass.
___
# Subdigest.py

Does the same thing but with CLI and is stolen from https://github.com/TypesettingTools/Myaamori-Aegisub-Scripts/blob/master/scripts/sub-digest/subdigest.py. 
Note: Instead of saving 2 other files, it splits the original file and does not keep it while the above one does. No idea if there is an argument to prevent this.

#### Usage:
`for %i in (*.ass); do python "subdigest.py" -i "%i" -o "%~ni_signs.ass" --selection-set style "Default|Alt|Italics|Dialogue|Flashback|Main|Top|Thoughts|Internal|Narrator|Naration|default|alt|italics|dialogue|flashback|main|top|thoughts|internal|narrator|narration" --remove-selected`
___
# Get_styles.py

To get styles present in the ass file that can be used in both of the above files.
___
# extract_all_fonts.py

This script extracts all font attachments of a Matroska file
Requirements: mkvtoolnix executables

Stolen from https://gist.github.com/FichteFoll/4488489
___
# mkvextractor.py

Extract anything from a Matroska (.mkv) file.

This Python script is to use MKVToolNix's mkvextract CLI tool. You can extract content from both MKV and WebM containers.

#### Usage
Open Terminal and type the below command. You can add one or more files at once.
`python mkvextractor.py [file_01] [file_02] [file_03]...`

Stolen from https://github.com/dropcreations/mkvextractor
