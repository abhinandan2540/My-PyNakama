Python Voice Recorder
---------------------------------------------------

* Importing dependencies
  
  ```bash
  pip install wavio
  pip install scipy
  ```

  in the code frequency referce the frequency for rocording, typically it varies between 44100 to 48000, and duration referce in seconds (s).
  ```bash
  sd.rec(int(frequency*duration))
  ```
  it is the formula for recording per cycle
  frequency is in **Hertz** and duration is in **seconds**
  and __frquency*duration__ = **Total number of audio samples**

  --------------------------------------------------------------------------------
  Thank You
  My-pyNakama
  
