# VOSK demo for the Ukrainian language

### Usage

1. Download model from this URL: https://drive.google.com/file/d/1MdlN3JWUe8bpCR9A0irEr-Icc1WiPgZs/view?usp=sharing 
   (you can also check out newer versions here: https://github.com/egorsmkv/speech-recognition-uk)

2. Unpack the archive into `data/model` folder

3. Save some WAV files in the `samples` folder

4. Install dependencies using **pipenv** and enter into the shell

   ```
   pipenv install
   pipenv shell
   ```

5. Run the recognizer

   ```
   python recognize.py
   ```
