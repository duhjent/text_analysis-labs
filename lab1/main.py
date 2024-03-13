from mitie import tokenize, load_entire_file, named_entity_extractor, to_default_str_type
from collections import Counter

ner = named_entity_extractor('./uk_model.dat')

with open('./ukr_text.txt') as file:
    f = file.read().lower()
# f = load_entire_file('./ukr_text.txt')

tokens = tokenize(f)
# print(to_default_str_type(tokens))

# cnt = Counter(to_default_str_type(t) for t in tokens)
# print([(to_default_str_type(x[0]), x[1]) for x in cnt.most_common(25)])
# print(cnt)

entities = ner.extract_entities(tokens)

for e in entities:
    range = e[0]
    tag = e[1]
    score = e[2]
    score_text = "{:0.3f}".format(score)
    entity_text = " ".join(tokens[i].decode() for i in range)
    print("   Score: " + score_text + ": " + tag + ": " + entity_text)
# print(entities)