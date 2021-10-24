import toolz
import re, itertools
from glob import iglob

def word_ratio(d):
    return float(d.get("a",0))/float(d.get("the",0.0001))

class PoemCleaner:
    def __init__(self):
        self.r = re.compile(r'[.,;:!-]')
    def clean_poem(self, fp):
        with open(fp) as poem:
            no_punc = self.r.sub("",poem.read())
            return no_punc.lower().split()

def word_is_desired(w):
    return w in ["a","the"]

def analyze_poems(poems, cleaner):
    return word_ratio(
        toolz.frequencies(
            filter(word_is_desired,
                itertools.chain(*map(cleaner.clean_poem, poems)))))

if __name__ == "__main__":

    cleaner = PoemCleaner()
    author1_poems = iglob("D:/Data/Poems/author_a/*.txt")
    author2_poems = iglob("D:/Data/Poems/author_b/*.txt")

    author1_ratio = analyze_poems(author1_poems, cleaner)
    author2_ratio = analyze_poems(author2_poems, cleaner)

    print("""
    Original_Poem:  0.3
    Author One:     {:.2f}
    Author Two:     {:.2f}
    """.format(author1_ratio, author2_ratio))