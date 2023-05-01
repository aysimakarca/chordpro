import re
import os

uniqueChordNames = ["A","B", "C", "D", "E", "F", "G"]       

def readChordProFile(chordProFile):
    with open(chordProFile, "r") as file:
        return file.read()

def getKey(content):
    pattern = r"{key:\s*([A-G][#b]?)\s*}"
    match = re.search(pattern, content)
    key = ''
    if match:
        key = match.group(1)
    return key

def getTitle(content, chordProFile):
    pattern = r"\{title:\s*(.*?)\s*\}"
    match = re.search(pattern, content)
    title = ''
    if match:
        title = match.group(1)
    else:
        title = os.path.splitext(os.path.basename(chordProFile))[0]
    return title

def getIntro(content):
    chordsOfIntro = []
    inIntro = False
    for line in content.split("\n"): 
        if '{c:intro:}' in line.lower() or '{c:intro}'in line.lower():
            inIntro = True
        elif inIntro:
            lineChords = getChordsOfALine(line, content)
            if len(lineChords) > 0:
                chordsOfIntro.extend(lineChords)
            else:
                inIntro = False
                break
    return chordsOfIntro

def getChorus(content):
    pattern = r"{soc}(.*?){eoc}"
    match = re.search(pattern, content, re.DOTALL)
    chords = []
    if match:
        chorus = match.group(1).strip()
        chord_pattern = r"\[([^\]]*)\]"
        chords = re.findall(chord_pattern, chorus)
    return chords


def getChordsOfALine(line, content):
    chord_pattern = r'\[([^\]]+)\]'
    lineChords = []
    if "chorus}" in line.lower():
        lineChords = getChorus(content)
    elif "repeat intro}" in line.lower():
        lineChords = getIntro(content)
    elif "[" in line:
        lineChords = re.findall(chord_pattern, line)   
    return lineChords

def cleanChords(chords):
    finalChords = []
    for chord in chords:
        chord = chord.replace("H", "B")
        chord = chord.replace("b", "-")
        chord = chord.replace("min", "m")
        chord = chord.replace("maj", "")
        chord = chord.replace("sus", "")
        chord = chord.replace("dim", "")
        if len(chord) > 3:
            chord = chord[0:3]
        chord = chord.replace("7", "")        
        chord = chord.replace("(", "")
        chord = chord.replace("+", "")
        chord = chord.replace("?", "")
        chord = chord.replace(".", "")
        chord = chord.split("/")[0]
        chord = chord.split("+")[0]
        chord = re.sub(r'\d+', '', chord)
        restWithoutAlphabethic = re.sub(r'[a-zA-Z]+', '', chord[1:]) 
        chord = chord[0] + restWithoutAlphabethic
        
        if chord[0:1] in uniqueChordNames:
            finalChords.append(chord)
    return finalChords



