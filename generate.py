class Text():
    def __init__(self, text_file_name):
        self.text_file_name = text_file_name

    def fit(self):
        '''
            Приводим текст к нижнему регистру, очищаем от лишних символов
        и получаем словарь, в котором содержатся слова с частотами
        '''
        with open(self.text_file_name, 'r', encoding='utf-8') as text_file:
            text = text_file.read()
            # print(text)
            text = text.strip().lower()
            text = re.sub(r"[^\ Ёёа-яА-Я]", ' ', text)
            words = text.split()
            text = ' '.join(words)
            b = {}

            for i in range(len(words)):
                b[words[i]] = {}
                for j in range(len(words)):
                    if i != j:
                        len_finded_list = text.count(words[i]+' '+words[j])
                        if len_finded_list:
                            b[words[i]][words[j]] = len_finded_list

            d = {}
            for key in b:
                d[key] = [kiy for kiy in sorted(b[key], key=lambda n: b[key][n], reverse=True)]

            
            self.model = d

    def generate(self, length):
        random.seed(222)
        # 35
        condition = random.choice([key for key in self.model.keys()])
        last_word = condition
        added_words = [condition]
        text = condition
        for i in range(length):
            k = 0
            while True:
                next_word = self.model[last_word][k]
                if next_word in added_words and k < len(self.model[last_word]) - 1:
                    k += 1
                else:
                    break
            text += ' ' + next_word
            added_words.append(next_word)
            last_word = next_word
        return text


text1 = Text('for_study.txt')
text1.fit()
print(text1.generate(25))




