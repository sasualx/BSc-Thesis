# BSc-Thesis

This is my Bachelors's Thesis.

I created a Drum accompaniment generator using Echo State Networks.
The whole process can be found in the Thesis.pdf file but I will make a short explanation here.

I start with GuitarPro files, preprocess them (code in GP-Filter). I convert them to midi using the following library: https://github.com/alexsteb/GuitarPro-to-Midi/blob/master/MidiExport.cs which I adapted to work with mono (code in GuitarPro-toMidi). And then I convert them to CSV.

The training and testing can be found in the folders ESN (without using output feedback) and ESN-Output-Feedback (using output feedback). And then the conversion back to midi can be found in the folder Final-Step.


In order to run these steps, one has to put the GuitarPro files in a Initial-Music-Sheet folder and run the bash scripts ./convert in order to convert the files and then run ./train-test-generate or ./train-test-generate-output-feedback depending if he wants output feedback or not.
