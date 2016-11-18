from SoundLib import *

class myClass:
  index = 0
  
def main():
  #written by Brad Snurka
  #Version 0.3
  #10/28/16
  
  #100 BPM
  #1.6x faster than 60BPM
  #22050.0 samples per second
  #35280 samples per "beat"
  #4410 for eight note
  #2205 for sixteenth
  #17640 for half
  
  myClass.index = 0
  song = makeEmptySound(471879)
  a3 = note(220.00)
  g3 = note(195.998)
  b3 = note(246.942)
  c4 = note(261.626)
  f2 = note(87.3071)
  e2 = note(82.4069)
  g2 = note(97.9989)
  a2 = note(110.000)
  
  song = makeSong(a3, g3, b3, c4, f2, e2, g2, a2, song)
  song = normalize(song)
  print "index at end", myClass.index
  
  canvas = makeEmptySoundBySeconds(45)
  copy(song, canvas, 0) #Repeats our beat to be twice the song length
  #customSong = custom(song)
  #copy(song, canvas, 471879)
  reverse(canvas)
  mirrorSound(canvas)

  
  explore(canvas)
  #writeSoundTo(target, getMediaPath("song.wav"))
  
def makeSong(a3, g3, b3, c4, f2, e2, g2, a2, target):

  a3half = clip(a3, 0, 17640)
  a3eighth = clip(a3, 0, 4410)
  a3sixteen = clip(a3, 0 , 2205)
  g3half = clip(g3, 0, 17640)
  g3eighth = clip(g3, 0, 4410)
  g3sixteen = clip(g3, 0, 2205)
  b3half = clip(b3, 0, 17640)
  b3eighth = clip(b3, 0, 4410)
  b3sixteen = clip(b3, 0, 2205)
  c4half = clip(c4, 0, 17640)
  c4eighth = clip(c4, 0, 4410)
  c4sixteen = clip(c4, 0, 2205)
  f2eighth = clip(f2, 0, 4410)
  f2sixteen = clip(f2, 0, 2205)
  e2eighth = clip(e2, 0, 4410)
  e2sixteen = clip(e2, 0, 2205)
  g2eighth = clip(g2, 0, 4410)
  g2sixteen = clip(g2, 0, 2205)
  a2eighth = clip(a2, 0, 4410)
  a2sixteen = clip(a2, 0, 2205)
  
  copy(a3eighth, target, myClass.index)#
  count(8)
  copy(a3eighth, target, myClass.index)
  count(8)
  copy(a3sixteen, target, myClass.index)
  count(16)
  copy(g3sixteen, target, myClass.index)
  count(16)
  copy(a3eighth, target, myClass.index) #
  count(8) 
  count(4) #quarter rest
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(c4eighth, target, myClass.index)#
  count(8)
  copy(c4eighth, target, myClass.index)
  count(8)
  copy(c4sixteen, target, myClass.index)
  count(16)
  copy(b3sixteen, target, myClass.index)
  count(16)
  copy(c4eighth, target, myClass.index)#
  count(8)
  count(4)
  copy(g3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(a3eighth, target, myClass.index)#
  count(8)
  copy(a3eighth, target, myClass.index)
  count(8)
  copy(a3sixteen, target, myClass.index)
  count(16)
  copy(g3sixteen, target, myClass.index)
  count(16)
  copy(a3eighth, target, myClass.index) #
  count(8)
  count(4)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(c4eighth, target, myClass.index)#
  count(8)
  copy(c4eighth, target, myClass.index)
  count(8)
  copy(c4sixteen, target, myClass.index)
  count(16)
  copy(b3sixteen, target, myClass.index)
  count(16)
  copy(c4eighth, target, myClass.index)#
  count(8)
  count(4)
  copy(a3eighth, target, myClass.index)#
  count(8)
  copy(a3eighth, target, myClass.index)
  count(8)
  copy(a3sixteen, target, myClass.index)
  count(16)
  copy(g3sixteen, target, myClass.index)
  count(16)
  copy(a3eighth, target, myClass.index) #
  count(8) 
  count(4) #quarter rest
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(c4eighth, target, myClass.index)#
  count(8)
  copy(c4eighth, target, myClass.index)
  count(8)
  copy(c4sixteen, target, myClass.index)
  count(16)
  copy(b3sixteen, target, myClass.index)
  count(16)
  copy(c4eighth, target, myClass.index)#
  count(8)
  count(4)
  copy(g3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(a3eighth, target, myClass.index)#
  count(8)
  copy(a3eighth, target, myClass.index)
  count(8)
  copy(a3sixteen, target, myClass.index)
  count(16)
  copy(g3sixteen, target, myClass.index)
  count(16)
  copy(a3eighth, target, myClass.index) #
  count(8)
  count(4)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(c4eighth, target, myClass.index)#
  count(8)
  copy(c4eighth, target, myClass.index)
  count(8)
  copy(c4sixteen, target, myClass.index)
  count(16)
  copy(b3sixteen, target, myClass.index)
  count(16)
  copy(c4eighth, target, myClass.index)#
  count(8)
  copy(g3eighth, target, myClass.index)
  count(8)
  copy(b3eighth, target, myClass.index)
  count(8)
  copy(a3half, target, myClass.index)
  count(2)
  copy(c4half, target, myClass.index)
  count(3)
  copy(b3half, target, myClass.index)
  count(3)
  copy(g3half, target, myClass.index)
  count(3)
  
  copy(createChord(f2eighth, b3eighth), target, myClass.index)
  count(8)
  copy(createChord(f2eighth, b3eighth), target, myClass.index)
  count(8)
  copy(createChord(f2sixteen, c4sixteen), target, myClass.index)
  count(16)
  copy(createChord(e2sixteen, b3sixteen), target, myClass.index)
  count(16)
  copy(createChord(f2eighth, b3eighth), target, myClass.index)
  count(8)  
  return target
  
def count(note):
  index = myClass.index
  if (note == 8):
    index = index + 6615
  elif (note == 16):
    index = index + 3308
  elif (note == 4):
    index = index + 8820
  elif (note == 2):
    index = index + 26460
  elif (note == 3):
    index = index + 17640
    
  myClass.index = index
  
def note(freq):
  #Accepts a frequency and returns a sound for it by applying
  #  a factor to shift up or down from A440.
  factor = (freq/440.0)
  sound = makeSound(getMediaPath("a440.wav"))
  sound = shiftPitch(sound,factor)
  return sound
  
def shiftPitch(source, factor):
  #Written by: DL Largent based on Guzial & Ericson E4 Program 119
  #Date written: 10/16/13
  
  #Accepts a sound and a factor and returns a new sound
  #  shifted by the factor from the original sound.
  #  factor > 0 and < 1 will decrease pitch
  #  factor > 1 will increase pitch
  
  target = makeEmptySound(getLength(source))
  source_index = 0
  
  for target_index in range(0, getLength(target)):
    source_value = getSampleValueAt(source, int(source_index))
    setSampleValueAt(target, target_index, source_value)
    source_index = source_index + factor
    if (source_index >= getLength(source)):
      #Start over to allow new sound to be same length as original.
      source_index = 0
  
  return target
  
def createChord(note1, note2):
  #Accepts three sound files that are "notes" and returns a 
  #  combined sound that forms a chord.
  chord = makeEmptySound(getLength(note1))
  for index in range(0,getLength(note1)):
    note1Value = getSampleValueAt(note1,index)
    note2Value = getSampleValueAt(note2,index)
    tota1 = (note1Value + note2Value )/2
    setSampleValueAt(chord,index,tota1) 
  return chord
  
def normalize(src):
  loudest = getLoudest(src)
  multiplier = 32767.0/ loudest
  for s in getSamples(src):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s, louder)
  return src
  
def getLoudest(src):
  loudest = 0
  for s in getSamples(src):
    if (getSampleValue(s) > loudest):
      loudest = getSampleValue(s)
  return loudest
  
def echo(src, delay, num, start, end):
  delay = getSamplingRate(src) * delay
  srcLength = getLength(src)
  delayLength = srcLength + (delay * num)
  
  src2 = makeEmptySound(int(delayLength))
  
  echoAmplitude = 1.0
  for echoCount in range(0, num):
    echoAmplitude = echoAmplitude * .6
    for pos in range(start, end):
      pos2 = pos + (delay * echoCount)
      value = getSampleValueAt(src, pos) * echoAmplitude
      value2 = getSampleValueAt(src2, int(pos2))
      setSampleValueAt(src2, int(pos2), int(value+value2))
      
  return src2
  
def custom(src):
  for s in getSamples(src):
    setSampleValue(s, getSampleValue(s) * -1)
  return src