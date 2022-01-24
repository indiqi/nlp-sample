import spacy
import os
from pipe import select
import re


def humanise(text, corpus):
    nlp = spacy.load(os.path.join(
        os.path.dirname(__file__),
        "vendor",
        f"{corpus}-3.2.0")
    )
    doc = nlp(text.strip())
    sentences = list(
        [sentence.text for sentence in doc.sents]
        | select(lambda string: re.sub(r'\s([?.,!"](?:\s|$))', r"\1", string))
        | select(lambda string: string.strip())
        | select(lambda string: string.replace("\n", ""))
        | select(
            lambda string: string
            if ((len(string) > 1) and (string[-1] in ["!", ".", "?"]))
            else f"{string}."
        )
    )
    return "\n\n".join(sentences)


if __name__ == '__main__':
    datum = "there's a lot there and I think Jordan's is very , it's very interesting what he's doing . And I I only " \
            "I think it's really only possible because of how brilliant at doing it he is . But I also think that it " \
            "will fundamentally be insufficient what he's doing . Like I actually think it cannot work in just one on " \
            "one in that broadcast setting . I think the context has to be fundamentally different . Um I think , " \
            "I think where we can . Yeah . Yeah , I do I do think that I think you can do , I think there's room for " \
            "it to be a healthy thing . I'm not trying to be critical in that sense . I just it's how much do you " \
            "really want to help someone say what they want to say if maybe that's part of you that's not willing to " \
            "potentially go where you need to go in order to build up from the base required in order to help them " \
            "say it . I just , I don't know , I don't know if that's , I don't know if that's clear , but it's um the " \
            "way that guy is talking , it's like life and death , you must care about this . It is war . So that is " \
            "utilizing what is also of the commons in some sense , which is kind of like a righteous fervor to defend " \
            "the most sacred or something like this , you know , so um Like one doesn't just , you don't I don't know " \
            "if , I don't know if my I'd be careful about extending um rule omega in the wrong context and trying " \
            "seeking to enable that to to manifest as best it possibly can . If there isn't a deeper lurking , " \
            "you've got to be careful where you like , where you build it up from , basically . I don't know . I " \
            "don't know , mm hmm "
    print(humanise(datum, 'en_core_web_sm'))
