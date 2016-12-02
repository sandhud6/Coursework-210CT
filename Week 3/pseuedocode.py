Sentence(Phrase)
    PhraseLen <-- LENGTH OF Phrase
    IF(Phrase)=1
        return Phrase
    return(Pharse[1]+ Sentence(Phrase[:-1])
