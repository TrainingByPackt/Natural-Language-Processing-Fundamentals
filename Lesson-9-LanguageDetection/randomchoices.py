import random
import torch 

languages = ['Arabic',
 'Chinese',
 'Czech',
 'Dutch',
 'English',
 'French',
 'German',
 'Greek',
 'Irish',
 'Italian',
 'Japanese',
 'Korean',
 'Polish',
 'Portuguese',
 'Russian',
 'Scottish',
 'Spanish',
 'Vietnamese']

def randomChoice(l):
    return l[random.randint(0, len(l) - 1)]

def randomTrainingExample():
    language = randomChoice(languages)
    line = randomChoice(language_to_names[language])
    language_index = languages.index(language)
    language_tensor = torch.tensor([language_index], dtype=torch.long)
    line_tensor = lineToTensor(line)
    return language, line, language_tensor, line_tensor