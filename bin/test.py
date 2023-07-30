from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("")

# voice = clone(
#     name="Voice Name",
#     description="An old American male voice with a slight hoarseness in his throat. Perfect for news.",
#     files=["./sample1.mp3", "./sample2.mp3"],
# )

text_sample = "ऊँचे ऊँचे वादी में बसते हैं भोले शंकर ऊँचे ऊँचे वादी में बसते हैं भोले शंकर";

# कैसी ये लगी मुझको तेरी लगन
# गाऊँ और झूमूँ होके तुझमे मगन
# शंभू!

# ऊँची ऊँची वादी में
# बसते हैं भोले शंकर
# ऊँची ऊँची वादी में
# बसते हैं भोले शंकर

# भोले भोले शंकर भोले भोले
# भोले भोले शंकर भोले

# रुद्र रूपा महादेवा";

audio = generate(text=text_sample, voice='Charlotte')

play(audio)

# history = History.from_api()
# print(history)
