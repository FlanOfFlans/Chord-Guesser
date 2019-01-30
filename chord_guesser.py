import random
import time

notes_sharp = [
  "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", 
  "A", "A#", "B"]
notes_flat = [
  "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab",
  "A", "Bb", "B"]

keys = [
  "C", "G", "F", "D", "Bb", "A", "Eb", "E", "Db",
  "B", "F#"]

sharp_keys = [
  "C", "G", "D", "A", "E", "B", "F#"
] 

flat_keys = [
  "F", "Bb", "Eb", "Ab", "Db"
]

chords = [
  ["Major", 0, 4, 3],
  ["Minor", 0, 3, 4],
  ["Major 7th", 0, 4, 3, 4],
  ["Dominant 7th", 0, 4, 3, 3],
  ["Minor 7th", 0, 3, 4, 3]
]

response = ""
print("Input Q to exit.")
while True:
  root = keys[random.randint(0, 10)]
  if root in sharp_keys: possible_notes = notes_sharp
  else: possible_notes = notes_flat
  chord_type = chords[random.randint(0, 4)]
  notes_in = []
  note_num = possible_notes.index(root)
  for steps in chord_type:
    if type(steps) == str: continue
    note_num += steps
    notes_in.append(possible_notes[note_num % 12].lower())
  print("What notes are in %s %s?" % (root, chord_type[0]))
  response = input(">").lower()
  if(response == "q"): break
  response_list = response.split(" ")
  if response_list == notes_in: print("Correct!")
  else: print("Incorrect! %s" % notes_in)