The Configuration of Emoji2Text Project
-----------------------------------------------------------------------------------

Converting emoticons or emojis into text in Python can be done using the demoji module. It is used to accurately remove and replace emojis in text strings. To install the demoji module the below command can be used: 
```bash 
pip install demoji
```
then you need to import demoji in your file
```bash
import demoji
```

In Crux
```bash
import demoji
text=""" any text input including emoji """
output=demoji.findall(text)
print(output)
```

Thank You
