from chordpro_chord.chord_parser import cleanChords, getChordsOfALine, getChorus, getIntro, getKey, getTitle, readChordProFile


class Song:
    def __init__(self, chordProFile):
        self.chordProFile = chordProFile
        self.content = readChordProFile(chordProFile)
        self.chorus = self.getChorus()
        self.chords = self.getChords()
        self.title = self.getTitle()
        self.key = self.getKey()
        
    def getChords(self):
        chords = []
        for line in self.content.split("\n"): 
            lineChords = getChordsOfALine(line, self.content)
            chords.extend(cleanChords(lineChords))
        return chords
    
    def getChordsBeforeChorus(self):
        chords = []
        for line in self.content.split("\n"): 
            if 'chorus' in line.lower() or '{soc}'in line.lower() or '{start_of_chorus}'in line.lower():
                break
            lineChords = getChordsOfALine(line, self.content)
            chords.extend(cleanChords(lineChords))
        return chords
        
    def getChorus(self):
        return getChorus(self.content)
    
    def getIntro(self):
        return getIntro(self.content)
    
    def getTitle(self):
        return getTitle(self.content, self.chordProFile)
    
    def getKey(self):
        return getKey(self.content)
    