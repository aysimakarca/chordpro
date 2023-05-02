# Chordpro Parser
A python library to extract chord information from ChordPro files. It is able to extract the special parts like chorus, bridge, verse and extract chords of a song as an array.


### Parsing Chorus

You need to define chorus between the directives {soc} & {eoc} or {start_of_chorus} & {end_of_chorus}

Later chorus will be replaced when "{chorus}" is found in the chords.


### Parsing Bridge

You need to define bridge in the next line after directives ends with "c:bridge:}" or "c:bridge}". There shouldnt be an empty line after defining the bridge directive.

Later bridge  will be replaced when "repeat bridge}" is found in the chords.


### Parsing Intro

You need to define intro in the next line after directives ends with "c:intro:}" or "c:intro}". There shouldnt be an empty line after defining the intro directive.

Later intro  will be replaced when "repeat intro}" is found in the chords.

### Title

title should be defined as {title:xxx} otherwise the file name will be used as the title.


### The public functions are:

- readChordProFile
- getKey
- getTitle
- getIntro
- getChorus
- getBridge
- getChordsOfALine
- cleanChords
