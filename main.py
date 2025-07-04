import random

## I need to import my datasets so that I have something to generate coherent sentences from
from datasets import jieng_verbs
from datasets import jieng_pronouns
from datasets import possessive_pronouns
from datasets import family
from datasets import animals

## I need to make my function, I'll start off with SVO
def generate_dinka_sentence():

subject_focus = random.choice([jieng_pronouns, possessive_pronouns, family])

if subject_focus == "jieng_pronouns" :
  sentence = random.choice(list(jieng_pronouns.jieng_pronouns.key))
elif subject_focus == "family" :
  noun = random.choice(list(family.family.keys))
  subject = f"e {noun}"
  ### in this context "e" will be our determiner, as e is the equivalent for the english word "the"
else: ## fix this code
   possessive = random.choice(list(possessive_pronouns.possessive_pronouns.keys()))
        noun = random.choice(list(family.family.keys()))
        subject = f"{possessive} {noun}"

## I need to do verbs next, a similar approach
verb = random.choice(list(jieng_verbs.jieng_verbs.key))

## Next is the object
object = random.choice(list(animals.animals.key)) + list(family.family.keys()) + list(home.home.keys)) 
object = f"e {object}"

## To build a sentence using SVO, Subject, Verb, Object
sentence = f"{subject} {verb} {object}."
return sentence

### Have to adjust this
if __name__ == "__main__":
    for _ in range(5):
        print(generate_dinka_sentence())
