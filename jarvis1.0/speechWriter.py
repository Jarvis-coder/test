from pocketsphinx import LiveSpeech, get_model_path
import os

model_path = get_model_path()


class translateSpeech:

    def createRUS(self):
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
            lm=os.path.join(model_path, 'ru.lm'),
            dic=os.path.join(model_path, 'ru.dic')
        )
        return speech

    def record(self):
        speech = self.createRUS()
        print("Скажите что вы хотите сделать?")
        for phrase in speech:
            print(phrase)